def calcula():
    try:
        first_number = int(input('Введите первое число: '))
        second_number = int(input('Введите второе число: '))
        calc = first_number / second_number
        return calc
    except ZeroDivisionError:
        return
calc = calcula()
print(calc)
