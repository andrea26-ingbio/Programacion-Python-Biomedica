def linearSearch(item,my_list):
    found=False
    position=0
    while position<len(my_list)and not found:
        if my_list[position]==item:
            found=True
        position=position+1
    return found

while 1:
    bolsa=['libro','pc','lapiz','pluma','laptop']

    item=input('¿Que quieres buscar: ')

    itemfound=linearSearch(item,bolsa)

    if itemfound:
        print('Si existe')
    else:
        print('No existe')
