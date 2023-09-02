"""
Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и 
вывести его.
"""
# list_1 = [1, 4, 3, 7, 8, 9, 2]
# k = 8
# el = []
# for i in list_1:
#     if k == i:
#         el.append(i)
#     elif k % i == 1:
#         # el = i
#         el.append(i)
#         # print(i)
# print(max(el))

list_1 = [1, 12, 6, 7, 8, 15]
k = 11
result = k
for i in range(len(list_1)):
    if abs(list_1[i] - k) < result:
        temp = i
        result = abs(list_1[i] - k)
        
print(list_1[temp])