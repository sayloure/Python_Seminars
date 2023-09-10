"""
Дано натуральное число N и
последовательность из N элементов.
Требуется вывести эту последовательность в
обратном порядке.
Примечание. В программе запрещается
объявлять массивы и использовать циклы
(даже для ввода и вывода).
Input: 2 -> 3 4
Output: 4 3
"""

# 1
# def rev(n):
#     s = input()
#     if n != 1:
#         rev(n - 1)
#     print(s, end=" ")


# n = int(input())
# rev(n)


# 2
def rev(n):
    number = input()
    if n == 1:
        return number
    return rev(n-1) + " " + number

print(rev(4))