from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread
import time
from sys import exit

client = []

host = '192.168.52.205'
port = 4200
s = socket(AF_INET, SOCK_STREAM)

def Connecting():
    s.bind((host, port))
    print("Koneksi berhasil dibuka")
    s.listen()

def listen():
    while True:
        c, addr = s.accept()
        print("Client baru tersambung!", addr)
        client.append(c)

        try:
            data = c.recv(1024).decode()
            f = open('log.csv', 'a')
            f.write(data + '\n')
            f.close()
            i = 0

            for i in range(4):
                print("Data Masuk!", end='\r')
                time.sleep(0.5)
                print('', end='\r')
                i += 1
        except:
            print("Listening...", end='')

def menu():
    print("=============Pusat Data Storage Kasir==============")
    print("Listen on IP : %s" %host)
    print("Listen on Port : %d" %port)
    while True:
        try:
            n = len(client)
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
