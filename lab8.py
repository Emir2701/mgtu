# Каракотова Наталья ИУ7-13Б

# Программа предназначена для работы с целочисленной матрицей с помощью меню

# Данные, принимаемые на вход программойЖ
# columns - количество столбцов
# lines – количество строк
# num – номер строки/столбца, который нужно добавить/убрать

# Переменные для вычислений:
# text – приглашение ввода
# type_1 – тип числа, который можно использовать в данном пункте
# n – строка, которую мы проверяем на целочисленнное (и положительное) значение
# s – строка для вывода матрицы в виде таблицы
# matrix - матрица
# line_count/column_count - массив, в котором запоминается количество элементов в строке/столбце, подходящих под условие
# count - текущее количество элементов в строке/столбце, подходящих под условие
# count_max - максимальное количество элементов в строке/столбце, подходящих под условие
# column_summ - сумма элементов столбца
# summ - текущая сумма
# ind / ind_max / ind_min - индекс подходящей строки/столбца

# Проверка введённого значения
def check_num(text, type_1):
	text_1 = str(input(text))

	while True:
		# Если пустая строка
		if not text_1:
			text_1 = str(input(text))
		# Если нужно целое положительное число
		if type_1 == '+':
			if positive(text_1):
					return int(text_1)
			else:
				print('Введите целое положительное число.')
				text_1 = str(input(text))

		# Если нужно целое число
		elif type_1 == '':
			if is_int(text_1):
					return int(text_1)
			else:
				print('Введите целое число.')
				text_1 = str(input(text))
				

# Проверка на целое положительное:
def positive(n):
    # Если у числа есть знак
    if n[0] == '+':
        n = n[1:]
    # Число не ноль
    if n[0] == '0':
    	return False
    return n.isdigit()

# Проверка на целое:
def is_int(n):
    # Если у числа есть знак
    if n[0] == '+' or n[0] == '-':
        n = n[1:]
    return n.isdigit()

# Вывод матрицы в виде таблицы 
def output_matrix(matrix_1, lines_1, columns_1):
	s = ''
	for i in range(lines_1):
		for j in range(columns_1):
			s += '{:<10}'.format(matrix_1[i][j])
		s += '\n\n'
	return s

# Ввод матрицы с клавиатуры
def input_matrix():
	lines_1 = check_num('Введите количество строк: ', '+')
	columns_1 = check_num('Введите количество столбцов: ', '+')
	matrix_1 = []
	for i in range(lines_1):
		matrix_1.append([])
		for j in range(columns_1):
			matrix_1[i].append(check_num('Введите {:} элемент {:} строки: '.format(j+1, i+1), ''))
	return matrix_1, lines_1, columns_1

# Добавление строки в матрицу
def insert_line(matrix_1, lines_1, columns_1):

	if lines_1 > 0:
		num = check_num('Введите номер строки, которую хотите добавить: ', '+')
		if num > lines_1 + 1:
			print('Вы вышли за границу матрицы.')
			matrix_1, lines_1, columns_1 = insert_line(matrix_1, lines_1, columns_1)
			return matrix_1, lines_1, columns_1
	else:
		columns_1 = check_num('Матрица ещё не заполнена. Введите количество элементов в строке: ', '+')
		num = 1

	num -= 1

	# С помощью возможностей питона
	# matrix_1.insert(num, [check_num('Введите элемент: ', '') for i in range(columns_1)])

	# Добавление строки
	matrix_1.append([])
	for i in range(columns_1):
		matrix_1[-1].append(0)
	lines_1 += 1

	# Смещение всех элементов после добавленной строки на одну строку вниз
	for i in range(lines_1 - 1, num, -1):
		for j in range(columns_1):
			matrix_1[i][j] = matrix_1[i - 1][j]


	# Добавление элементов в новую строку
	for i in range(columns_1):
		matrix_1[num][i] = check_num('Введите {:} элемент строки: '.format(i+1), '')

	return matrix_1, lines_1, columns_1

