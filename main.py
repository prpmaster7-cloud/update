import os
import sys
import requests

# Ensure required modules are installed
for module in ['requests', 'urllib3', 'mechanize', 'rich']:
    try:
        __import__(module)
    except ImportError:
        os.system(f'pip install {module}')

requests.urllib3.disable_warnings()

os.system('clear')
print(' \x1b[38;5;46mRAJA SERVER LOADING....')

os.system('pip uninstall requests chardet urllib3 idna certifi -y')
os.system('pip install chardet urllib3 idna certifi requests')
os.system('pip install httpx')
os.system('pip install beautifulsoup4')
print('loading Modules ...\n')
os.system('clear')

from security import raja_approval, anti_tamper_check
from menu import BNG_71_

raja_approval()

os.system('clear')
os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
os.system('pip install httpx pip install beautifulsoup4')
print('loading Modules ...\n')
os.system('clear')

anti_tamper_check()

sys.stdout.write('\x1b]2;𓆩【R.A.J.A 👑 】𓆪 \x07')

if __name__ == '__main__':
    BNG_71_()
