# Каракотова Наталья ИУ7-13Б

# Программа предназначена для поворота квадратной матрицы 
# на 90 градусов по часовой стрелке и на 90 градусов против часовой стрелки

# Данные, принимаемые программой на вход:
# n – количество строк и столбцов в квадратной матрице

# Переменные функций проверки введённого значения:
# text – приглашение ввода
# type_1 – тип числа, который можно использовать в данном пункте
# n – строка, которую мы проверяем на целочисленнное (и положительное) значение
# dot – массив строки, разделённой точками
# e – массив строки, разделённой е

# Переменные для вычислений:
# a – матрица

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

# Ввод количества строк и столбцов в квадратной матрице
n = check_num('\nВведите количество строк и столбцов в квадратной матрице: ', '+')

print()

a = []

# Заполнение матрицы
for i in range(n):
	a.append([])
	for j in range(n):
		a[i].append(check_num('Введите {:} элемент {:} строки: '.format(j + 1, i + 1), ''))

# Поворот по часовой стрелке
for i in range(n // 2):
	for j in range(i, n - i - 1):
		a[i][j], a[j][n - i - 1], a[n - i - 1][n - j - 1], a[n - j - 1][i] =\
		 a[n - j - 1][i], a[i][j], a[j][n - i - 1], a[n - i - 1][n - j - 1]


# Вывод матрицы
print('\nМатрица, повёрнутая по часовой стрелке: ')
for i in range(n):
	for j in range(n):
		print('{:<10.4}'.format(a[i][j]), end='')
	print()

# Поворот против часовой стрелки
for i in range(n // 2):
	for j in range(i, n - i - 1):
		a[i][j], a[j][n - i - 1], a[n - i - 1][n - j - 1], a[n - j - 1][i] =\
		 a[j][n - i - 1], a[n - i - 1][n - j - 1], a[n - j - 1][i], a[i][j]

# Вывод митрицы
print('\nМатрица, повёрнутая против часовой стрелки: ')
for i in range(n):
	for j in range(n):
		print('{:<10.4}'.format(a[i][j]), end='')
	print()

print()






