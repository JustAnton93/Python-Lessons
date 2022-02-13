import string

a = input("Введите название техники которую хотите купить через пробел: ")
b = input('Введите по какой цене хотите ее купить в грн: ')
f = input('Сколько едениц товара Вам надо? ')
a = a.split( )
b = b.split( )
f = f.split( )
c = a, b, f
d = "Название товара: ", "Стоимость: ", "Количество: "
newDict = {d : c}
for key, value in newDict.items():
    values = zip(*value)
    val = list(values)
    print(f"{key}" + f"{val}")
