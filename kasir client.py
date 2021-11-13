import socket
from socket import timeout
import time
from threading import Thread

s = socket.socket()

def menu():
    print("======================Client Kasir====================")         #fungsi untuk pilihan menu
    print("===Menu===============================================")
    print("1. Input Data Barang Keluar")
    print("2. Delete Data Barang Keluar")
    print("3. Keluar...")

def connecting():
    try:
        host = input('Masukkan IP Server: ')                                #fungsi untuk connecting socket ke sisi server
        port = input ('Masukkan Port Server: ')
        s.connect((host,port))
    
    except:
        print("-> Error tidak dapat menyambungkan, mohon dicek kembali host dan port tujuan atau sisi server belum dibuka")
        time.sleep(1)
        return "error"

if __name__ == '__main__':
    client = input('Masuk sebagai: ')
