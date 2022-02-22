from itertools import count
for x in count(3, 1):
    if x > 10:
        break
    print(x)

"""from itertools import cycle
my_list = [12, 44, 4, 10, 78, 123]
c = 0
for el in cycle(my_list):
    if c > 10:
        break
    print(el)
    c += 1
"""
