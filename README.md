Python-Lessons
lesson 1
userName = input('Введите Ваше имя: ')
age = int(input('Введите сколько Ваш возраст: '))
married = input('Введите Ваше семейное положение: ')
childrens = int(input('Сколько у Вас детей? '))
print('Меня зовут' , userName ,'мне', age,'года' ,'я', married ,'и воспитываю',childrens, 'детей')

lesson 2
userTime = int(input('Введите время в секундах: '))
timeMinut = userTime/60
timeHours = timeMinut/60
print(f'{timeHours}:{timeMinut}:{userTime}')

lesson 3
n = int(input('Введите любое целое число: '))
nn = n*11
nnn = n*111
amount = n + nn + nnn
print(f'{n}+{nn}+{nnn}={amount}')

lesson 4
userNumber = int(input('Введите целое положительное число: '))
r = -1
while userNumber > 10:
    d = userNumber % 10
    userNumber//=10
    if d > r:
        r = d
print(r)

lesson 5
proceeds = int(input('Введите значение выручки: '))
cost = int(input('Введите значение издержек: '))
workers = int(input('Введите количество сотрудников фирмы: '))
if proceeds > cost:
    amount = proceeds - cost
    print('Фирма отработала с прибылью, её рентабельность составила: ',amount,'грн')
    allGet = amount/workers
    print('Каждый сотрудник получил: ', allGet,'грн')
else:
    print('Ваша фирма отработала с убытком, она нерентабельна. ')


lesson 6
distanceFirstDay  = int(input('Введите сколько спортсмен пробежал в первый день км: '))
distanceLastDay = int(input('Сколько максимум хочет пробежать спортсмен км? '))
firstDay = 1
print(f'В {firstDay} - й день он пробежал:  {distanceFirstDay} км')
while distanceLastDay > distanceFirstDay :
    distanceFirstDay = distanceFirstDay + distanceFirstDay*0.1
    firstDay = firstDay + 1
    print("В", firstDay, '- й день он пробежал: ', distanceFirstDay, 'км')
else:
    lastDay = firstDay
    print("Ответ: на", lastDay, '- й день он пробежал не менее ', distanceLastDay, 'км')