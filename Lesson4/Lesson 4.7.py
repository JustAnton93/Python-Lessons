from math import factorial


def my_func():
    fact = range(1, 21)
    for el in fact:
        yield factorial(el)


gen = my_func()
x = 0
for i in gen:
    if x < 5:
        print(i)
        x += 1
    else:
        break
