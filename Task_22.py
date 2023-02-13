""" Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов 
второго множества. Затем пользователь вводит сами элементы множеств. """

   # РЕШЕНИЕ 1 (с рандомным заполнением)
# import random
# n = int(input('Введите целое число N: '))
# m = int(input('Введите целое число M: '))

# rand_list_1 = [random.randint(1, 20) for i in range(n)]
# rand_list_2 = [random.randint(1, 20) for i in range(m)]

# print(f'Первая последовательность: {rand_list_1}')
# print(f'Вторая последовательность: {rand_list_2}')

# set_sum = sorted(set(rand_list_1).intersection(set(rand_list_2)))
# print(f'Отсортированное множество: {set_sum}')

   # РЕШЕНИЕ 2 (с вводом данных вручную)
n = int(input('Введите целое число N: '))
m = int(input('Введите целое число M: '))

rand_list_1 = input(f'Введите {n} чисел(а) через пробел: ').split()
rand_list_2 = input(f'Введите {m} чисел(а) через пробел: ').split()
if len(rand_list_1) == n and len(rand_list_2) == m:
   set_sum = set(rand_list_1).intersection(set(rand_list_2))
   result = sorted([int(item) for item in set_sum])
   print(f'Отсортированное множество:', end = ' ')
   for i in result:
      print(i, end = ' ')
else:
   print('Количество переменных не соответствует заданной длине множества')


   # ЭТАЛОННОЕ РЕШЕНИЕ
# mol = [int(x) for x in input().split()]
# n = mol[0]
# m = mol[1]
# set_1 = set()
# set_2 = set()
# list_1 = list()
# a = [int(x) for x in input().split()]
# k = set(a)
# for i in k:
#     set_1.add(i)
# b = [int(x) for x in input().split()]
# k1 = set(b)
# for i in k1:
#     set_2.add(i)
# lok = set_1 & set_2
# kool = list(lok)
# kool.sort()
# for i in kool:
#     print(i, end=' ')