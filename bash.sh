SuperUser="sudo"
CuckooUser="cuckoo"
TempDirectory=$(pwd)

create_cuckoo_user(){
    $SuperUser adduser  --disabled-password -gecos "" ${CuckooUser}
    $SuperUser usermod -G vboxusers ${CuckooUser}
    return 0
}

create_hostonly_iface(){
    $SuperUser vboxmanage hostonlyif create
    $SuperUser iptables -A FORWARD -o eth0 -i vboxnet0 -s 192.168.56.0/24 -m conntrack --ctstate NEW -j ACCEPT
    $SuperUser iptables -A FORWARD -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
    $SuperUser iptables -A POSTROUTING -t nat -j MASQUERADE
    $SuperUser sysctl -w net.ipv4.ip_forward=1
    return 0
}

setcap(){
    $SuperUser /bin/bash -c 'setcap cap_net_raw,cap_net_admin=eip /usr/sbin/tcpdump' 2>&/dev/null
    return 0
}

build_jansson(){
    cd jansson
    autoreconf -vi --force
    ./configure
    make
    make check
    $SuperUser make install
    cd ${TempDirectory}
    return 0
}

build_yara(){
    cd yara
    ./bootstrap.sh
    $SuperUser autoreconf -vi --force
    ./configure --enable-cuckoo --enable-magic
    make
    $SuperUser make install
    cd yara-python/
    $SuperUser python setup.py install
    cd ${TempDirectory}
    return 0
}

build_cuckoo(){
    cd cuckoo
    $SuperUsersudo pip install -r requirements.txt
    cd ${TempDirectory}
    return 0
}

build_volatility(){
    tar xvf volatility-2.4.tar.gz
    cd volatility-2.4/
    $SuperUser python setup.py build
    $SuperUser python setup.py install
    return 0
}

build_distorm(){
    cd distorm/
    $SuperUser python setup.py build
    $SuperUser python setup.py install
    return 0
}

# Create user and clone repos
create_cuckoo_user "Creating cuckoo user" "Could not create cuckoo user"

# Build packages
    
build_jansson "Building jansson"
build_yara "Building yara"
build_distorm "Building distorm"
build_volatility "Building volatility"
build_cuckoo "Building cuckoo"

# Configuration
fix_django_version "Fixing django problems on old versions"
enable_mongodb "Enabling mongodb in cuckoo"

# Networking (latest, because sometimes it crashes...)
create_hostonly_iface "Creating hostonly interface for cuckoo"
setcap "Setting capabilities"
