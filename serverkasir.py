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

def handle(a):
    while True:
        try:
            for a in clients:
                a[0].send('tes'.encode())
        except timeout or TimeoutError:
            clients.remove[a]
            print("1 Client telah terputus")

def listen():
    while True:
        c, addr = s.accept()
        clients.append(c)
        data = c.recv(1024).decode()
        if data == 'exit':
            for c in clients:
                clients.remove(c)
                print("1 Client telah terputus!")
        f = open('log.csv', 'a')
        f.write(data + '\n')
        f.close()
        print("\nData Masuk!")
        time.sleep(1)

        global threadlisten
        threadlisten = Thread(target=handle, args=(c,))
        threadlisten.start()

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
        threadlisten.join()
        print("Keluar....")
        exit()
