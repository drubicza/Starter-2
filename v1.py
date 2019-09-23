import os, sys
from time import sleep
BK = '\x1b[0;30m'
BL = '\x1b[0;34m'
GN = '\x1b[0;32m'
CY = '\x1b[0;36m'
R = '\x1b[0;31m'
PE = '\x1b[0;35m'
BW = '\x1b[0;33m'
LG = '\x1b[0;37m'
DG = '\x1b[1;30m'
LB = '\x1b[1;34m'
LGN = '\x1b[1;32m'
LC = '\x1b[1;36m'
LR = '\x1b[1;31m'
LP = '\x1b[1;35m'
Y = '\x1b[1;33m'
W = '\x1b[1;37m'
MN = '\x1b[101m'
MS = '\x1b[0m'

def menu():
    os.system('clear')
    print((LR + '╔══╗╔══╗╔══╗╔═╗╔══╗╔═╗╔═╗'))
    print((LR + '║══╣╚╗╔╝║╔╗║║╬║╚╗╔╝║╦╝║╬║'))
    print((W + '╠══║─║║─║╠╣║║╗╣─║║─║╩╗║╗╣'))
    print((W + '╚══╝─╚╝─╚╝╚╝╚╩╝─╚╝─╚═╝╚╩╝   ' + Y + 'v1'))
    print((W + '───────────────────────────────'))
    print((W + 'Author : Mr.iVx7'))
    print((W + '───────────────────────────────'))
    print((LGN + '{ ' + W + '1' + LGN + ' } ' + W + 'Package'))
    print((LGN + '{ ' + W + '2' + LGN + ' } ' + W + 'Tampilan'))
    print((LGN + '{ ' + W + '3' + LGN + ' } ' + W + 'Informasi'))
    print('')
    print((LGN + '{ ' + W + '0' + LGN + ' } ' + W + 'Exit'))
    print('')
    pilih = input((W + '[ ' + LR + 'Choice' + W + ' ] ' + LGN + '•>' + LC + '  '))
    if pilih == '1' or pilih == '01':
        play()
    elif pilih == '2' or pilih == '02':
        tampilan()
    elif pilih == '3' or pilih == '03':
        os.system('clear')
        info()
    elif pilih == '0' or pilih == '00':
        print((W + ''))
        os.system('login')
    else:
        print('')
        print((W + 'Wrong Input !!'))
        print('')
        asq = input((W + '[ ' + LR + 'Kembali' + W + ' ]'))
        os.system('clear')
        menu()


def play():
    os.system('clear')
    print((LB + '[ ! ] Download Starting...'))
    sleep(4)
    print((LR + '[ ! ] Please Dont Turn Off Your System..'))
    sleep(4)
    print((W + ' '))
    os.system('apt update && apt upgrade && apt install curl && apt install git && apt install wget && pkg install python2 && pkg install python2 && pkg install root-repo && pkg install unstable-repo && pkg install x11-repo && apt install ruby && apt install cowsay && apt install clang && apt install apt install figlet && gem install lolcat && apt install neofetch && apt install openssh && apt install toilet && apt install nodejs && apt install mc')
    sleep(3)
    print((LGN + '[ ● ] Installing is Done..'))
    print('')
    jas = input((W + '[ ' + LR + 'Kembali ' + W + ']'))
    sleep(2)
    os.system('clear')
    menu()


def info():
    os.system('clear')
    print((LGN + '▬▬▬▬▬▬▬▬▬▬▬▬▬▬' + W + '' + Y + '✦' + W + 'Informasi' + Y + '✦' + LGN + '▬▬▬▬▬▬▬▬▬▬▬▬▬▬'))
    sleep(2)
    print((W + '* Tools ini Adalah Tools Installer.. '))
    sleep(2)
    print('* Tools ini Tidak berbahaya sama sekali.. ')
    sleep(2)
    print('* Tools ini dibuat tanggal 6 / 9 / 2019..')
    sleep(2)
    print('* Tools ini Versi 1.0')
    sleep(2)
    print('* Github : https://github.com/ivx7 ')
    print((LGN + '▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬'))
    print('')
    hoq = input((W + '[ ' + LR + 'Kembali' + W + ' ]'))
    os.system('clear')
    menu()


def tampilan():
    os.system('clear')
    os.system('bash v1.sh')
    os.system('clear')
    os.system('login')


menu()
