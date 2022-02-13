words = input('Введите слова через пробел: ')
words = words.split()
for ind, el in enumerate(words):
    if len(str(el)) < 11:
        print(ind, el[0:9])
    else:
        print(ind, el[0:10])