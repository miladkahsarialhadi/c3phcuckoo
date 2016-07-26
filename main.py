#!/usr/bin/python3

"""
    C3ph Cuckoo is a tool that designed to install cuckoo sandbox automatically. 
    
    Author      : Milad Kahsari Alhadi @c3phalexin
    Email       : the.cephalexin[at]gmail[dot].com
    Home Page   : http://Myfreetime.ir/
    
"""
from modules.header import Headers
from modules.luncher import Luncher


class EntryPoint:
    def __init__(self):
        self.c3phCuckooHeader = Headers()
        self.c3phCuckooLuncher = Luncher()
        
    def start_tool(self):
        self.c3phCuckooHeader.main_header()
        self.c3phCuckooHeader.main_menu()
        self.c3phCuckooLuncher.operational()

if __name__ == "__main__":
    c3phCuckoo = EntryPoint()
    c3phCuckoo.start_tool()