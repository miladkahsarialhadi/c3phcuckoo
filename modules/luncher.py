from modules.header import Colors
from subprocess import DEVNULL
import subprocess 
import os


class Luncher():
    def __init__(self):
        self.color = Colors()
    
    def git(self, *args):
        subprocess.check_call(['git'] + list(args), stdout=DEVNULL, stderr=DEVNULL)
        return True

    def super_uid(self):
        self.euid = os.geteuid()
        if (self.euid != 0):
            self.color.print_purple("You must run this script with root privilege!")
            raise EnvironmentError("Need to be root!")
    
    def update_ubuntu(self):
        self.aptUp = "apt-get update"
        self.aptUpG = "apt-get upgrade"
        self.distUp = "apt-get dist-upgrade"
        
        self.color.print_green("[+] Phase 1 : Upgrading of the ubuntu repository is starting:")
        
        if (subprocess.run(self.aptUp.split(), stdout=DEVNULL, stderr=DEVNULL)):
            self.color.print_blue("\t[+] apt repository updated")
            
        if (subprocess.run(self.aptUpG.split(), stdout=DEVNULL, stderr=DEVNULL)):
            self.color.print_blue("\t[+] apt repository upgraded") 
            
        if (subprocess.run(self.distUp.split(), stdout=DEVNULL, stderr=DEVNULL)):
            self.color.print_blue("\t[+] apt dist upgraded")
        
        self.color.print_red("[+] Phase 1 Accomplished.\n")
    
    def package_installation(self):
        self.apt = "apt install -y "
        self.packages = "wget python-pip python-sqlalchemy mongodb python-bson python-dpkt python-jinja2 python-magic python-gridfs python-libvirt python-bottle python-pefile python-chardet git build-essential autoconf automake libtool dh-autoreconf libcurl4-gnutls-dev libmagic-dev python-dev libffi-dev libssl-dev tcpdump libcap2-bin virtualbox dkms python-pyrex"
        
        self.color.print_green("[+] Phase 2 : Installation of the ubuntu packages is starting:")
        
        for self.items in self.packages.split():
            self.command = str(self.apt) + str(self.items)
            
            if (subprocess.run(self.command.split(), stdout=DEVNULL, stderr=DEVNULL)):
                self.color.print_blue("\t[+] Package [{}] Installed".format(str(self.items)))
            else:
                self.color.print_red("\t[+] Package [{}] Don't Installed".format(str(self.items)))
                
        self.color.print_red("[+] Phase 2 Accomplished.\n")
    
    def essentials_installation(self):
        self.apt = "pip3 install "
        self.packages = "pymongo django pydeep maec py3compat lxml cybox distorm3 pycrypto"
        
        self.color.print_green("[+] Phase 3 : Installation of the essential packages of cuckoo is starting:")
        
        for self.items in self.packages.split():
            self.command = str(self.apt) + str(self.items)
            
            if (subprocess.run(self.command.split(), stdout=DEVNULL, stderr=DEVNULL)):
                self.color.print_blue("\t[+] Package [{}] Installed".format(str(self.items)))
            else:
                self.color.print_red("\t[+] Package [{}] Don't Installed".format(str(self.items)))
                
        self.color.print_red("[+] Phase 3 Accomplished.\n")
    
    def get_softwares(self):
        self.getYara = "https://github.com/plusvic/yara.git"
        self.getCuckoo = "https://github.com/cuckoosandbox/cuckoo.git"
        self.getJansson = "https://github.com/akheron/jansson.git"
        self.getVolatility = "wget http://downloads.volatilityfoundation.org/releases/2.4/volatility-2.4.tar.gz"
        
        self.color.print_green("[+] Phase 4 : Getting of the softwares is starting:")
        
        if (self.git("clone", self.getYara)):
            self.color.print_blue("\t[+] Cloning of the Yara is finished.")
        else:
            self.color.print_blue("\t[+] Cloning of the Yara isn't finished.")
        
        if (self.git("clone", self.getCuckoo)):
            self.color.print_blue("\t[+] Cloning of the Cuckoo is finished.")
        else:
            self.color.print_blue("\t[+] Cloning of the Cuckoo isn't finished.")
            
        if (self.git("clone", self.getJansson)):
            self.color.print_blue("\t[+] Cloning of the Jonsson is finished.")
        else:
            self.color.print_blue("\t[+] Cloning of the Jonsson isn't finished.")
        
        if (subprocess.run(self.getVolatility.split(), stdout=DEVNULL, stderr=DEVNULL)):
            self.color.print_blue("\t[+] Cloning of the Volatility is finished.")
        else:
            self.color.print_red("\t[+] Cloning of the Volatility is finished.")
            
        
        self.color.print_red("[+] Phase 4 Accomplished.\n")    
    
    def configuration_packages(self):
        self.command = "sudo sh ./bash.sh"
        
        self.color.print_green("[+] Phase 5 : Configuration of packages are starting:")
        
        if (subprocess.run(self.command.split(), stdout=DEVNULL, stderr=DEVNULL)):
            self.color.print_blue("\t[+] Configuration is finished.")
        else:
            self.color.print_blue("\t[+] Configuration isn't finished.")
        
        self.color.print_red("[+] Phase 5 Accomplished.\n")
    
    def operational(self):
        try:
            self.super_uid()
            self.update_ubuntu()
            self.package_installation()
            self.essentials_installation()
            self.get_softwares()
            self.configuration_packages()
            
        except Exception as e:
            self.color.print_red_exception("Exception Occured : ", e)
        
        