# Каракотова Наталья ИУ7-13Б

# Программа предназначена для вывода среза по второму индексу, номер которого задаёт пользователь

# Данные, принимаемые на вход программой:
# x – размер матрицы по X
# y – размер матрицы по Y
# z – размер матрицы по Z
# srez – номер среза

# Переменные функций проверки введённого значения:
# text – приглашение ввода
# type_1 – тип числа, который можно использовать в данном пункте
# n – строка, которую мы проверяем на целочисленнное (и положительное) значение
# dot – массив строки, разделённой точками
# e – массив строки, разделённой е

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


# Ввод размера массива
print()
x = check_num('Введите размер трёхмерного массива по X: ', '+')
y = check_num('Введите размер трёхмерного массива по Y: ', '+')
z = check_num('Введите размер трёхмерного массива по Z: ', '+')
print()

mas = []

# Заполнение массива
for i in range(x):
    mas.append([])
    for j in range(y):
        mas[i].append([])
        for k in range(z):
            mas[i][j].append(check_num('Введите элемент с координатами ({:}, {:}, {:}): '.format(i, j, k), ''))

print()

# Ввод номера среза
def srez_func():
    srez_1 = check_num('Введите номер среза, который нужно вывести: ', '+')
    if srez_1 > y:
        print('Среза с таким номером нет.')
        srez_1 = srez_func()
    return srez_1
    

srez = srez_func()


# Вывод среза
print('\n{:}-й срез по второму индексу: \n'.format(srez))

for i in range(x):
    for j in range(y):
        if j + 1 == srez:
            for k in range(z):
                print('{:<10.4}'.format(matrix[i][k][]), end='')
    print()
print()



