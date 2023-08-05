"""
В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами. 
За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов. Выведите наименьшее число парт, которое нужно приобрести для них.
Input: 20 21 22(ввод чисел НЕ в одну строку)
Output: 32
"""

firstClass = int(input("Количество учащихся в первом классе: "))
secondClass = int(input("Количество учащихся во втором классе: "))
thirdClass = int(input("Количество учащихся в третьем классе: "))

firstClassDesks = (-firstClass) // 2 * (-1)
secondClassDesks = (-secondClass) // 2 * (-1)
thirdClassDesks = (-thirdClass) // 2 * (-1)

Desks = firstClassDesks + secondClassDesks + thirdClassDesks

print(f"Необходимое количество парт = {Desks}")
