import os
import sys
import colorama
import time
import requests
import random
import os
import json
from user_agent import generate_user_agent
from colorama import Fore, Style
import random
from time import sleep
from colorama import init, Fore, Back

init(autoreset=True)
if os.sys.platform == "win32":
    os.system("cls")
else:
    os.system("clear")
print(Back.GREEN + '', Fore.RED + " ▌ ▐·▄▄▄        ·▄▄▄·▄▄▄▄▄▄▄▄            ▄▄▌  .▄▄ · ", Back.GREEN + '')
print(Back.GREEN + '', Fore.RED + "▪█·█▌▀▄ █·▪     ▐▄▄·▐▄▄·•██  ▪     ▪     ██•  ▐█ ▀. ", Back.GREEN + '')
print(Back.GREEN + '', Fore.RED + "▐█▐█•▐▀▀▄  ▄█▀▄ ██▪ ██▪  ▐█.▪ ▄█▀▄  ▄█▀▄ ██▪  ▄▀▀▀█▄" , Back.GREEN + '')
print(Back.GREEN + '', Fore.RED + " ███ ▐█•█▌▐█▌.▐▌██▌.██▌. ▐█▌·▐█▌.▐▌▐█▌.▐▌▐█▌▐▌▐█▄▪▐█" + ' ', Back.GREEN + '')
print(Back.GREEN + '', Fore.RED + ". ▀  .▀  ▀ ▀█▄▀▪▀▀▀ ▀▀▀  ▀▀▀  ▀█▄▀▪ ▀█▄▀▪.▀▀▀  ▀▀▀▀ " + '    ', Back.GREEN + '')
print(Back.GREEN + '', Fore.RED + "                       1.1       ", Back.GREEN + '')
print(Back.GREEN + '', " =============================================", Back.GREEN + '')
print(Back.GREEN + '', "        Разработчик", Fore.CYAN + "XDEARBOY                " + '      ', Back.GREEN + '')
print(Back.GREEN + '', "        Обновления:", Fore.CYAN + "https://t.me/VROFFTEAM" + '      ', Back.GREEN + '')
print(Back.GREEN + '', " =============================================", Back.GREEN + '')
print(Back.GREEN + '', Back.BLACK + "                                              ", Back.GREEN + '')
print(Back.GREEN + '', Fore.YELLOW  + "                  Штучки" + '                 ', Back.GREEN + '')
print(Back.GREEN + '', Back.BLACK + "                                              ", Back.GREEN + '')
print(Back.GREEN + '', Back.BLACK + '             ' + Back.RED + 'Спасибо Матвею2207❤ ' + Back.BLACK + '                ' + Back.BLACK + '                        ' + Back.GREEN + "")
print(Back.GREEN + '', Fore.LIGHTMAGENTA_EX  + " 1.[Своровать логи с чужого стиллера из тг]       2.[Бомбер]       3.[Запустить селфбота]" + '', Back.GREEN + '')
print(Back.GREEN + '', Back.BLACK + "                                              ", Back.GREEN + '')
print(Back.GREEN + '', Fore.MAGENTA  + " '''''''''''''''''''''''''''''''''''''''''''' ", Back.GREEN + '')
while True:
    inp = int(input(Back.BLACK + ' ' + Back.BLACK + '  <$> ' + Fore.LIGHTBLACK_EX))
    try:
        if inp == 1:
            print(Fore.GREEN + 'Вы выбрали [Стырить логи из тг]')
            sleep(2)
            if os.sys.platform == "win32":
                os.system("cls")
            else:
                os.system("clear")
            os.system('CheckTgBot.exe')
    except Exception:
        print(Fore.RED + 'Ошибка, сообщите об ней xdearboю!!')
        sleep(2)
        if os.sys.platform == "win32":
            os.system("cls")
        else:
            os.system("clear")
        os.execl(sys.executable, sys.executable, *sys.argv)
    try:
        if inp == 2:
            print(Fore.GREEN + 'Вы выбрали [FZL-БОМБЕР]')
            sleep(2)
            if os.sys.platform == "win32":
                os.system("cls")
            else:
                os.system("clear")
            os.system('py fzlbomb.py')
    except Exception:
        print(Fore.RED + 'Ошибка, сообщите об ней xdearboю!')
        sleep(2)
        if os.sys.platform == "win32":
            os.system("cls")
        else:
            os.system("clear")
        os.execl(sys.executable, sys.executable, *sys.argv)
    try:
        if inp == 3:
            print(Fore.GREEN + 'Вы выбрали [Запустить селфбота] , что-бы выйти нажмите CTRL+C')
            sleep(5)
            if os.sys.platform == "win32":
                os.system("cls")
            else:
                os.system("clear")
            os.system('mainnn.exe')
            
    except Exception:
        print(Fore.RED + 'Ошибка, сообщите об ней xdearboю!!')
        sleep(2)
        if os.sys.platform == "win32":
            os.system("cls")
        else:
            os.system("clear")
        os.execl(sys.executable, sys.executable, *sys.argv)




input()
