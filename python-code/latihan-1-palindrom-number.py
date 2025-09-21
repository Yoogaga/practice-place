ulang = "y"
while ulang == "y": 
    print("-" * 50)
    print("Program Menentukan Bilangan Palindrom".center(45))
    print("-" * 50)

    palindrom = int(input("Masukkan bilangan : "))
    print("-" * 50)

    testbagi = palindrom
    reverse = 0

    while testbagi > 0: 
        a = testbagi % 10
        reverse = reverse * 10 + a
        testbagi //= 10 

    if reverse == palindrom: 
        print(f"{palindrom} {"Merupakan Bilangan Palindrom"}".center(45))
        print("-" * 50)

    else: 
        print(f"{str(palindrom)} {'Bukan Bilangan Palindrom'}".center(45))
        print("-" * 50)

    ulang = str(input("Apakah Program ingin diulang? (y/n) "))
    print("-" * 50)

print("Program Selesai Berjalan!".center(45))
print("-" * 50)