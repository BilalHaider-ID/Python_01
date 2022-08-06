# import Pythom Modules --> [ libraries ]
from os import system as cmd 
from time import sleep as slp
import sys,platform
from datetime import date,datetime
# Create Different Function --> [ Def ]
def clear_screen():
    if sys.platform.lower() == "linux":
        slp(0.5)
        cmd("clear")
    elif sys.platform.lower() == "win":
        slp(0.5)
        cmd("cls")
    else:
        slp(0.5)
        cmd("clear")
def chack_time():
    now = datetime.now()
    hours = now.hour
    if hours in [21,22,23,24,1,2,3,4]:
        time_now = "Good Night Bro"
    elif hours in [5,6,7,8,9]:
        time_now = "Good Morning Bro"
    elif hours in [10,11,12,13,14,15]:
        time_now = "Good Afternoon Bro"
    elif hours in [16,17,18,19,20]:
        time_now = "Good Evening Bro"
    return time_now
# Create logo --> [ Banner ]
def logo():
    clear_screen()
    print(" ")
# Create main menu --> [ Function ]
def menu():
    logo()
    print("[01]")
    print("[02]")
    print("[03]")
    print("[04]")
    print("[05]")
    print("[06]")
    ch = input('\n[->] Choose : ')
    if ch in ["1","01"]:
        pass
    else:
        menu()
if __name__=='__main__':
    #menu()
    c = chack_time()
    print(c)
