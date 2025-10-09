# Episode 4 - Perulangan 
# Pelajaran
nama = ["Alya", "Bima", "Citra", "Dedi"]
nilai = ["80", "90", "75", "85"]

for i in range(len(nama)): 
    print(nama[i], "mendapat nilai", nilai[i])

print("")

# Masalah dikembangkan
nama = ["Alya", "Bima", "Citra", "Dedi"]
nilai = [60, 90, 75, 85]
jumlah_lulus = 0

for i in range(len(nama)): 
    print(nama[i], "mendapat nilai", nilai[i])
    if nilai[i] >= 75: 
        print(nama[i], "LULUS")
        jumlah_lulus += 1
        print("")
    else: 
        print(nama[i], "TIDAK LULUS")
        print("")

print("Total peserta lulus : ", jumlah_lulus)

# Penambhaan terakhir 
nama = ["Alya", "Bima", "Citra", "Dedi"]
nilai = [60, 90, 75, 85]
jumlah_lulus = 0

nama.append("Eko")
nilai.append(70)

for i in range(len(nama)): 
    print(nama[i], "mendapat nilai", nilai[i])
    if nilai[i] >= 75: 
        print(nama[i], "LULUS")
        jumlah_lulus += 1
        print("")
    else: 
        print(nama[i], "TIDAK LULUS")
        print("")

print("Total peserta lulus : ", jumlah_lulus)