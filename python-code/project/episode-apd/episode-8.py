# Episode 8 - Perkembangan Masalah
# Masalah 

# Data awal peserta (Ada duplikat nama)
peserta_awal = ["Alya", "Bima", "Citra", "Bima", "Dedi", "Fajar"]

# Peserta tidak aktif 
tidak_aktif = ("Fajar", "Dedi")

# Gunakan set untuk peserta unik 
peserta = set(peserta_awal)

# Hapus peserta tidak aktif
peserta = peserta.difference(tidak_aktif)

# Modul dan nilai (tuple : (modul, nilai))
modul_nilai = {
    "Alya": [("Python", 80), ("Algoritma", 90)],
    "Bima": [("Python", 70), ("Algoritma", 60)], 
    "Citra": [("Python", 95), ("Algoritma", 85)] 
}

# Menampilkan daftar peserta dan nilai 
for i in peserta: 
    print("Peserta : ", i)
    for modul, nilai in modul_nilai[i]: 
        print("-", modul, ":", nilai)
        if nilai >= 75: 
            print(" Status : Lulus")
            print("")
        else: 
            print(" Status : Tidak Lulus")
            print("")

# Hitung total peserta lulus tiap modul 
lulus_modul = {}
for i in peserta: 
    for modul, nilai in modul_nilai[i]: 
        if modul not in lulus_modul: 
            lulus_modul[modul] = 0
        if nilai >= 75: 
            lulus_modul[modul] +=1

print("\nTotal peserta lulus tiap modul:")
for modul, total in lulus_modul.items(): 
    print(modul, ":", total)