import random
number=random.randint(1, 100)
number_low=1
number_high=100
answer = None
while answer != '=':
    print (f"Ваше число {number}?")
    answer = input('Введите реакцию: ')
    if answer=='<':
        number_high=number-1
        number=random.randint(number_low, number-1)
    elif answer=='>':
        number_low = number+1
        number=random.randint(number+1, number_high)
print('Компьютер угадал!')