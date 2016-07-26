SuperUser="sudo"
CuckooUser="cuckoo"
TempDirectory=$(pwd)

CreateCuckooUser(){
    $SuperUser adduser  --disabled-password -gecos "" ${CuckooUser}
    $SuperUser usermod -G vboxusers ${CuckooUser}
    return 0
}

CreateHostOnlyInterface(){
    $SuperUser vboxmanage hostonlyif create
    $SuperUser iptables -A FORWARD -o eth0 -i vboxnet0 -s 192.168.56.0/24 -m conntrack --ctstate NEW -j ACCEPT
    $SuperUser iptables -A FORWARD -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
    $SuperUser iptables -A POSTROUTING -t nat -j MASQUERADE
    $SuperUser sysctl -w net.ipv4.ip_forward=1
    return 0
}

SettingUpTcpDump(){
    $SuperUser /bin/bash -c 'setcap cap_net_raw,cap_net_admin=eip /usr/sbin/tcpdump' 2>&/dev/null
    return 0
}

Jansson(){
    cd jansson
    autoreconf -vi --force
    ./configure
    make
    make check
    $SuperUser make install
    cd ${TempDirectory}
    return 0
}

Yara(){
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

Cuckoo(){
    cd cuckoo
    $SuperUsersudo pip install -r requirements.txt
    cd ${TempDirectory}
    return 0
}

Volatility(){
    tar xvf volatility-2.4.tar.gz
    cd volatility-2.4/
    $SuperUser python setup.py build
    $SuperUser python setup.py install
    return 0
}

Distorm(){
    cd distorm/
    $SuperUser python setup.py build
    $SuperUser python setup.py install
    return 0
}

# Create user and clone repos
CreateCuckooUser "Creating cuckoo user" "Could not create cuckoo user"

# Build packages
Yara "Building yara"
Jansson "Building jansson"
Distorm "Building distorm"
Volatility "Building volatility"
Cuckoo "Building cuckoo"

# Networking (latest, because sometimes it crashes...)
CreateHostOnlyInterface "Creating hostonly interface for cuckoo"
SettingUpTcpDump "Setting capabilities"
