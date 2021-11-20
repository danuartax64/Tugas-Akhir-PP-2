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
    global clients
    while a == True:
        for c in clients:
            try:
                 c[0].settimeout(1)
                 data = c[0].recv(1024).decode()
                 if len(data) > 0:
                     while True:
                        if data == 'exit':
                            break
                        elif data == 'exitexit':
                            break
                        else:
                            f = open('log.csv', 'a')
                            f.write(data + '\n')
                            f.close()
                            print("Data Masuk")
                            time.sleep(1)
                            print ("\033[A                             \033[A")
                            break
            except timeout:
                pass

def menu():
    print("=============Pusat Data Storage Kasir==============")
    print("Listen on IP : %s" %host)
    print("Listen on Port : %d" %port)
    print("Ctrl+C 2x untuk keluar")
    while a == True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            break

if __name__ == '__main__':
    try:
        f = open('log.csv', 'x')
        f.write('User,Barang,Harga,Kuantitas,Total,\n')
        f.close()
        print("File log telah dibuat")
    except:
        print("File log telah dibuat")
        
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
