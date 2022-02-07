# Каракотова Наталья ИУ7-13Б

# Программа предназначена для формирования матрицы C путём построчного перемножения матриц A и B одинаковой 
# размерности и вывода суммы всех элементов в столбцах матрицы C

# Данные, принимаемые на вход программой:
# line – количество строк в матрицах  
# col – количество столбцов в матрицах 

# Переменные функций проверки введённого значения:
# text – приглашение ввода
# type_1 – тип числа, который можно использовать в данном пункте
# n – строка, которую мы проверяем на целочисленнное (и положительное) значение
# dot – массив строки, разделённой точками
# e – массив строки, разделённой е

# Переменные для вычислений:
# a – матрица A
# b – матрица B
# c – матрица C
# v – массив V, содержащий сумму элментов в каждом столбце матрицы C

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


# Ввод количества строк и столбцов в матрицах
line = check_num('\nВведите количество строк в матрицах: ', '+')
col = check_num('Введите количество столбцов в матрицах: ', '+')

print()

a = []

# Заполнение матриц A
for i in range(line):
	a.append([])
	for j in range(col):
		a[i].append(check_num('Введите {:} элемент {:} строки матрицы A: '.format(j + 1, i + 1), ''))
print()

b = []

# Заполнение матрицы B
for i in range(line):
	b.append([])
	for j in range(col):
		b[i].append(check_num('Введите {:} элемент {:} строки матрицы B: '.format(j + 1, i + 1), ''))

c = []

# Заполнение матрицы C
for i in range(line):
	c.append([])
	for j in range(col):
		c[i].append(a[i][j] * b[i][j])

v = [0] * line

# Заполнение массива V
for i in range(line):
	for j in range(col):
		v[i] += c[i][j]

# Вывод матрицы C
print('\nМатрица С: ')
for i in range(line):
	for j in range(col):
		print('{:<10.4}'.format(c[i][j]), end='')
	print()

# Вывод массива V
print('\nМассив V: ')
for j in range(line):
	print('{:<10.4}'.format(v[j]), end='')

print()


