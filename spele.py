from random import randint

secret = randint(0, 100)
intMIN = 0
intMAX = 100
minejums = int(input("Lūdzu ievadiet skaitli no 1 - 100: "))
rezultats = str("M")
MinejumuSkaits = 0



while rezultats != "p":
    MinejumuSkaits = MinejumuSkaits + 1
    print(secret)
    rezultats = str(input("Ievadiet Lielāks - L; Mazāks - M vai Pareizi - P: "))
    rezultats = rezultats.lower()
    if rezultats == "l":
        intMIN = secret
        secret = round((intMAX+intMIN)/2)
    elif rezultats == "m":
        intMAX = secret
        secret = round((intMAX+intMIN)/2)
    else:
        secret = secret
print("Minējumu skaits: ", MinejumuSkaits)
print("Pareizā atbilde: ", secret)

