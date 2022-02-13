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







