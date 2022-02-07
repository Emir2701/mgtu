# Каракотова Наталья ИУ7-13Б

# Программа предназначена для сортировки списков методом простого выбора 
# и сравнения времени сортировки на массивах с различными данными

import random
import timeit

# Проверка введённого значения
def check_num(text, type_1):
	text_1 = str(input(text))

	while True:
		# Если пустая строка
		while not text_1:
			text_1 = input(text)

		# Если нужно целое число
		if type_1 == '+':
			if integer(text_1):
					return int(text_1)
			else:
				print('Введите целое число.')
				text_1 = input(text)		

# Проверка на целое:
def integer(n):
    # Если у числа есть знак
    if n[:1] == '+' or n[:1] == '-':
        n = n[1:]
    return n.isdigit()

# Функция сортировки
def selection_sort(mas):
	start_time = timeit.default_timer()
	for i in range(len(mas)):
		min_ind = i
		for j in range(i + 1,len(mas)):
			if mas[j] < mas[min_ind]: 
				min_ind = j
		mas[i],mas[min_ind] = mas[min_ind], mas[i]
	time = timeit.default_timer() - start_time
	return mas, time


# Ввод списка
n = check_num("Введите количество элементов в списке: ", "+")
while n <= 0:
		print("Количество элементов должно быть положительным числом.")
		n = check_num("Введите количество элементов в списке: ", "+")

mas = [0] * n

for i in range(n):
	mas[i] = check_num("Введите {:}-е число: ".format(i + 1), "+")


print("Отсортированный массив: ", *(selection_sort(mas)[0]))

size = [0] * 3

for i in range(3):
	size[i] = check_num("Введите {:}-ю размерность массивов: ".format(i + 1), "+")
	while size[i] <= 0:
		print("Размерность массивов должна быть положительным числом.")
		size[i] = check_num("Введите {:}-ю размерность массивов: ".format(i + 1), "+")

size = selection_sort(size)[0]

# Заполнение списков
mas_sort_n3 = [i for i in range(size[2])]
mas_random_n3 = [random.randint(0, size[2]) for i in range(size[2])]  
mas_unsort_n3 = [i for i in range(size[2] - 1, -1, -1)]

mas_sort_n2 = mas_sort_n3[:size[1]]
mas_random_n2 = mas_random_n3[:size[1]]
mas_unsort_n2 = mas_unsort_n3[:size[1]]

mas_sort_n1 = mas_sort_n3[:size[0]]
mas_random_n1 = mas_random_n3[:size[0]]
mas_unsort_n1 = mas_unsort_n3[:size[0]]

# Время сортировки
mas_sort_n3 = selection_sort(mas_sort_n3)[1]
mas_random_n3 = selection_sort(mas_random_n3)[1]
mas_unsort_n3 = selection_sort(mas_unsort_n3)[1]

mas_sort_n2 = selection_sort(mas_sort_n2)[1]
mas_random_n2 = selection_sort(mas_random_n2)[1]
mas_unsort_n2 = selection_sort(mas_unsort_n2)[1]

mas_sort_n1 = selection_sort(mas_sort_n1)[1]
mas_random_n1 = selection_sort(mas_random_n1)[1]
mas_unsort_n1 = selection_sort(mas_unsort_n1)[1]

print('-' * 77)
print('|                                 |', '{:^11}'.format(size[0]), '|', '{:^11}'.format(size[1]), '|', '{:^11}'.format(size[2]), '|')
print('-' * 77)
print('|Упорядоченный список             |', '{:<11.8}'.format(mas_sort_n1), '|', '{:<11.8}'.format(mas_sort_n2), '|', '{:<11.8}'.format(mas_sort_n3), '|')
print('-' * 77)
print('|Случайный список                 |', '{:<11.8}'.format(mas_random_n1), '|', '{:<11.8}'.format(mas_random_n2), '|', '{:<11.8}'.format(mas_random_n3), '|')
print('-' * 77)
print('|Упорядоченный в обратном порядке |', '{:<11.8}'.format(mas_unsort_n1), '|', '{:<11.8}'.format(mas_unsort_n2), '|', '{:<11.8}'.format(mas_unsort_n3), '|')
print('-' * 77)



