"""
Дан список чисел. Посчитайте, сколько в нем пар
элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных
строках.
Ввод:
1 2 3 2 3 
Вывод:
2
"""
from random import randint

# Решение 1
# def count_par(list):
#     count = 0
#     for i in range(len(list)):
#         for j in range(i + 1, len(list)):
#             if list[i] == list[j]:
#                 count += 1
#     return count
                

# list_1 = [randint(1, 12) for i in range(int(input('Введите количество элементов: ')))]
# print(list_1)
# print(count_par(list_1))


# Решение 2
def count_par(list):
    count = 0
    for i, el in enumerate(list_1):
        count += list[i + 1:].count(el)
    return count

list_1 = [randint(1, 12) for i in range(int(input('Введите количество элементов: ')))]
print(list_1)
print(count_par(list_1))