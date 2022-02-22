numbers_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_number_list = [el for el in numbers_list if el > numbers_list[numbers_list.index(el) - 1]]
print(new_number_list)
