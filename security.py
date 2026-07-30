import os
import sys
import time
import hashlib
import requests
from requests import api, models, sessions


def raja_approval():
    os.system('clear')
    uuid_raw = str(os.getlogin()) + str(os.getuid())
    key = hashlib.md5(uuid_raw.encode()).hexdigest().upper()[:12]
    github_link = "https://github.com/prpmaster7-cloud/KABBO-CK/blob/main/approval.txt"

    print('''\n\033[1;31m ██████╗  █████╗      ██╗ █████\x1b[0m╗ \n\033[1;32m ██╔══██╗██╔══██╗     ██║██╔══██╗\x1b[0m\n\033[1;33m ██████╔╝███████║     ██║███████║\x1b[0m\n\033[1;34m ██╔══██╗██╔══██║██   ██║██╔══██║\x1b[0m\n\033[1;35m ██║  ██║██║  ██║╚█████╔╝██║  ██║\x1b[0m\n\033[1;36m ╚═╝  ╚═╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝\x1b[0m''')
    print('\x1b[38;5;48m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print(f"\x1b[1;37m YOUR KEY : \x1b[1;32mRAJA-{key}")
    print('\x1b[38;5;48m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print("\033[1;32m BINANCE ID : 1185161524 \033[0m")
    print('\x1b[38;5;48m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print("\033[1;36m💵 Available TOOL PRICES\033[0m")
    print("\033[1;31m" + "━" * 40 + "\033[0m")
    print("\033[1;32m[1] 5 Dollars 7 days \033[0m")
    print("\033[1;33m[2] 10 Dollars 15 days \033[0m")
    print("\033[1;34m[3] 18 Dollars 30 days \033[0m")
    print("\033[1;31m" + "━" * 40 + "\033[0m")
    print(" \x1b[1;37mStatus: \x1b[1;31mChecking Approval...")

    try:
        response = requests.get(github_link).text
        if f"RAJA-{key}" in response:
            print(" \33[32;41m\t Welcome RAJA TOOL 🔥\33[0;m.")
            time.sleep(2)
        else:
            print(" \x1b[1;31mKey Is Not Approved Please Contact The Admin .")
            os.system(f'xdg-open https://wa.me/+923229120975?text=Mera-Key-Approve-Kardo-RAJA-{key}')
            sys.exit()
    except:
        sys.exit()


def anti_tamper_check():
    try:
        api_body = open(api.__file__, 'r').read()
        models_body = open(models.__file__, 'r').read()
        session_body = open(sessions.__file__, 'r').read()
        word_list = ['print', 'lambda', 'zlib.decompress']
        for word in word_list:
            if word in api_body or word in models_body or word in session_body:
                exit()
    except:
        pass


class sec:
    def __init__(self):
        self.__module__ = __name__
        self.__qualname__ = 'sec'
        paths = [
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/sessions.py',
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/api.py',
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/models.py'
        ]
        for path in paths:
            if 'print' in open(path, 'r').read():
                self.fuck()
        if os.path.exists('/storage/emulated/0/x8zs/app_icon/com.guoshi.httpcanary.png'):
            self.fuck()
        if os.path.exists('/storage/emulated/0/Android/data/com.guoshi.httpcanary'):
            self.fuck()

    def fuck(self):
        print(' \x1b[1;32m Congratulations ! ')
        self.linex()
        exit()

    def linex(self):
        print('\x1b[38;5;48m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
