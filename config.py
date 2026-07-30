import threading

method = []
oks    = []
cps    = []
user   = []
loop   = 0
_lock  = threading.Lock()


def inc_loop():
    global loop
    with _lock:
        loop += 1


def add_ok(uid):
    with _lock:
        oks.append(uid)

# ── Colour Palette ──────────────────────────────────────────
RESET  = '\x1b[0m'
BOLD   = '\x1b[1m'
W      = '\x1b[1;97m'
G      = '\x1b[38;5;46m'
Y      = '\x1b[38;5;220m'
CY     = '\x1b[38;5;51m'
BL     = '\x1b[38;5;27m'
rad    = '\x1b[38;5;196m'
DIM    = '\x1b[2;37m'
X      = W
PP     = '\x1b[38;5;203m'
RR     = '\x1b[38;5;196m'
GS     = '\x1b[38;5;40m'

# ── Branding ────────────────────────────────────────────────
TOOL_NAME    = 'KABBO'
TOOL_VERSION = 'v3.0.0'
TOOL_AUTHOR  = 'KABBO CYBER'
TOOL_FB      = 'KABBO CLONER'
TOOL_GITHUB  = 'prpmaster7-cloud'
TOOL_TG      = 'KABBO OFFICIAL'
