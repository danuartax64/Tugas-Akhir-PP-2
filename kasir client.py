import socket
from socket import timeout
import time
from threading import Thread

s = socket.socket()

def menu():
    while True:
        print("======================Client Kasir====================")         #fungsi untuk pilihan menu
        print("===Menu===============================================")
        print("1. Input Data Barang Keluar")
        print("2. Delete Data Barang Keluar")
        print("3. Keluar...")
    
        masukan = int(input("Pilihan: "))                                      #asking pilihan user

        if masukan == 1:
            barang = input("Nama Barang keluar: ")
            harga = int(input("Harga Barang: "))
            kuantitas = int(input("Jumlah: "))
            if kuantitas > 1:
                total = harga * kuantitas
            else:
                pass
            hargastr = str(harga)
            kuantistr = str(kuantitas)
            totalstr = str(total)
            msg = barang + hargastr + kuantistr + totalstr
            s.send((client + ' : ' + msg).encode())                            #kirim data barang ke server

def connecting():
    try:
        host = input('Masukkan IP Server: ')                                #fungsi untuk connecting socket ke sisi server
        port = int(input('Masukkan Port Server: '))
        s.connect((host,port))
    
    except:
        print("-> Error tidak dapat menyambungkan, mohon dicek kembali host dan port tujuan atau sisi server belum dibuka")
        time.sleep(1)
        return "error"
if __name__ == '__main__':

    client = input('Masuk sebagai: ')
    try:
        connecting()
        if connecting == 'error':
            print("Ada yang salah dengan host / port server")
            print("Closing App...")
        else:
            menu()
    except:
        pass
