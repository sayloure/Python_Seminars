"""
Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes
"""


# Решение 1
# def prostoe(n):
#     if n < 4:
#         return "YES"

#     for i in range(2, n // 2 + 1):
#         if n % i == 0:
#             return "NO"
#     return "YES"


# n = int(input())
# print(prostoe(n))


# Решение 2
def prost(n):
    count = 0
    for i in range(2, n):
        if n % i == 0:
            count += 1
    return count == 0


n = int(input())
print(prost(n))
