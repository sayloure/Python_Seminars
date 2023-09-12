"""
Даны два массива чисел. Требуется вывести те элементы
первого массива (в том порядке, в каком они идут в первом
массиве), которых нет во втором массиве. Пользователь вводит
число N - количество элементов в первом массиве, затем N
чисел - элементы массива. Затем число M - количество
элементов во втором массиве. Затем элементы второго массива
Ввод: 
7 
3 1 3 4 2 4 12
6
4 15 43 1 15 1 (каждое число вводится с новой строки)
Вывод:
3 3 2 12
"""
from random import randint

# Решение 1
# def deviation(lst1, lst2):
#     return [el for el in list_1 if el not in list_2]

# n = int(input('Введите количество элементов: '))
# list_1 = [randint(1, 11) for i in range(n)]
# print(*list_1)
# m = int(input('Введите количество элементов: '))
# list_2 = [randint(1, 11) for i in range(m)]
# print(*list_2)
# list_3 = deviation(list_1, list_2)
# print(*list_3)


# Решение 2
def sortArr (arr1, arr2):
    arr3 = []
    for i in arr1:
        if i not in arr2:
            arr3.append(i)
    return arr3

def elInput (n):
    array_1 = []
    for i in range(n):
        array_1.append(int(input(f"Enter numbers of the array {i}: ")))
    return array_1

n = int (input ("Enter quontity of elements for array: "))
m = int (input ("Enter quontity of elements for array: "))

# array_1 = elInput(n)
# array_2 = elInput(m)
# array_3 = sortArr(array_1, array_2)
# print (array_3)

array_3 = sortArr(elInput(n), elInput(m))
print (array_3)