# Удаление строки из митрицы
def remove_line(matrix_1, lines_1, columns_1):
	num = check_num('Введите номер строки, которую хотите удалить: ', '+')

	if num > lines_1:
		print('Вы вышли за границу списка.')
		remove_line(matrix_1, lines_1, columns_1)

	num -= 1

	# С помощью возможностей питона
	# matrix_1.remove(matrix_1[num])

	for i in range(num, lines_1 - 1):
		for j in range(columns_1):
			matrix_1[i][j] = matrix_1[i + 1][j]

	matrix_1.pop()

	lines_1 -= 1

	return matrix_1, lines_1, columns_1

# Добавление столбца в матрицу
def insert_column(matrix_1, lines_1, columns_1):

	if columns_1 > 0:
		num = check_num('Введите номер столбца, который хотите добавить: ', '+')
		if num > columns_1 + 1:
			print('Вы вышли за границу списка.')
			insert_column(matrix_1, lines_1, columns_1)
	else:
		lines_1 = check_num('Матрица ещё не заполнена. Введите количество элементов в столбце: ', '+')
		matrix_1 = [[] for i in range(lines_1)]
		num = 1

	num -= 1

	# С помощью возможностей питона
	# for i in range(lines_1):
	# 	matrix_1[i].insert(num, check_num('Введите элемент: ', ''))
	
	# Добавление дополнительного столбца в конец
	for i in range(lines_1):
		matrix_1[i].append(0)

	columns_1 += 1

	# Смещение всех столбцов от добавляемого вправо
	for i in range(lines_1):
		for j in range(columns_1 - 1, num, -1):
			matrix_1[i][j] = matrix_1[i][j - 1]

	# Добавление столбца
	for i in range(lines_1):
		matrix_1[i][num] = check_num('Введите {:} элемент нового столбца: '.format(i+1), '')

	return matrix_1, lines_1, columns_1

# Удаление столбца
def remove_column(matrix_1, lines_1, columns_1):
	num = check_num('Введите номер столбца, который хотите удалить: ', '+')

	if num > columns_1:
		print('Вы вышли за границу списка.')
		remove_column(matrix_1, lines_1, columns_1)

	num -= 1

	# С помощью возможностей питона
	# for i in range(lines):
	# 	matrix_1[i].remove(num)


	# Смещение всех столбцов, начиная с удаляемого, влево
	for i in range(lines_1):
		for j in range(num, columns_1 - 1):
			matrix_1[i][j] = matrix_1[i][j + 1]

	# Удаление последнего лишнего столбца
	for i in range(lines_1):
		matrix_1[i].pop()

	columns_1 -= 1

	return matrix_1, lines_1, columns_1

# Поиск строки, имеющей наибольшее количество подряд идущих одинаковых элементов
def find_line(matrix_1, lines_1, columns_1):
	line_count = []

	for i in range(lines_1):
		count_max = 1
		count = 1
		for j in range(1, columns_1):
			if matrix_1[i][j] == matrix_1[i][j - 1]:
				count += 1
				if count > count_max:
					count_max = count
			else:
				count = 1
		line_count.append(count_max)

	# Индекс строки
	ind = line_count.index(max(line_count))

	return matrix_1[ind]

# Переставление местами строк с наибольшим и наименьшим количеством отрицательных элементов
def replace_lines(matrix_1, lines_1, columns_1):
	line_count = []

	for i in range(lines_1):
		count = 0
		count_max = 0
		for j in range(columns_1):
			if matrix_1[i][j] < 0:
				count += 1
				if count > count_max:
					count_max = count
		line_count.append(count_max)

	# Индексы строк с максимальным и минимальным количеством таких элементов
	ind_max = line_count.index(max(line_count))
	ind_min = line_count.index(min(line_count))

	matrix_1[ind_max], matrix_1[ind_min] = matrix_1[ind_min], matrix_1[ind_max]

	return matrix_1

