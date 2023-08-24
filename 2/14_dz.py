"""
Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
"""

n = int(input("Введите число N: "))

power_of_two = 1
k = 0

while power_of_two <= n:
    print(power_of_two)
    k += 1
    power_of_two = 2 ** k