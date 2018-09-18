print("KM uz jūdzēm")

while True:
    print(" Lūdzu ievadiet km! Ievadiet tikai ciparus")
    km = input("Kilometrs: ")
    # veic darbību
    try:
        km = float(km.replace(",", "."))
        miles = km * 0.621371
        print("{} kilometri ir {} jūdzes".format(km, miles))
    # ja nevar veikt darbību parāda kļūdu
    except Exception as e:
        print("Lūdzu ievadiet tikai ciparus")
    choice = input("Vai vēlaties atkārtot darbību (j/n)")
    if choice.lower() != "j" and choice.lower() != "Jā":
        break
