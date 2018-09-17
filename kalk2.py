print("Kalkulātors 0.1")

x = input("Skaitli X")
y = input("Skaitli Y")

rez = int(x) + int(y)

print("Summa", x, "+", y, "=", rez)

# == izmanto lai salīdzinātu, = lai vienādotu
if rez > 50:
    print("Rezultāts ir lielāks par 50")
elif rez == 50:
    print("Rezultāts ir vienāds ar 50")
else:
    print("Rezultāts ir mazāks par 50")
