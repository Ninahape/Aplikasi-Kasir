import os
import sys

def pindah (label) :
    global nomor
    nomor = label
def clearscreen () :
    os.system ('cls')
def keluar():
    sys.exit()
def tanya () :
    
    if (tanya == 'y') :
        pindah (0)
        clearscreen ()
    elif (tanya == 't') :
        clearscreen ()
        keluar ()
    else:
        (keluar)

def cetak () :
    print ''
    print '\t===================='
    print '\t     PEMBAYARAN'
    print '\t===================='
    print ''
    print '\tNama Barang : Rp ',nm_brng
    print '\tHarga Barang : Rp ', harga
    print '\tJumlah Beli :  ', jmlbeli
    print '\tTotal Harga : Rp ', total
    print '\tPembayaran : Rp ', cast
    print '\tJumlah Kembalian : Rp', kmbl
    print '\tHutang : Rp ', hu
    print ''
nomor = 0
while True :
    if nomor == 0 :
        clearscreen ()
        print ''
        print '\t\t----------------------'
        print '\t\tAPLIKASI PROGRAM KASIR'
        print '\t\t----------------------'
        print ''
        print '\t\tPILIH MENU [1/2]'
        print '\t\t1. Pembayaran'
        print '\t\t2. Kalkulator'
        print ''
        a = (raw_input ('\t\tPilihan Anda? '))
        if a == '1' :
            print ''
            nm_brng = raw_input ('\tMasukkan Nama Barang : ')
            harga = int (input ('\tMasukkan Harga Barang : Rp '))
            jmlbeli = int (input('\tMasukkan Jumlah Beli : '))
            total = harga*jmlbeli
            print '\tTotal Harga', nm_brng, 'Adalah Rp.', total
            cast = int(input('\tMasukkan Pembayaran : Rp '))
            hu = total-cast
            kmbl = cast-total
            if(cast > total):
                print '\tJumlah Kembalian Anda adalah Rp ', kmbl
                print '\tRincian kembalian adalah'
                d = [100000, 50000, 20000, 10000, 5000, 1000, 500, 200, 100, 50]
                for x in range (0, 10) :
                    i = 0
                while kmbl >= d[x]:
                    kmbl = kmbl - d[x]
                    i = i+1
                if (i>0):
                    print '\tUang Rp. %d sebanyak %d lembar' %(d[x], i)
                    cetak ()
                    tanya ()
                else:
                    print '\tSelesai'
                    pinda
                    h (2)
                    clearscreen ()
                    cetak ()
                    tanya()
            if (cast < total) :
                print '\tAnda memiliki Hutang sebesar Rp ', hu
                clearscreen ()
                cetak ()
                tanya ()
            else:
                cetak ()
                tanya()
        elif a == '2' :
            print ''
            print '\t=========='
            print '\tKALKULATOR'
            print '\t=========='
            print ''
            print '\t1. (+)'
            print '\t2. (-)'
            print '\t3. (*)'
            print '\t4. (/)'
            print '\t5. (%)'
            print '\t6. (**)'
            print ''
            operasi = input ('\tPilih operasi : ')
            a = int(input('\ta : '))
            b = int(input('\tb : '))
            if operasi == 1 :
                print '\tHasil = ', a+b
                pindah (3)
                tanya ()
            elif operasi == 2 :
                print '\tHasil = ', a-b
                pindah (4)
                tanya ()
            elif operasi == 3 :
                print '\tHasil = ', a*b
                pindah (5)
                tanya ()
            elif operasi == 4:
                print '\tHasil = ', a/b
                pindah (6)
                tanya ()
            elif operasi == 5 :
                print '\tHasil = ', a%b
                pindah (7)
                tanya ()
            elif operasi == 6 :
                print '\tHasil = ', a**b
                pindah (8)
                tanya ()
            else:
                clearscreen ()
                keluar ()
        else :
            (keluar)
    else :
        keluar ()
            
