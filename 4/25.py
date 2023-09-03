"""
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.

Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

"""
# Решение 1
# n = 'a a a b c a a d c d d'.split()
# print(*n)

# for i in range(len(n)):
#     s = n[:i]
#     if s.count(n[i]) == 0:
#         print(n[i], end=' ')
#     else:
#         print(f'{n[i]}_{s.count(n[i])}', end=" ")


# Решение 2
all_letters = 'a a a b c a a d c d d'.split()

letters_count = {}

result_str = ''

for letter in all_letters:
    if letter not in letters_count:
        letters_count[letter] = 1
        result_str += f'{letter} '
    else:
        result_str += f'{letter}_{letters_count[letter]} '
        letters_count[letter] += 1
        
print(result_str)
