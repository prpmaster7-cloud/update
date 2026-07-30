import os
import sys
import requests

for module in ['requests', 'urllib3', 'mechanize', 'rich']:
    try:
        __import__(module)
    except ImportError:
        os.system(f'pip install {module} -q')

requests.urllib3.disable_warnings()

os.system('clear')
print('\x1b[38;5;51m  KABBO — Loading...\x1b[0m')

os.system('pip uninstall requests chardet urllib3 idna certifi -y -q')
os.system('pip install chardet urllib3 idna certifi requests httpx beautifulsoup4 -q')
os.system('clear')

from security import kabbo_approval, anti_tamper_check
from menu import BNG_71_

kabbo_approval()
os.system('clear')
anti_tamper_check()

sys.stdout.write('\x1b]2;𓆩 KABBO 👑 𓆪\x07')

if __name__ == '__main__':
    BNG_71_()
