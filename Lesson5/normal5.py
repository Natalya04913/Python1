# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os
import sys


def print_help():
    print('1. Перейти в папку')
    print('2. Просмотреть содержимое текущей папки')
    print('3. Удалить папку')
    print('4. Создать папку')


def go_to_dir():
    if not dir_name:
        print('Folder name not entered')
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.chdir(dir_path)
        print(os.getcwd())
    except FileNotFoundError:
        print('Folder does not exist')


from easy5 import create_dir
from easy5 import delete_dir
from easy5 import display

user_input = {
    'help': print_help,
    '1': go_to_dir,
    '2': display,
    '3': delete_dir,
    '4': create_dir
}
try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if user_input.get(key):
        user_input[key]()
    else:
        print("Задан неверный ключ")

