a: list = input('Vvedite raznye dannye: ')
a = a.split()
a[:-1:2], a[1::2] = a[1::2], a[:-1:2]
print(a)


