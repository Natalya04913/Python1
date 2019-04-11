# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.

names = ['Max', 'Shae', 'Alex', 'Massimo', 'Marina', 'Antonio', 'Misha', 'Maria']
salaries = [40000, 67000, 59000, 87000, 540000, 760000, 35000, 79000]
dict_salaries = dict(zip(names, salaries))
print(dict_salaries)
file = open('salary.txt', 'a+', encoding='utf-8')
for key, value in dict_salaries.items():
    file.write(f'{key} - {value} \n')
file.close()
with open('salary.txt') as file:
    for line in file:
        name_out, salary_out = line.split(' - ')
        if int(salary_out) < 500000:
            salary_out = int(salary_out) - (int(salary_out)) * 0.13
            print(name_out.upper(), ' - ', salary_out)