'''
PROGRAM PENGUKUR SUHU
        BY
    BOY KUCAYY 
'''



print(44*"=")
print("\t\tPROGRAM SUHU")
print(44*"=")
a = "Celcius"
b = "Reamur"
c = "Fahrenheit"
d = "Kelvin"
print("""Pilih Satuan Asal Suhu :
a. Celcius
b. Reamur
c. Fahrenheit
d. Kelvin""")
suhu = input("Masukan Satuan Suhu :")
print(44*"=")
if suhu == "a":
    print("Satuan yang anda pilih adalah", a)
    print(44*"=")
    subsuhu = float(input("""Anda ingin menghitung kesatuan mana?
    1. Reamur
    2. Fahrenheit
    3. Kelvin
    ========================================
    Jawaban Anda :"""))
    if subsuhu == 1:
        print(44*"=")
        print(a,">",b)
        print(20*"=")
        C = float(input("Berapa Celcius : "))
        R = 4/5*C
        print(C,"C = ",R,"R")

    elif subsuhu == 2:
        print(44*"=")
        print(a,">",c)
        C = float(input("Berapa Celcius : "))
        F = 9/5*C+32
        print(C,"C = ",F,"F")

    elif subsuhu == 3:
        print(44*"=")
        print(a,">",d)
        C = float(input("Berapa Celcius : "))
        K = C+273
        print(C,"C = ",K,"K")

    else:
        print(44*"=")
        print("Pilihan anda Tidak Ada")   

elif suhu == "b":
    print("Satuan yang anda pilih adalah", b)
    print(44*"=")
    subsuhu = float(input("""Anda ingin menghitung kesatuan mana?
    1. Celcius
    2. Fahrenheit
    3. Kelvin
    ========================================
    Jawaban Anda :"""))
    if subsuhu == 1:
        print(44*"=")
        print(b,">",a)
        print(20*"=")
        R = float(input("Berapa Reamur : "))
        C = 5/4*R
        print(R,"R = ",C,"C")

    elif subsuhu == 2:
        print(44*"=")
        print(b,">",c)
        R = float(input("Berapa Reamur : "))
        F = 9/4*R+32
        print(R,"R = ",F,"F")

    elif subsuhu == 3:
        print(44*"=")
        print(b,">",d)
        R = float(input("Berapa Reamur : "))
        K = 5/4*R+273
        print(R,"R = ",K,"K")

    else:
        print(44*"=")
        print("Pilihan anda Tidak Ada")   
    
elif suhu == "c":
    print("Satuan yang anda pilih adalah", c)
    print(44*"=")
    subsuhu = float(input("""Anda ingin menghitung kesatuan mana?
    1. Celcius
    2. Reamur
    3. Kelvin
    ========================================
    Jawaban Anda :"""))
    if subsuhu == 1:
        print(44*"=")
        print(c,">",a)
        print(20*"=")
        F = float(input("Berapa Fahrenheit : "))
        C = 5/9*(F-32)
        print(F,"F = ",C,"C")

    elif subsuhu == 2:
        print(44*"=")
        print(c,">",b)
        F = float(input("Berapa Fahrenheit : "))
        R = 4/9*(F-32)
        print(F,"F = ",R,"R")

    elif subsuhu == 3:
        print(44*"=")
        print(c,">",d)
        F = float(input("Berapa Fahrenheit : "))
        K = 5/9*(F-32)+273
        print(F,"F = ",K,"K")

    else:
        print(44*"=")
        print("Pilihan anda Tidak Ada")   
       
elif suhu == "d":
    print("Satuan yang anda pilih adalah",d)
    print(44*"=")
    subsuhu = float(input("""Anda ingin menghitung kesatuan mana?
    1. Celcius
    2. Reamur
    3. Fahrenheit
    ========================================
    Jawaban Anda :"""))
    if subsuhu == 1:
        print(44*"=")
        print(d,">",a)
        print(20*"=")
        K = float(input("Berapa Kelvin : "))
        C = K-273
        print(K,"K = ",C,"C")

    elif subsuhu == 2:
        print(44*"=")
        print(d,">",b)
        K = float(input("Berapa Kelvin : "))
        R = 4/5*(K-273)
        print(K,"K = ",R,"R")

    elif subsuhu == 3:
        print(44*"=")
        print(d,">",d)
        K = float(input("Berapa Kelvin : "))
        F = 5/9*(K-273)+32
        print(K,"K = ",F,"F")

    else:
        print(44*"=")
        print("Pilihan anda Tidak Ada")   
    
else:
    print("Pilihan anda Tidak Ada")


print(44*"=")
print("Terima Kasih Sudah Mencoba")
print(44*"=")

