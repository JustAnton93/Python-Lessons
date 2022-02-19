def my_func(first_number, second_number, third_number):
    return first_number + second_number, second_number + third_number, first_number + third_number
total = my_func(
    first_number = int(input('Введите первое число: ')),
    second_number = int(input('Введите второе число: ')),
    third_number = int(input('Введите третье число: '))
)
print(max(total))
