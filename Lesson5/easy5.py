# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

dir_names = ['dir_1', 'dir_2', 'dir_3', 'dir_4', 'dir_5', 'dir_6', 'dir_7', 'dir_8', 'dir_9']
for dir_name in dir_names:
    def create_dir():
        dir_path = os.path.join(os.getcwd(), dir_name)
        try:
                os.mkdir(dir_path)
        except FileExistsError:
            print(f'Directory {dir_name} already exists')
    create_dir()
print(os.listdir())

for dir_name in dir_names:
    def delete_dir():
        dir_path = os.path.join(os.getcwd(), dir_name)
        try:
            os.rmdir(dir_path)
        except OSError:
            print(f'Unable to delete directory {dir_name}')
    delete_dir()


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def display():
    print(os.listdir())
display()


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

from shutil import copyfile

copyfile(__file__, os.path.join(os.getcwd(), 'easy5_copy'))

print(os.listdir())