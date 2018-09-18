# append
print ("Append ļauj pievienot papildus darbus")
numur = 0
todo_list = []

while True:
    task = input("Ievadiet darbu sarakstu: ")
    todo_list.append(task)
    new = input("Vai pievienot papildus darbus (j/n) (Jā/Nē)? ")
    if new.lower() == "n" or new.lower() == "nē":
        break

print ("Visi pievienotie darbi: %s" %todo_list)
for task in todo_list:
    numur = numur + 1
    print('{}. {}'.format(numur,task))
print ("Beigas")