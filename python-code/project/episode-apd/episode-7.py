# Episode 7 - Set
# Belajar
teman = {"Alya", "Bima", "Citra", "Bima", "Dedi"}
print(teman)
print("")

# Masalah 
peserta = {"Alya", "Bima", "Citra", "Dedi"}

# Menambahkan peserta baru
peserta.add("Eko")
peserta.add("Alya")

print("Daftar peserta : ", peserta)

# Set peserta hadir 
hadir = {"Alya", "Citra", "Eko"}

# Peserta yang hadir 
print("Hadir : ", peserta.intersection(hadir))

# Peserta yang belum hadir
print("Belum hadir : ", peserta.difference(hadir))