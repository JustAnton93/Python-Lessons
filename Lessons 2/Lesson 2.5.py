numbers = [7, 5, 3, 3, 2]
print(f"Рейтинг - {numbers}")
userNumber = int(input("Введите число (21 - выход) "))
while userNumber != 21:
    for el in range(len(numbers)):
        if numbers[el] == userNumber:
            numbers.insert(el + 1, userNumber)
            break
        elif numbers[0] < userNumber:
            numbers.insert(0, userNumber)
        elif numbers[-1] > userNumber:
            numbers.append(userNumber)
        elif numbers[el] > userNumber and numbers[el + 1] < userNumber:
            numbers.insert(el + 1, userNumber)
    print(f"текущий список - {numbers}")
    userNumber = int(input("Введите число "))

