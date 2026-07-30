import os
import sys

CY  = '\x1b[38;5;51m'
G   = '\x1b[38;5;46m'
Y   = '\x1b[38;5;220m'
DIM = '\x1b[2;37m'
RST = '\x1b[0m'

os.system('clear')
print(f"\n  {CY}KABBO{RST}  {DIM}─  Initializing...{RST}\n")

steps = [
    ('Checking dependencies',  'pip install requests urllib3 mechanize rich -q'),
    ('Refreshing packages',    'pip uninstall requests chardet urllib3 idna certifi -y -q && pip install chardet urllib3 idna certifi requests httpx beautifulsoup4 -q'),
]
for label, cmd in steps:
    sys.stdout.write(f"  {DIM}❯{RST}  {label}...  ")
    sys.stdout.flush()
    os.system(cmd)
    print(f"{G}done{RST}")

import requests
requests.urllib3.disable_warnings()

os.system('clear')

from security import kabbo_approval, anti_tamper_check, sec
from menu import BNG_71_

kabbo_approval()
os.system('clear')
anti_tamper_check()
sec()

sys.stdout.write('\x1b]2;𓆩 KABBO 👑 𓆪\x07')

if __name__ == '__main__':
    BNG_71_()
