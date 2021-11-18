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
    c, addr = s.accept()
    clients.append(c)
    global a
    while a == True:
        data = c.recv(1024).decode()
        while True:
            if data == 'exit':
                for c in clients:
                    clients.remove(c)
                    print("\n1 Client telah terputus!")
                    break
            elif data is not 'exit':
                f = open('log.csv', 'a')
                f.write(data + '\n')
                f.close()
                print("\nData Masuk!")
                time.sleep(1)
                break

def menu():
    print("=============Pusat Data Storage Kasir==============")
    print("Listen on IP : %s" %host)
    print("Listen on Port : %d" %port)
    while True:
        try:
            n = len(clients)
            time.sleep(1)
            print("Total client yang tersambung: %d" %n, end='\r')
            print(clients, end='\r')
        except KeyboardInterrupt:
            break

if __name__ == '__main__':
    Connecting()
    a = True
    try:
        threadrecv = Thread(target=listen, args=())
        threadrecv.start()
        menu()
    except KeyboardInterrupt:
        threadrecv.join()
        print("Keluar....")
        exit()
