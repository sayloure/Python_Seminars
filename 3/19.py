"""
Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K –
положительное число.
Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]
"""

# Решени 1
# list_1 = [1, 2, 3, 4, 5]
# list_2 = []
# k = int(input("Введите k: "))

# for i in range(0, len(list_1)):
#     if i <(len(list_1)-k):
#         list_2.append(list_1[k+i-1])
#     else:
#         list_2.append(list_1[i-k])
        
# print((list_2))


# Решение 2
# lst = [1, 2, 3, 4, 5]
# k = 3
# for i in range(k):
#     el = lst.pop()
#     lst.insert(0, el)
# print(lst)


# Решение 3

# 0 1 2 3 4
my_list = [1, 2, 3, 4, 5]
# -1 -2 -3 -4 -5

k = 3
k = k % len(my_list)

print(my_list[-k:] + my_list[:-k])