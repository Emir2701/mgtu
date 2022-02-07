# Каракотова Наталья ИУ7-13Б

# Программа предназначена для работы с базой данных склада

# Переменные принимаемые программой на вход:
# num – номер пункта
# path – путь файла
# word – название овоща, который нужно найти
# count – количество названного овоща

# Переменные функций проверки введённого значения:
# text – приглашение ввода
# type_1 – тип числа, который можно использовать в данном пункте
# n – строка, которую мы проверяем на целочисленнное (и положительное) значение


# Переменные для вычислений:
# len_col – список максимальных длин столбцов
# s – текущая строка
# f – текущий файл
# veg – название нового овоща
# price – цена нового овоща


import os

# Проверка введённого значения
def check_num(text, type_1):
	text_1 = str(input(text))

	while True:
		# Если пустая строка
		if not text_1:
			text_1 = input(text)

		# Если нужно целое неотрицательное число
		if type_1 == '+':
			if positive(text_1):
					return int(text_1)
			else:
				print('Введите целое неотрицательное число.')
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
    # # Число не ноль
    # if n[0] == '0':
    # 	return False
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

# Проверка наличия файла
def check_path(path):

	# Существует ли файл с таким путём
	if not os.path.exists(path):
		return False

	return True

# Проверка является ли файл нашей базой данных
def check_file(path):
	# Открываем файл на чтение

	try:
		f = open(path, 'r', encoding='utf-8')
		f.readline()
		f.seek(0)
		f.close()

	except:
		print('Введён неверный путь')
		return

	f = open(path, 'r', encoding='utf-8')

	# Начальное количество символов в каждом столбце
	len_col = [5, 4, 10]

	s = f.readline()
	# Считываем строки до того момента, пока не найдётся пустая строка
	while s.strip() != '':
		# Разделяем строки по табу
		s = s.strip().split('\t')
		# Проверяем количество колонок в открытом файле
		if len(s) != 3:
			f.close()
			return False
		else:
			# проверяем соответствие типов данных в каждой колонке
			if is_float(s[1]) and float(s[1]) > 0 and positive(s[2]):
				for i in range(3):
					# Запоминаем максимальную длину каждой колонки
					len_col[i] = max(len_col[i], len(s[i]))
				s = f.readline()
			else:
				f.close()
				return False


	return len_col

# Выбор файла
def select_file():
	path = input('Введите путь файла: ')
	print()

	# Если пользователь ввёл только имя, то ищем файл в нашей папке
	if (not os.sep in path) and path:
		path = '/Users/natalakarakotova/progi/lab12/' + path


	# Если такого файла не существует
	if not check_path(path):
		print('Вы ввели путь несуществующего файла. Для дальнейшей работы требуется',
		      'инициализировать файл (пункт 2).')
		print()
	
	return path

# Инициализация файла
def init_file(path):

	if path:
		# Открываем на запись (перезапись)
		try:
			f = open(path, 'w', encoding='utf-8')
			print('Файл инициализирован.')
			f.close()
		except:
			print('Введён неверный путь.')

	else:
		print('Укажите путь файла в пункте 1.')
		print()


# Вывод базы данных
def print_base(path):
	if path:
		if check_path(path):
			try:
				f = open(path, 'r', encoding='utf-8')
				f.readline()
				f.seek(0)
				f.close()

			except:
				print('Введён неверный путь.')
				return

			f = open(path, 'r', encoding='utf-8')	

			len_col = check_file(path)
			if len_col:

				s = f.readline()

				if s.strip() == '':
					print('Файл пустой.')

				else:
					print('Товар', ' ' * (len_col[0] - 5), 'Цена', ' ' * (len_col[1] - 4), 'Количество', ' ' * (len_col[2] - 10))

					while s.strip() != '':
						s = s.strip().split('\t')
						print(s[0], ' ' * (len_col[0] - len(s[0])), s[1], ' ' * (len_col[1] - len(s[1])), s[2], ' ' * (len_col[2] - len(s[2])))
						s = f.readline()
				print()
			else:
				print('В данном файле нет базы данных.')
				print()
	
		else:
			print('Файл не существует. Для работы инициализируйте файл.')
			print()

	else:
		print('Путь файла отсутствует.')
		print()


