import random

_selected = None


def _fb_android():
    ver   = f"{random.randint(350, 410)}.0.0.0.0"
    bv    = random.randint(100000000, 999999999)
    w, h  = random.choice([(1080,1920),(1080,2340),(1080,2400),(720,1280),(1440,3200)])
    den   = random.choice(['2.0', '2.5', '3.0', '3.5'])
    andv  = random.randint(9, 14)
    return (
        f"[FBAN/FB4A;FBAV/{ver};FBBV/{bv};"
        f"FBDM{{density={den},width={w},height={h}}};"
        f"FBLC/en_US;FBRV/0] Android/{andv}"
    )


def _fb_lite():
    ver  = f"{random.randint(300, 380)}.0.0.0.0"
    bv   = random.randint(100000000, 999999999)
    andv = random.randint(8, 13)
    return (
        f"[FBAN/FBLITE;FBAV/{ver};FBBV/{bv};"
        f"FBLC/en_US;FBRV/0] Android/{andv}"
    )


def _messenger():
    ver  = f"{random.randint(350, 420)}.0.0.0.0"
    bv   = random.randint(100000000, 999999999)
    andv = random.randint(9, 14)
    return (
        f"[FBAN/Orca-Android;FBAV/{ver};FBBV/{bv};"
        f"FBLC/en_US;FBRV/0] Android/{andv}"
    )


def _chrome_mobile():
    andv  = random.randint(9, 14)
    dev   = random.choice(['SM-G991B','SM-A525F','Redmi Note 10','M2101K6G','CPH2269','V2109'])
    major = random.randint(110, 124)
    build = random.randint(5000, 6800)
    patch = random.randint(1, 200)
    return (
        f"Mozilla/5.0 (Linux; Android {andv}; {dev}) "
        f"AppleWebKit/537.36 (KHTML, like Gecko) "
        f"Chrome/{major}.0.{build}.{patch} Mobile Safari/537.36"
    )


def _chrome_desktop():
    major = random.choice(range(120, 146))
    build = random.randint(6000, 7500)
    patch = random.randint(1, 300)
    nt    = random.choice(['10.0', '11.0'])
    return (
        f"Mozilla/5.0 (Windows NT {nt}; Win64; x64) "
        f"AppleWebKit/537.36 (KHTML, like Gecko) "
        f"Chrome/{major}.0.{build}.{patch} Safari/537.36"
    )


def _samsung_browser():
    andv  = random.randint(10, 14)
    dev   = random.choice(['SM-G991B','SM-S908B','SM-A536B','SM-G998B'])
    sbver = random.choice(['21.0','22.0','23.0','24.0'])
    major = random.randint(110, 120)
    build = random.randint(5000, 6500)
    return (
        f"Mozilla/5.0 (Linux; Android {andv}; {dev}) "
        f"AppleWebKit/537.36 (KHTML, like Gecko) "
        f"SamsungBrowser/{sbver} Chrome/{major}.0.{build}.0 Mobile Safari/537.36"
    )


def _opera_mobile():
    andv  = random.randint(9, 13)
    dev   = random.choice(['SM-G991B','Redmi Note 10','CPH2269'])
    major = random.randint(75, 85)
    cmaj  = random.randint(108, 120)
    build = random.randint(5000, 6500)
    return (
        f"Mozilla/5.0 (Linux; Android {andv}; {dev}) "
        f"AppleWebKit/537.36 (KHTML, like Gecko) "
        f"Chrome/{cmaj}.0.{build}.0 Mobile Safari/537.36 OPR/{major}.0.0.0"
    )


def _firefox_mobile():
    andv = random.randint(9, 14)
    ffv  = random.randint(110, 125)
    return (
        f"Mozilla/5.0 (Android {andv}; Mobile; rv:{ffv}.0) "
        f"Gecko/{ffv}.0 Firefox/{ffv}.0"
    )


def _firefox_desktop():
    ffv = random.randint(110, 125)
    return (
        f"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:{ffv}.0) "
        f"Gecko/20100101 Firefox/{ffv}.0"
    )


def _edge_mobile():
    andv  = random.randint(10, 14)
    dev   = random.choice(['SM-G991B','SM-A525F','Redmi Note 10'])
    major = random.randint(110, 122)
    build = random.randint(5000, 6800)
    edgev = f"{major}.0.{random.randint(1000,2000)}.{random.randint(1,99)}"
    return (
        f"Mozilla/5.0 (Linux; Android {andv}; {dev}) "
        f"AppleWebKit/537.36 (KHTML, like Gecko) "
        f"Chrome/{major}.0.{build}.0 Mobile Safari/537.36 EdgA/{edgev}"
    )


_UA_MAP = {
    '1':  _fb_android,
    '2':  _fb_lite,
    '3':  _messenger,
    '4':  _chrome_mobile,
    '5':  _chrome_desktop,
    '6':  _samsung_browser,
    '7':  _opera_mobile,
    '8':  _firefox_mobile,
    '9':  _firefox_desktop,
    '10': _edge_mobile,
    '11': lambda: random.choice([_fb_android, _fb_lite, _messenger])(),
    '12': lambda: random.choice([_fb_android, _fb_lite, _messenger, _chrome_mobile, _samsung_browser, _opera_mobile, _firefox_mobile, _edge_mobile])(),
    '13': lambda: random.choice(list(_UA_MAP.values()))(),
}


def set_ua(choice):
    global _selected
    _selected = choice


def get_ua():
    fn = _UA_MAP.get(_selected, _fb_android)
    return fn()


# legacy aliases
def window1(): return _chrome_desktop()
def windows(): return _chrome_desktop()
