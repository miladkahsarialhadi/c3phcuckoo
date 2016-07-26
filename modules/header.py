import random

class Colors:
    def __init__(self):
        self.PURPLE = '\033[95m'
        self.YELLOW = '\033[93m'
        self.CYAN = '\033[96m'
        self.BLUE = '\033[94m'
        self.GREEN = '\033[92m'
        self.RED = '\033[91m'
        self.ENDC = '\033[0m'
    
    def print_purple(self, __string):
        print(self.PURPLE + __string + self.ENDC)
        
    def print_yellow(self, __string):
        print(self.YELLOW + __string + self.ENDC)
    
    def print_cyan(self,__string):
        print(self.CYAN + __string + self.ENDC)
    
    def print_blue(self, __string): 
        print(self.BLUE + __string + self.ENDC)        
    
    def print_green(self, __string):
        print(self.GREEN + __string + self.ENDC)    
        
    def print_red(self, __string):
        print(self.RED + __string + self.ENDC)
        
    def print_message(self, __string):
        print(self.RED + "[+] " + self.GREEN + __string + self.ENDC)
        
    def print_red_exception(self, __string, __exception):
        print(self.RED + __string + self.GREEN + str(__exception) + self.ENDC)

class Headers():
    def __init__(self):
        self.colors = Colors()
        
        self.headerOne = r"""
                         .--.             .-.               
            : .--'            : :.-.            
            : :   .-..-. .--. : `'.' .--.  .--. 
            : :__ : :; :'  ..': . `.' .; :' .; :
            `.__.'`.__.'`.__.':_;:_;`.__.'`.__.'
                    """
    
        self.headerTwo = r"""
             CCCCC                 kk                   
            CC    C uu   uu   cccc kk  kk  oooo   oooo  
            CC      uu   uu cc     kkkkk  oo  oo oo  oo 
            CC    C uu   uu cc     kk kk  oo  oo oo  oo 
             CCCCC   uuuu u  ccccc kk  kk  oooo   oooo                                 
                    """    
    
        self.headerThree = r"""

             .d8888b.                 888                      
            d88P  Y88b                888                      
            888    888                888                      
            888       888  888 .d8888b888  888 .d88b.  .d88b.  
            888       888  888d88P"   888 .88Pd88""88bd88""88b 
            888    888888  888888     888888K 888  888888  888 
            Y88b  d88PY88b 888Y88b.   888 "88bY88..88PY88..88P 
             "Y8888P"  "Y88888 "Y8888P888  888 "Y88P"  "Y88P"         
                        """
    
        self.headerFour = r"""
    

              .,-:::::  ...    :::  .,-:::::  :::  .      ...         ...     
            ,;;;'````'  ;;     ;;;,;;;'````'  ;;; .;;,..;;;;;;;.   .;;;;;;;.  
            [[[        [['     [[[[[[         [[[[[/' ,[[     \[[,,[[     \[[,
            $$$        $$      $$$$$$        _$$$$,   $$$,     $$$$$$,     $$$
            `88bo,__,o,88    .d888`88bo,__,o,"888"88o,"888,_ _,88P"888,_ _,88P
              "YUMMMMMP""YmmMMMM""  "YUMMMMMP"MMM "MMP" "YMMMMMP"   "YMMMMMP"                      
                        """
                    
        self.headerFinal = r"""

             _____            _               
            /  __ \          | |              
            | /  \/_   _  ___| | _____   ___  
            | |   | | | |/ __| |/ / _ \ / _ \ 
            | \__/\ |_| | (__|   < (_) | (_) |
             \____/\__,_|\___|_|\_\___/ \___/ 
                        """
        
    def main_header(self):
        self.numbersOfHeader = random.randint(1, 5)
        
        if (self.numbersOfHeader == 1):
            self.colors.print_yellow(self.headerOne)
        elif (self.numbersOfHeader == 2):
            self.colors.print_yellow(self.headerTwo)
        elif (self.numbersOfHeader == 3):
            self.colors.print_yellow(self.headerThree)
        elif (self.numbersOfHeader == 4):
            self.colors.print_yellow(self.headerFour)
        elif (self.numbersOfHeader == 5):
            self.colors.print_yellow(self.headerFinal)

    def main_menu(self):
        bracketS = self.colors.BLUE + "{" + self.colors.ENDC
        bracketF = self.colors.BLUE + "}" + self.colors.ENDC
        
        print("\t\t--=" + bracketS + self.colors.CYAN + "Written by Milad Kahsari Alhadi" + self.colors.ENDC + bracketF)
        print("\t\t--=" + bracketS + self.colors.GREEN + "C3ph Cuckoo Auto Installer" + self.colors.ENDC + bracketF)
        print("\t\t--=" + bracketS + "Update Date : [" + self.colors.RED + "24.01.2016" + self.colors.ENDC + "]" + bracketF)
        
        print("\n\n")