# Добавление записи
def add_note(path):
	if path:
		if check_path(path):
			try:
				f = open(path, 'a', encoding='utf-8')
				f.write()
				f.close()

			except:
				print('Введён неверный путь.')
				return

			f = open(path, 'a', encoding='utf-8')	
			
			# Добавление названия овоща
			veg = input('Введите название товара: ')
			print()

			while not veg:
				print('Вы не ввели слово.')
				veg = input('Введите название товара: ')
				print()
				
			veg = veg.replace('\t', ' ')

			# Добавление цены
			price = check_num('Введите цену товара: ', '')
			print()

			while not price > 0:
				print('Цена должна быть неотрицательной.')
				price = check_num('Введите цену товара: ', '')
				print()

			# Добавление количества
			count = check_num('Введите количество товара: ', '+')
			print()

			# Открываем файл на дозапись
			f = open(path, 'a', encoding='utf-8')
			f.write(veg + '\t' + str(price) + '\t' + str(count) + '\n')
			f.close()

			
		else:
			print('Файл не существует. Для работы инициализируйте файл.')
			print()
	else:
		print('Укажите путь файла в пункте 1.')
		print()


# Поиск по одному полю
def one_field(path):
	if path:
		if check_path(path):
			try:
				f = open(path, 'r', encoding='utf-8')
				f.readline()
				f.seek(0)
				f.close()
				
			except:
				print('Введён неверный путь.')
				return

			f = open(path, 'r', encoding='utf-8')	

			len_col = check_file(path)
			if len_col:

				s = f.readline()

				if s.strip() == '':
					print('Файл пуст.')
					return

				word = input('Введите название товара: ')
				while not word:
					print('Вы не ввели слово.')
					word = input('Введите название товара: ')

				print()
				c = 0

				while s.strip() != '':
					s = s.strip().split('\t')
					if s[0] == word:
						# Если первый раз нашли товар
						if c == 0:

							print('Товар', ' ' * (len_col[0] - 4), 'Цена', ' ' * (len_col[1] - 4), 'Количество', ' ' * (len_col[2] - 10))
							c += 1

						print(s[0], ' ' * (len_col[0] - len(s[0])), s[1], ' ' * (len_col[1] - len(s[1])), s[2], ' ' * (len_col[2] - len(s[2])))

					s = f.readline()
				print()

				if c == 0:
					print('Товар не найден.')
					print()

				f.close()

			else:
				print('В данном файле нет базы данных.')
				print()
			

		else:
			print('Файл не существует. Для работы инициализируйте файл.')
			print()

	else:
		print('Путь файла отсутствует.')
		print()



# Поиск по 2м полям
def two_field(path):
	if path:
		if check_path(path):
			try:
				f = open(path, 'r', encoding='utf-8')
				f.readline()
				f.seek(0)
				f.close()
				
			except:
				print('Введён неверный путь.')
				return

			f = open(path, 'r', encoding='utf-8')	


			len_col = check_file(path)
			if len_col:
				s = f.readline()

				if s.strip() == '':
					print('Файл пуст.')
					return

				word = input('Введите название товара: ')

				while not word:
					print('Вы не ввели слово.')
					word = input('Введите название товара: ')

				count = check_num('Введите количество товара: ', '+')
				print()

				c = 0
				while s.strip() != '':
					s = s.strip().split('\t')
					if s[0] == word and s[2] == str(count):
						# Если первый раз нашли товар
						if c == 0:

							print('Товар', ' ' * (len_col[0] - 4), 'Цена', ' ' * (len_col[1] - 4), 'Количество', ' ' * (len_col[2] - 10))
							c += 1

						print(s[0], ' ' * (len_col[0] - len(s[0])), s[1], ' ' * (len_col[1] - len(s[1])), s[2], ' ' * (len_col[2] - len(s[2])))

					s = f.readline()
				print()

				if c == 0:
					print('Совпадения не найдены.')
					print()

				f.close()

			else:
				print('В данном файле нет базы данных.')
				print()
		
		else:
			print('Файл не существует. Для работы инициализируйте файл.')
			print()

	else:
		print('Путь файла отсутствует.')
		print()


path = ''

# Работа с меню
while True:
	print()
	print('Меню:\n',
		   '1. Выбрать файл для работы\n',
		   '2. Инициализировать базу данных\n',
		   '3. Вывести содержимое базы данных\n',
		   '4. Добавить запись в базу данных\n',
		   '5. Поиск по одному полю\n',
		   '6. Поиск по двум полям\n',
		   '7  Завершить программу.')
	print()

	num = check_num('Введите номер меню: ', '+')
	print()

	if num == 1:
		path = select_file()

	elif num == 2:
		init_file(path)

	elif num == 3:
		print_base(path)

	elif num == 4:
		add_note(path)

	elif num == 5:
		one_field(path)

	elif num == 6:
		two_field(path)

	elif num == 7:
		break

	else:
		print('Пункта меню с таким номером нет.')
		print()




