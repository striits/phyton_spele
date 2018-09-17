print("Kalkulātors")

darbiba = input("Ievadiet vēlamo darbību(+ - * /): ")
a = int(input("Ievadiet pirmo skaitli: "))
b = int(input("Ievadiet otro skaitli: "))

if darbiba == "+":
    rez = a + b
elif darbiba == "-":
    rez = a - b
elif darbiba == "*":
    rez = a * b
elif darbiba == "/":
    rez = a / b
else:
    print("Šādas darbības nav")

print("Rezultāts {} {} {} = {}".format(a, darbiba, b, rez))