import socket
import sys
import time
import os

s = socket.socket()
n = 0
log = []

def clear():
    try:
        os.system('cls')
    except:
        os.system('clear')

def menu():
    while True:
        print("======================Client Kasir====================")         #fungsi untuk pilihan menu
        print("===Menu===============================================")
        print("1. Input Data Barang Keluar")
        print("2. Cek status")
        print("3. Keluar...")
    
        masukan = int(input("Pilihan: "))                                      #asking pilihan user

        if masukan == 1:
            barang = input("Nama Barang keluar: ")
            harga = int(input("Harga Barang: "))
            kuantitas = int(input("Jumlah: "))
            if kuantitas >= 1:
                total = harga * kuantitas
            else:
                pass
            diskon = int(input("Potongan Harga: "))            
            total -= diskon

            if total < 0:
                print("Gratis, pembeli tidak perlu membayar apapun")
                total = 0
            else:
                print("Yang harus dibayar adalah: %d" %total)
                uang = int(input("Bayar uang sebesar: "))
                kembalian = uang - total
                print("Kembalian sebesar: %d" %kembalian)

            hargastr = str(harga)
            kuantistr = str(kuantitas)
            totalstr = str(total)
            msg = barang + hargastr + kuantistr + totalstr
            s.send((client + ',' + barang + ',' + hargastr + ',' + kuantistr + ',' + totalstr).encode())                            #kirim data barang ke server
            log.append(msg)

            global n
            n += 1
            input()
            clear()
            
        elif masukan == 2:
            print("======================Status========================")
            print("Ip Server %s" %host)
            print("Port : %d" %port)
            print("Input data kali ini sebanyak %d kali" %n)
            clear()
            input()
        
        elif masukan == 3:
            print("Keluar...")
            time.sleep(1)
            clear()
            sys.exit()


def connecting():
    try:
        global host
        host = input('Masukkan IP Server: ')                                #fungsi untuk connecting socket ke sisi server
        global port
        port = int(input('Masukkan Port Server: '))
        s.connect((host,port))
        print("Berhasil tersambung sebagai %s" %client)
        time.sleep(1)
        clear()

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
            sys.exit()
        else:
            menu()
    except:
        sys.exit()
