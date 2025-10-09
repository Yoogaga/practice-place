# Episode 6 - Tuple
# Pelajaran 
teman = ("Alya", "Bima", "Citra", "Dedi")
print(teman)

# Masalah 
peserta = ("Alya", "Bima", "Citra", "Dedi")
hadir = [True, False, True, True]

for i in range(len(peserta)): 
    status = "Hadir" if hadir[i] else "Tidak Hadir"
    print(peserta[i], "-", status)