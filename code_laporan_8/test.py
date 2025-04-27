


# #STRING bersifat imutable tidak bisa di ubah 
# # a="selamat paskah hhhh"
# # a[5]="h"#tidak bisa diotak atik/imutable ,agar bisa di ubah harus disimpan dengan variable yang berbeda
# #contoh akses dtring
# nama_buah="banana"
# print(nama_buah)
# print(nama_buah[-2])

# kalimat ="hai nak"
# print(kalimat)

# nama = "anggi comel"
# print(nama[0])  # Output: 'a' (menghitung indeks dimulai dari 0)
# print(nama[-2]) # Output: 'e' (menghitung indeks negatif dari akhir)
# print(nama[::2]) # Output: agicml (mengambil setiap karakter kedua mulai dari indeks 0)
# print(nama[4:6]) # Output: i ()


# #gabungkan string
# a='ukdw'
# b='yogya'
# print(a+b)

# #berdasrkan code ASCII
# a='A'
# b='a'
# print(a<b) #KNP hasil true karena huruf ascii A = 56 lebih besar dari a kecil

# a='Anton'
# b='anton'
# print(a>b)

# #Operator dan Metode String OPERATOR in

# #FUNGSI LEN untuk mengatahui panjang kata atau hruf ,spasi juga ikut di huting len berguan untuk tau huruf nya berapa karena inputan nya dinamis


# TRAVERSING mengunjung setiap huruf untuk di ubah serta bisa memanipulasi perhruf
# a="selmat pagi"
# b="selamat malam"

# print(b in a)
# for i in a: # Output: False
#     if i == 'a':
#         i='4'
#     elif i == 'e':
#         i='3'
#     elif i == 's':
#         i='2'
#     print(i,end='')
    # Output: 23lm4t p4giTrue
    
#SLICE menampilkan bagian dari string
# a="selmat pagi paskha"
# b="selamat malam"
# print(a[0:5])#output: selma
# print(a[1:]) #output: elmat pagi paskha
# print(a[::-1])# untuk balik kalimat,output:ahksap igap tamles

# # #METHOD CAPITALIZE dll
# # a="selmat pagi paskha"
# # b="selamat malam"
# # # print(b.capitalize())
# # print(b.islower())

# # #OPERATOR KALI
# # a="a "
# # print(a*4)

#PARSING  string jadi menulusuri string untuk mendapat sesuatu
# kalimat="saya berulang tahun 20-03-2005 dan jimin ulang tahun 18-08-2005 kami pacaran"
# hasil_spilit = kalimat.split(" ")
# print(hasil_spilit)

# for i in hasil_spilit: #code mencari tanggal dd/mm/yyyy
#     if i[0].isdigit():#menegcek apakah hruf depan nya angka atau bukan 
#         print(i)
        
#PENGANTAR  REGEX (pola regular expersion)berbentuk kalimat atau kata  pola yg bisa kita cari dalam sebuah string (sanagt berguna kalau teks nya panjang)
    #misal mencari nama email pada file txt
import re
handle=open('hii.txt')
jumlah = 0
for line in handle:
 line=line.rstrip()
 if re.search('From:', line): #mencari kalimat yang ada kata from atau bisa mencari("d{1,2}")
  jumlah += 1
  print(line)
print("jumlah: " +str(jumlah))


# # #CONTOH SOAL PRATIKUM 




# #OPERATOR penggabungan
# a = "anggrayni"
# b = "layuk"
# nama_lengkap = a +" "+ b  # "anggrayni layuk"

# #Operator in (Membership Operator)
# teks = "Anggi comel bgtt"
# # Cek apakah "Python" ada dalam teks
# print("Anggi" in teks)    # Output: True
# print("AnggY" in teks)    # Output: FALSE karena kata tidak ada
# # Cek apakah "Java" tidak ada dalam teks
# print("Cute" not in teks)  # Output: True


# kalimat = "Hey, patrick!"
# print(len(kalimat)) # Output: 13

# # Menggunakan dengan list
# no = [1, 2, 3, 4, 5]
# print(len(no)) # Output: 5
