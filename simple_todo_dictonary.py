# append
print ("Append ļauj pievienot papildus darbus")

todo_list = {}
numur = 0

while True:
    task = input("Ievadiet darbu sarakstu: ")
    status = input("Vai darbs ir izdarīt j/n")
    if status.lower() == "j":
        todo_list[task] = True
    else:
        todo_list[task] = False
    new = input("Vai vēlataties papildus darbus pievienot j/n ")
    if new == "n":

        break
dokuments = open('todo_list.txt', 'w+')
print ("Visi pievienotie darbi: %s" %todo_list)
for task in todo_list:
    numur = numur + 1
    if todo_list[task]:
        status = 'Ir'
    else:
        status = 'Nav'
    print('{}. {}: {}'.format(numur, task, status))
    dokuments.write('{}. {}: {}\n'.format(numur, task, status))

print ("Beigas")
dokuments.close()