# Поиск столбца, который имеет минимальное количество отрицательных элементов
def find_column(matrix_1, lines_1, columns_1):
	column_count = []

	for j in range(columns_1):
		count = 0
		max_count = 0
		for i in range(lines):
			if matrix_1[i][j] < 0:
				count += 1
				if count > max_count:
					max_count = count
		column_count.append(max_count)

	# Индекс строки
	ind = column_count.index(min(column_count))

	column = ''

	# Строка дла вывода столбца вертикально
	for i in range(lines_1):
		column += str(matrix_1[i][ind]) + '\n\n'

	return column

# Переставление местами столбцов с максимальной и минимальной суммой элементов
def replace_columns(matrix_1, lines_1, columns_1):
	column_summ = []

	for j in range(columns_1):
		summ = 0
		for i in range(lines_1):
			summ += matrix[i][j]
		column_summ.append(summ)

	# Индексы строк с максимальной и минимальной суммой
	ind_max = column_summ.index(max(column_summ))
	ind_min = column_summ.index(min(column_summ))

	for i in range(lines_1):
		matrix_1[i][ind_max], matrix_1[i][ind_min] = matrix_1[i][ind_min], matrix_1[i][ind_max]

	return matrix
	


matrix = []
lines = 0
columns = 0
k = 5

while True:
	if k == 5:
		print('Меню:\n',
			  '1. Ввести матрицу\n', 
			  '2. Добавить строку\n', 
			  '3. Удалить строку\n',
			  '4. Добавить столбец\n', 
			  '5. Удалить столбец\n', 
			  '6. Найти строку, имеющую наибольшее количество подряд идущих одинаковых элементов\n',
			  '7. Переставить местами строки с наибольшим и наименьшим количеством отрицательных элементов\n',
			  '8. Найти столбец, имеющий наименьшее количество отрицательных элементов\n',
			  '9. Переставить местами столбцы с максимальной и минимальной суммой элементов\n',
			  '10. Вывести текущую матрицу\n',
			  '11. Завершить программу')
		k = 0

	num_point = check_num('Введите номер пункта меню: ', '+')

	if num_point == 1:
		matrix, lines, columns = input_matrix()
		print(output_matrix(matrix, lines, columns))
		k += 1

	if num_point == 2:
		matrix, lines, columns = insert_line(matrix, lines, columns)
		print(output_matrix(matrix, lines, columns))
		k += 1

	if num_point == 3:
		if lines == 0:
			print('Матрица не заполнена.')
		else:
			matrix, lines, columns = remove_line(matrix, lines, columns)
			print(output_matrix(matrix, lines, columns))
		k += 1

	if num_point == 4:
		matrix, lines, columns = insert_column(matrix, lines, columns)
		print(output_matrix(matrix, lines, columns))
		k += 1

	if num_point == 5:
		if columns == 0:
			print('Матрица не заполнена.')
		else:
			matrix, lines, columns = remove_column(matrix, lines, columns)
			print(output_matrix(matrix, lines, columns))
		k += 1

	if num_point == 6:
		if lines == 0:
			print('Матрица не заполнена.')
		else:
			line = find_line(matrix, lines, columns)
			print(*line)
		k += 1

	if num_point == 7:
		if lines < 2:
			print('В матрице меньше 2х строк.')
		else:
			matrix = replace_lines(matrix, lines, columns)
			print(output_matrix(matrix, lines, columns))
		k += 1

	if num_point == 8:
		if columns == 0:
			print('Матрица не заполнена.')
		else:
			column = find_column(matrix, lines, columns)
			print(column)
		k += 1

	if num_point == 9:
		if columns < 2:
			print('В матрице меньше 2х столбцов.') 
		else:
			matrix = replace_columns(matrix, lines, columns)
			print(output_matrix(matrix, lines, columns))
		k += 1

	if num_point == 10:
		if lines == 0:
			print('Матрица не заполнена.')
		else:
			print(output_matrix(matrix, lines, columns))
		k += 1

	if num_point == 11:
		break

	elif num_point > 11:
		print('Пункта меню с таким номером нет.')
		k += 1

