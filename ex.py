newDict =  {"name":["dgon","mon"],"age":[9,0],}

for keys, values in newDict.items():
    values = newDict.values()
    keys = newDict.keys()
    for keys, values in enumerate(newDict):
        print(keys, values)
    print(f"{keys} = {values}")

a = input("Введите название техники которую хотите купить через запятую: ")
b = input('Введите по какой цене хотите ее купить в грн: ')
f = input('Сколько едениц товара Вам надо? ')

el_1, el_2, *el_3 = a
print(el_1, el_2, el_3)
el_1, el_2, el_3, *el_4 = a
print(el_1, el_2, el_3, el_4)
el_1, el_2, el_3, el_4, *el_5 = a
print(el_1, el_2, el_3, el_4, el_5)