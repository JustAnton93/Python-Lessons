my_list = [20, 30, 40, 50]
*el_1, el_2, el_3 = my_list
print(el_1, el_2, el_3)
el_1, *el_2, el_3 = my_list
print(el_1, el_2, el_3)
el_1, el_2, *el_3 = my_list
print(el_1, el_2, el_3)
el_1, el_2, el_3, *el_4 = my_list
print(el_1, el_2, el_3, el_4)
el_1, el_2, el_3, el_4, *el_5 = my_list
print(el_1, el_2, el_3, el_4, el_5)