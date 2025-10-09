# Episode 5 - List
# Contoh Sederhana 
mata_kuliah = ["Matematika", "Fisika", "Kimia", "Informatika"]
nilai = [80, 75, 90, 85]

# Menampilkan semua mata kuliah 
for i in range(len(mata_kuliah)): 
    print(mata_kuliah[i], ":", nilai[i])

print("")

# Masalah
# Nilai tertinggi dan terendah 
max_nilai = max(nilai)
min_nilai = min(nilai) 
print("Nilai tertinggi :", max_nilai)
print("Nilai terendah : ", min_nilai)
print("")

# Menambahkan mata kuliah baru 
mata_kuliah.append("Biologi")
nilai.append(88)
print("Setelah ditambah :")
print(mata_kuliah)
print(nilai)

# Menghapus mata kuliah 
del mata_kuliah[1]
del nilai[1]
print("Setelah dihapus :")
print(mata_kuliah)
print(nilai)