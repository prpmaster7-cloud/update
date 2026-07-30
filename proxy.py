import requests
import itertools
import threading

_proxies = []
_cycle   = None
_clock   = threading.Lock()

CY  = '\x1b[38;5;51m'
G   = '\x1b[38;5;46m'
Y   = '\x1b[38;5;220m'
rad = '\x1b[38;5;196m'
DIM = '\x1b[2;37m'
RST = '\x1b[0m'


def _parse(line):
    parts = line.strip().split(':')
    if len(parts) == 4:
        host, port, user, pw = parts
        return {
            'http':  f'http://{user}:{pw}@{host}:{port}',
            'https': f'http://{user}:{pw}@{host}:{port}',
        }
    if len(parts) == 2:
        host, port = parts
        return {
            'http':  f'http://{host}:{port}',
            'https': f'http://{host}:{port}',
        }
    return None


def _validate(proxy_dict):
    try:
        r = requests.get('https://api.ipify.org', proxies=proxy_dict, timeout=8)
        return r.status_code == 200
    except Exception:
        return False


def load_proxies(path='proxy.txt', validate=True):
    global _proxies, _cycle
    raw = []
    try:
        with open(path, 'r') as f:
            raw = [l for l in f.read().splitlines() if l.strip() and not l.strip().startswith('#')]
    except FileNotFoundError:
        print(f"  {rad}✘  proxy.txt not found — running without proxy.{RST}")
        return

    print(f"  {DIM}❯{RST}  Validating {CY}{len(raw)}{RST} proxies...")
    good = []
    for line in raw:
        p = _parse(line)
        if p is None:
            continue
        if validate:
            if _validate(p):
                good.append(p)
                print(f"  {G}✔{RST}  {line.split(':')[0]}:{line.split(':')[1]}")
            else:
                print(f"  {rad}✘{RST}  {line.split(':')[0]}:{line.split(':')[1]}")
        else:
            good.append(p)

    _proxies = good
    _cycle   = itertools.cycle(good) if good else None
    print(f"  {G}✔{RST}  {len(good)}/{len(raw)} proxies active\n")


def next_proxy():
    """Return next proxy dict in rotation, or None if no proxies loaded."""
    global _cycle
    if _cycle is None:
        return None
    with _clock:
        return next(_cycle)
