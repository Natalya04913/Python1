# Постарайтесь использовать то, что мы прошли на уроке при решении этого ДЗ,
# вспомните про zip(), map(), lambda, посмотрите где лучше с ними, а где они излишни!

# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"

def personal_info():
    name = input('Enter name: ')
    age = input('Enter age: ')
    city = input('Enter city: ')
    result = f'{name}, {age} год(а)/лет, проживает в городе {city}'
    print(result)
personal_info()

# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

def num_input():
    number = input('Enter three numbers divided by space: ')
    split_number = number.split()
    split_number1 = [float(i) for i in split_number]
    max_number = max(split_number1)
    print(f'The highest value entered is {max_number}')
num_input()


# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов

def str_input():
    items = input('Enter groups of symbols divided by space: ')
    split_str = items.split()
    max_str = max(split_str, key=len)
    print(f'The longest string entered is {max_str}')
str_input()