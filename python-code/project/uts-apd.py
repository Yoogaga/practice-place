import os
import time

# Episode 1
# Tidak Ada

# Episode 2 - Variabel
# Pelajaran dari Raka
apel = 5
pisang = 3
total_buah = apel + pisang 
print("Jumlah buah = ", total_buah)

# Belajar Input 
semangka = int(input("Masukkan Jumlah Semangka : "))
pepaya = int(input("Masukkan Jumlah Pepaya : "))
jumlah = semangka + pepaya
print(jumlah)

# Pengembangan Masalah 
beras = 2 * 10000
telur = 6 * 1500
sayur = 3 * 5000
susu = 2 * 12000

total_belanja = beras + telur + sayur + susu
print("Total Belanja = ", total_belanja)

# Episode 3 - Kondisional
# Pelajaran 1
telur = False
tepung = False
cokelat = True 

if telur and tepung:
    print("Kamu bisa Bikin Pancake!")
elif tepung and cokelat: 
    print("Kamu bisa bikin kue cokelat")
else: 
    print("Bahan kurang, buat snack lain aja")

# Mssslsh
telur = False
tepung = False
cokelat = True
gula = True
mentega = True 

if telur and tepung and gula: 
    print("Kamu bisa bikin Pancake Manis!")
elif tepung and cokelat and gula: 
    print("Kamu bisa bikin brownies")
elif telur and mentega: 
    print("Kamu bisa bikin omelet")
else: 
    print("Bahan kurang, beli snack instan aja!")

# Episode 4 - Perulangan
nama = ["Alya", "Bima", "Citra", "Dedi"]
nilai = ["80", "90", "75", "85"]

for i in range(len(nama)): 
    print(nama[i], "mendapat nilai", nilai[i])

# Episode 5 - List


# Episode 6 - Tuple


# Episode 7 - Set


# Episode 8 - Gabungan Masalah