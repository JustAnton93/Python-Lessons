b = [9, "a", {21}, (10 > 5), ([]), {"b":"a"}]
index = []
for index in b:
    print(type(index))

a: list = input('Vvedite raznye dannye: ')
a = a.split()
a[:-1:2], a[1::2] = a[1::2], a[:-1:2]
print(a)

a = int(input("Введите номер месяца: "))
aList = ['зима', 'весна', 'лето', 'осень']
aDict = {1:'зима',2 : 'весна', 3 : 'лето', 4 : 'осень'}
if a == 12 or a == 1 or a == 2:
    print(aList[0])
    print(aDict.get(1))
elif a == 3 or a == 4 or a == 5:
    print(aList[1])
    print(aDict.get(2))
elif a == 6 or a == 7 or a == 8:
    print(aList[2])
    print(aDict.get(3))
elif a == 9 or a == 10 or a == 11:
    print(aList[3])
    print(aDict.get(4))
else:
    print(' Нет такого месяца ')

words = input('Введите слова через пробел: ')
words = words.split()
for ind, el in enumerate(words):
    if len(str(el)) < 11:
        print(ind, el[0:9])
    else:
        print(ind, el[0:10])

numbers = [7, 5, 3, 3, 2]
print(f"Рейтинг - {numbers}")
userNumber = int(input("Введите число (21 - выход) "))
while userNumber != 21:
    for el in range(len(numbers)):
        if numbers[el] == userNumber:
            numbers.insert(el + 1, userNumber)
            break
        elif numbers[0] < userNumber:
            numbers.insert(0, userNumber)
        elif numbers[-1] > userNumber:
            numbers.append(userNumber)
        elif numbers[el] > userNumber and numbers[el + 1] < userNumber:
            numbers.insert(el + 1, userNumber)
    print(f"текущий список - {numbers}")
    userNumber = int(input("Введите число "))

a = input("Введите название техники которую хотите купить через пробел: ")
b = input('Введите по какой цене хотите ее купить в грн: ')
f = input('Сколько едениц товара Вам надо? ')
a = a.split( )
b = b.split( )
f = f.split( )
c = a, b, f
d = "Название товара: ", "Стоимость: ", "Количество(шт): "
newDict = {d : c}
for key, value in newDict.items():
    values = zip(*value)
    val = list(values)
    for d in  val:
        d = key + d
        print(d)
