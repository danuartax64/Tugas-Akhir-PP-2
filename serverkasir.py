from socket import AF_INET, SOCK_STREAM, socket, timeout
from threading import Thread
import time
from sys import exit

clients = []

host = '192.168.210.205'
port = 4200
s = socket(AF_INET, SOCK_STREAM)

def Connecting():
    s.bind((host, port))
    print("Koneksi berhasil dibuka")
    s.listen()

def listen():
    while a == True:
        try:
            s.settimeout(1)
            clients.append(s.accept())
        except:
            pass

def write():
    while a == True:
        for c in clients:
            try:
                c[0].settimeout(1)
                data = c[0].recv(1024).decode()
                if data == 'exit':
                    for c in clients:
                        clients.remove(c)
                else:
                    f = open('log.csv', 'a')
                    f.write(data + '\n')
                    f.close()
                    print("\nData Masuk!")
            except timeout:
                pass

def menu():
    print("=============Pusat Data Storage Kasir==============")
    print("Listen on IP : %s" %host)
    print("Listen on Port : %d" %port)
    while True:
        try:
            n = len(clients)
            time.sleep(1)
            print("Total client yang tersambung: %d" %n, end='\r')
        except KeyboardInterrupt:
            break

if __name__ == '__main__':
    Connecting()
    a = True
    try:
        threadwrite = Thread(target=write, args=())
        threadlisten = Thread(target=listen, args=())
        threadwrite.start()
        threadlisten.start()
        menu()
    except KeyboardInterrupt:
        threadwrite.join()
        threadlisten.join()
        print("Keluar....")
        a = False
        s.close()
        exit()
