# Episode 3 - Kondisional
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