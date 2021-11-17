from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread
import time
from sys import exit

clients = set()

host = '192.168.56.103'
port = 4200
s = socket(AF_INET, SOCK_STREAM)

def Connecting():
    s.bind((host, port))
    print("Koneksi berhasil dibuka")
    s.listen()

def listen():
    c, addr = s.accept()
    clients.add(c)
    while True:

        try:
            data = c.recv(1024).decode()
            if data == 'exit':
                clients.remove[c]
            f = open('log.csv', 'a')
            f.write(data + '\n')
            f.close()
            i = 0

            for i in range(4):
                print("\nData Masuk!", end='\r')
                time.sleep(0.5)
                print('', end='\r')
                i += 1

        except:
            print("Listening...", end='\r')
            listen()

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
    try:
        threadrecv = Thread(target=listen, args=())
        threadrecv.start()
        menu()
    except KeyboardInterrupt:
        threadrecv.join()
        print("Keluar....")
        exit()
