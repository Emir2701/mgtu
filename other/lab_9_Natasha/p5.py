# Каракотова Наталья ИУ7-13Б

# Программа предназначена для подсчёта в каждой строке матрицы D количества элементов, 
# превышающих суммы элементов соответствующих строк матрицы Z, размещения этого количества в массиве G, 
# умножения матрицы D на максимальный элемент массива G. 

# Данные, принимаемые на вход программой:
# d_line – количсетво строк матрицы D
# d_col – количество столбцов матрицы D
# z_col – количество столбцов матрицы Z

# Переменные функций проверки введённого значения:
# text – приглашение ввода
# type_1 – тип числа, который можно использовать в данном пункте
# n – строка, которую мы проверяем на целочисленнное (и положительное) значение
# dot – массив строки, разделённой точками
# e – массив строки, разделённой е

# Переменные для вычислений:
# d – матрица D
# z – матрица Z
# z_line – количество строк матрицы Z 
# sum_z – массив суммы элементов каждой строки матрицы Z
# g – массив G количества элементов матрицы D, превышающих сумму элементов матрицы Z 
# max_g – максимальный элемент массива G


# Проверка введённого значения
def check_num(text, type_1):
	text_1 = str(input(text))

	while True:
		# Если пустая строка
		if not text_1:
			text_1 = input(text)

		# Если нужно целое положительное число
		if type_1 == '+':
			if positive(text_1):
					return int(text_1)
			else:
				print('Введите целое положительное число.')
				text_1 = input(text)

		# Если нужно число
		elif type_1 == '':
			if is_float(text_1):
					return float(text_1)
			else:
				print('Введите число.')
				text_1 = input(text)
				

# Проверка на целое положительное:
def positive(n):
    # Если у числа есть знак
    if n[0] == '+':
        n = n[1:]
    # Число не ноль
    if n[0] == '0':
    	return False
    return n.isdigit()

# Проверка на вещественное:
def is_float(n):
	# Если у числа есть знак
    if n[0] == '-' or n[0] == '+':
        n = n[1:]
    # Разделяем по точкам
    dot = n.split('.')
    if len(dot) == 1:
    	# Разделяем по e
        e = n.split('e')
        # Если нет e
        if len(e) == 1:
            return n.isdigit()
        # Если есть e
        elif len(e) == 2:
        	# Проверяем правильную расстановку знаков и цифр в экспоненциальном виде
            return (e[0].isdigit() and
            	    e[1] and
                    ((e[1][0] in '+-' and
                     e[1][1:].isdigit()) or
                     e[1].isdigit()))
    # Если число с точкой 
    elif len(dot) == 2:
    	# Разделяем по e
        e = dot[1].split('e')
        # Если нет e
        if len(e) == 1:
            return dot[0].isdigit() and dot[1].isdigit()
        # Если есть e
        elif len(e) == 2:
        	# Проверяем расстановку знаков и цифр в экспоненциальном виде
            return (dot[0].isdigit() and
                    e[0].isdigit() and
                    e[1] and
                    (e[1][0] in '+-' and 
                     e[1][1:].isdigit() or
                     e[1].isdigit()))
    return False


# Ввод количсетва строк и столбцов матрицы D
print()
d_line = check_num('Введите количество строк в матрицах: ', '+')
d_col = check_num('Введите количество столбцов в матрице D: ', '+')
print()

d = []

# Заполнение матрицы D
for i in range(d_line):
	d.append([])
	for j in range(d_col):
		d[i].append(check_num('Введите {:} элемент {:} строки матрицы D: '.format(j + 1, i + 1), ''))

# Вывод матрицы D
print('\nМатрица D до преобразования: ')
for i in range(d_line):
	for j in range(d_col):
		print('{:<10.4}'.format(d[i][j]), end='')
	print()


z_line = d_line

# Ввод количества столбцов матрицы Z
z_col = check_num('\nВведите количество столбцов в матрице Z: ', '+')
print()

z = []

# Заполнение матрицы Z
for i in range(z_line):
	z.append([])
	for j in range(z_col):
		z[i].append(check_num('Введите {:} элемент {:} строки матрицы Z: '.format(j + 1, i + 1), ''))


sum_z = []

# Подсчёт суммы элементов каждой строки матрицы Z
for i in range(z_line):
	summ = 0
	for j in range(z_col):
		summ += z[i][j]
	sum_z.append(summ)
	summ = 0

g = []

# Количество элементов в строке матрицы D превышающих сумму элементов соответствующей строки матрицы Z
for i in range(d_line):
	count = 0
	for j in range(d_col):
		if d[i][j] > sum_z[i]:
			count += 1
	g.append(count)
	count = 1

max_g = max(g)

# Умножение матрицы D на максимальный элемент массива G
for i in range(d_line):
	for j in range(d_col):
		d[i][j] = d[i][j] * max_g

# Вывод матрицы после преобразования
print('\nМатрица D после преобразования: ')
for i in range(d_line):
	for j in range(d_col):
		print('{:<10.4}'.format(d[i][j]), end='')
	print()

# Вывод массива G
print('\nМассив G: ')
for j in range(len(g)):
	print('{:<10.4}'.format(float(g[j])), end='')

print()


