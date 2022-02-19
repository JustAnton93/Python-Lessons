def int_func(user_words, second_word):
    print(user_words)
    for words in second_word:
        words = str(words.capitalize())
        print(words)
int_func(user_words=input('Введите слово с маленькой буквы: ').capitalize(),
         second_word = input("Введите несколько слов через пробел: ").split()
         )
