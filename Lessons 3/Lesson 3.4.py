def my_func(x, y):
    return x ** y
total = my_func(
     x = abs(int(input('Введите первое число: '))),
     y = abs(int(input('Введите второе число: '))) * -1
)
print(total)
