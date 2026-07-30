import os
import sys
import time
import hashlib
import requests
from requests import api, models, sessions
from config import G, Y, W, CY, rad, RESET, DIM, TOOL_VERSION, TOOL_NAME
from utils import box_line


def kabbo_approval():
    os.system('clear')
    uuid_raw = str(os.getlogin()) + str(os.getuid())
    key = hashlib.md5(uuid_raw.encode()).hexdigest().upper()[:12]
    github_link = "https://github.com/prpmaster7-cloud/KABBO-CK/blob/main/approval.txt"

    print(f"""
{CY}  ██╗  ██╗ █████╗ ██████╗ ██████╗  ██████╗
{CY}  ██║ ██╔╝██╔══██╗██╔══██╗██╔══██╗██╔═══██╗
{G}  █████╔╝ ███████║██████╔╝██████╔╝██║   ██║
{G}  ██╔═██╗ ██╔══██║██╔══██╗██╔══██╗██║   ██║
{Y}  ██║  ██╗██║  ██║██████╔╝██████╔╝╚██████╔╝
{Y}  ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═════╝  ╚═════╝{RESET}""")

    box_line('═', CY)
    print(f"  {W}YOUR KEY  {RESET} {DIM}│{RESET}  {G}KABBO-{key}{RESET}")
    box_line()
    print(f"  {W}BINANCE   {RESET} {DIM}│{RESET}  {Y}1185161524{RESET}")
    box_line('═', CY)
    print(f"\n  {W}Status  {RESET} {DIM}│{RESET}  {Y}Verifying license...{RESET}\n")

    try:
        response = requests.get(github_link).text
        if f"KABBO-{key}" in response:
            print(f"  {G}✔  Access Granted — Welcome to {TOOL_NAME} {TOOL_VERSION} 🔥{RESET}")
            time.sleep(1.5)
        else:
            print(f"  {rad}✘  Key not approved. Contact admin.{RESET}")
            sys.exit()
    except Exception:
        sys.exit()


def anti_tamper_check():
    try:
        api_body     = open(api.__file__, 'r').read()
        models_body  = open(models.__file__, 'r').read()
        session_body = open(sessions.__file__, 'r').read()
        for word in ['print', 'lambda', 'zlib.decompress']:
            if word in api_body or word in models_body or word in session_body:
                exit()
    except Exception:
        pass


class sec:
    def __init__(self):
        paths = [
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/sessions.py',
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/api.py',
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/models.py',
        ]
        for path in paths:
            try:
                if 'print' in open(path, 'r').read():
                    self._terminate()
            except Exception:
                pass
        if os.path.exists('/storage/emulated/0/x8zs/app_icon/com.guoshi.httpcanary.png'):
            self._terminate()
        if os.path.exists('/storage/emulated/0/Android/data/com.guoshi.httpcanary'):
            self._terminate()

    def _terminate(self):
        print(f'\x1b[1;32m  Security check failed. Exiting.{RESET}')
        exit()
