def my_sum ():
    total = 0
    ex = False
    while ex == False:
        number = input('Введите числа либо N для выхода ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'n' or number[el] == 'N':
                ex = True
                break
            else:
                res = res + int(number[el])
        total = total + res
        print(f'Текущее значение:  {total}')
    print(f'Итоговое значение: {total}')
my_sum()
