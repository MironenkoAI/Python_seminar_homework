""" Задача 16: Требуется вычислить, сколько раз встречается некоторое число X 
в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – 
количество элементов в массиве. В последующих строках записаны N целых чисел Ai. 
Последняя строка содержит число X
n = 5
1 2 3 4 5
x = 3
-> 1 """

import random
N = int(input('Введите длину списка N: '))
x = int(input('Введите искомое число X от 1 до 9: '))
print()
print('В последовательности:', end = ' ')

count = 0
for i in range(N):
    list = random.randrange(1, 10)
    print(list, end = ' ')
    if list == x:
        count += 1
print()
print(f'Число {x} встречается: {count} раз(а)')
