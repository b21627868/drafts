import random
sayi = int(input("Lütfen sayı giriniz:"))
number = random.randint(1,3)
#print(number)



while number != sayi:
    if number < sayi:
        print("decrease your sayi")
        sayi = int(input("Lütfen sayı giriniz:"))
    elif number > sayi:
        print("increase your sayi")
        sayi = int(input("Lütfen sayı giriniz:"))

if number == sayi:
    print("You have just found the correct number")
