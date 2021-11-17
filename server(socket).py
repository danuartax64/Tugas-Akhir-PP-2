from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread
import time
from sys import exit

clients = []
global n
n = len(clients)

host = '192.168.56.103'
port = 4200
s = socket(AF_INET, SOCK_STREAM)

def Connecting():
    s.bind((host, port))
    print("Koneksi berhasil dibuka")
    s.listen()

def status(c):
    while True:
        try:
            for c in clients:
                s.send(('a').encode())
        except:
            clients.remove(c)
            global n
            n = len(clients)
            s.close()
            break

def listen():
    while True:
        global c
        c = s.accept()
        clients.append(c)
        threadstatus = Thread(target=status, args=(c,))
        threadstatus.start()

        try:
            data = c.recv(1024).decode()
            f = open('log.csv', 'a')
            f.write(data + '\n')
            f.close()
            i = 0

            for i in range(4):
                print("\nData Masuk!")
                time.sleep(0.5)
                print('\n     ', end='\r')
                i += 1
        except ConnectionResetError:
            print("Listening...", end='\r')
            threadstatus.join()

def menu():
    print("=============Pusat Data Storage Kasir==============")
    print("Listen on IP : %s" %host)
    print("Listen on Port : %d" %port)
    while True:
        try:
            time.sleep(1)
            print("Total client yang tersambung: %d" %n, end='\r')
        except KeyboardInterrupt:
            break

if __name__ == '__main__':
    Connecting()
    try:
        threadrecv = Thread(target=listen, args=())
        threadrecv.start()
        menu()
    except KeyboardInterrupt:
        threadrecv.join()
        print("Keluar....")
        exit()
