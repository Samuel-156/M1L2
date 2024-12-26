import random

elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
lenght = int(input("Masukkan panjang kata sandi:"))
password = ""
for i in range(lenght):
    password += random.choice(elements)

print(password)