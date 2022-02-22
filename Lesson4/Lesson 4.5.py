from functools import reduce


def func_numbers(first_el, second_el):
    return first_el * second_el


list_for_reduce = [el for el in range(100, 1001) if el % 2 == 0]
print(f"Результат произведения чисел: {reduce(func_numbers, list_for_reduce)}")
