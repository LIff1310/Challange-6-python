print("LATIHAN 8")
num = int(input("Masukan Angka ganjil lebih dari 20 : "))

while num % 2 == 0 or num < 20:
    num = int(input("Masukan Angka ganjil lebih dari 20 : "))
else:
    print("Benar")

print("-"*15)

num = int(input("Masukan Angka 10-15 atau 20-25 atau 35-40 : "))

while (num < 10 or num > 15) and (num < 20 or num > 25) and (num < 35 or num > 40):
    num = int(input("Masukan Angka 10-15 atau 20-25 atau 35-40 : "))

else:
    print("Benar")
