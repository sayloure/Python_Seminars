"""
Дан список чисел. Определите, сколько в нем
встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6
"""
# Способ 1
# list_1 = [1, 1, 2, 0, -1, 3, 4, 4]
# print(len(set(list_1)))
# # my_set = set(list_1)
# # print(len(my_set))

# Способ 2
# list_with_duplicates = [1, 1, 2, 0, -1, 3, 4, 4]
# list_1 = []

# for i in list_with_duplicates:
#     if i not in list_1:
#         list_1.append(i)
# print(len(list_1))

# Способ 3
List_1 = [1, 1, 2, 0, -1, 3, 4, 4]
counter = 0
for i in range(len(List_1)):
    if List_1[i] not in List_1[:i]:
        counter += 1
print(counter)