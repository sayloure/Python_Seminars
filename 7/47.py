"""
У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
программы используется множество раз и вы не хотите ничего сломать):
transformation = <???>
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
transormed_values = list(map(transformation, values))
Единственный способ вашего взаимодействия с этим кодом - посредством задания
функции transformation.
Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
список значений, а нужно получить его как есть.
Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
копией values.
"""


# def transformation(a):
#     return a + 2


values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] 
# new_list = []
# for item in values:
#     new_list.append((lambda a: a +2)(item))
# print(new_list)

print(list(map(lambda a: a +2, values)))

# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] 
# transormed_values = list(map(transformation, values))

# print(transormed_values)