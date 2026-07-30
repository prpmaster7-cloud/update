import os

RESET = '\x1b[0m'
DIM   = '\x1b[2;37m'
CY    = '\x1b[38;5;51m'


def box_line(char='─', color=DIM, length=47):
    print(f"{color}{char * length}{RESET}")


def linex():
    box_line('━', CY)


def clear():
    os.system('clear')
