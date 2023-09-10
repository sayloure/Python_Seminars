""" 
Напишите программу, которая на вход принимает
два числа A и B, и возводит число А в целую степень B с
помощью рекурсии.

A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8
"""


def step(a, b):
    if b == 0:
        return 1
    elif b < 0:
        return 1 / (a * step(a, -b - 1))
    else:
        return a * step(a, b - 1)


A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

print(step(A, B))
