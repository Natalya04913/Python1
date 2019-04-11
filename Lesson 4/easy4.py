# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

import random
list = [random.randint(-100, 100) for _ in range(10)]
new_list = list.copy()
new_list = [i**2 for i in new_list]
print(list, new_list)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

import itertools
fruit_list_1 = ['apple', 'pineapple', 'melon', 'orange']
fruit_list_2 = ['pear', 'peach', 'raisin', 'banana']
result = [i for i in itertools.chain(fruit_list_1, fruit_list_2)]
print(fruit_list_1, fruit_list_2)
print(result)



# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

numbers = [random.randint(-10, 10) for _ in range(10)]
numbers2 = [i for i in numbers if i % 3 == 0 and i > 0 and i % 4 != 0]
print(numbers)
print(numbers2)