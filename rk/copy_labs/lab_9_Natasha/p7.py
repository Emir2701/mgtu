# RКаракотова Наталья ИУ7-13Б

# Программа предназначена для замены гласных букв в матрице на точки

# Данные, принимаемые на вход программой:
# line – количество строк м матрице
# col – количество столбцов в матрице

# Переменные функций проверки введённого значения:
# text – приглашение ввода
# type_1 – тип числа, который можно использовать в данном пункте
# n – строка, которую мы проверяем на целочисленнное (и положительное) значение

# Переменные для вычислений:
# matrix – матрица

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

# Проверка на символ
def check_s(text):
	text_1 = input(text)
	while True:
		if not text_1:
			text_1 = input(text)
		if len(str(text_1)) == 1:
			return text_1
		else:
				print('Введите символ.')
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

print()

# Ввод количества строк и столбцов в матрице
line = check_num('Введите количество строк в матрице: ', '+')
col = check_num('Введите количество столбцов в матрице: ', '+')

matrix = []

print()

# Заполнение матрицы
for i in range(line):
	matrix.append([])
	for j in range(col):
		matrix[i].append(check_s('Введите {:} элемент {:} строки матрицы D: '.format(j + 1, i + 1)))

# Замена гласных букв на точки
s = 'EeYyUuIiOoAa'
for i in range(line):
	for j in range(col):
		if matrix[i][j] in s:
			matrix[i][j] = '.'

# Вывод матрицы
print('\nМатрица после преобразования: ')
for i in range(line):
	print(*matrix[i])

print()


		

