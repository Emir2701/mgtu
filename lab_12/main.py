# Шимшир Эмирджан ИУ7-13Б

# Требуется написать программу, которая позволит с помощью меню выполнить следующие действия:
# 1. Выбрать файл для работы
# 2. Инициализировать базу данных
# 3. Вывести содержимое базы данных
# 4. Добавить запись в базу данных
# 5. Поиск по одному полю
# 6. Поиск по двум полям

# Запрашивает значения для новой строки базы данных и записывает её

# def add_line_to_database(file_name):

# Проверяет файл и выводит его, если тот существует и
# является базой данных

# def print_database(file_name):

# Создаёт или открывает файл по имени

# def init_database(file_name):

# Находит совпадения по одному полю

# def find_by_one_field(file_name):

# Функция ввода поля

# def enter():

# Находит совпадения по одному полю

# def find_by_two_fields(file_name):
from cheak_func import *



# Запрашивает значения для новой строки базы данных и записывает её

def add_line_to_database(file_name):

	if file_name == None:
		print("Файл для работы не был указан")
		return
	try:
		file = open(file_name, 'a')
	except:
		print("Файл не может быть открыт или создан")
		return

	name = input("Введите имя держателя карты: ")
	while len(name) >= 20 or ',' in name:
		print("Ошибка ввода имени")
		name = input("Введите имя держателя карты: ")
	number = correct_input('Введите номер карты: ', "int+")
	number = str(number)
	while len(number) != 16 or ',' in number:
		print("Ошибка ввода номера карты")
		number = correct_input('Введите номер карты: ', "int+")
		number = str(number)
	date = input("Введите срок действия карты: ")
	while len(date) != 5 or ',' in date:
		print("Ошибка ввода срока действия карты")
		date = input("Введите срок действия карты: ")
	cvv = correct_input('Введите CVV код карты: ', "int+")
	cvv = str(cvv)
	while len(cvv) != 4 or ',' in cvv:
		print("Ошибка ввода CVV кода карты")
		cvv = correct_input('Введите CVV код карты: ', "int+")
		cvv = str(cvv)
	bank = input("Введите название банка: ")
	while len(bank) >= 20 or ',' in bank:
		print("Ошибка ввода названия банка")
		bank = input("Введите название банка: ")
	file.write(name + ',' + number + ',' + date + ',' + cvv + ',' + bank + '\n')
	file.close()


# Проверяет файл и выводит его, если тот существует и
# является базой данных

def print_database(file_name):

	if file_name == None:
		print("Файл для работы не был указан")
		return None

	try:
		file = open(file_name, 'r')
	except:
		print("Файл не может быть открыт или его не существует")
		return
	for s in file:
		#print(s)
		if s.count(',') != 4 and s != '':
			
			print("Ошибка, это не база данных")
			file.close()
			return None

	empty = True
	file = open(file_name, 'r')
	
	for s in file:
		if s[-1] == '\n':
			s = s[:-1]
		l = s.split(',')
		
		empty = False

	file.close()
	if empty:
		print("Пустой файл")
		return None
	print('|' + '-'*104 + '|')
	print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format('Имя держателя карты', 'номер карты', 'срок действия', 'код CVV','банк'))
	print('|' + '-'*104 + '|')
	file = open(file_name, 'r')
	
	for s in file:
		if s[-1] == '\n':
			s = s[:-1]
		l = s.split(',')
		
		print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(l[0], l[1], l[2], l[3], l[4]))
		print('|' + '-'*104 + '|')
		empty = False

	file.close()

# Создаёт или открывает файл по имени

def init_database(file_name):
    
    if file_name == None:
        print("Файл для работы не был указан")
        return None
    try:
        file = open(file_name, 'w')
        file.close()
        return file_name
    except:
        print("Файл не может быть открыт или создан")
        return None

# Находит совпадения по одному полю

def find_by_one_field(file_name):
	if file_name == None:
		print("Файл для работы не был указан")
		return None

	try:
		file = open(file_name, 'r')
	except:
		print("Файл не может быть открыт или его не существует")
		return
	for s in file:
		
		if s.count(',') != 4 and s != '':
			print("Ошибка, это не база данных")
			file.close()
			return None

	empty = True
	file = open(file_name, 'r')
	
	for s in file:
		if s[-1] == '\n':
			s = s[:-1]
		l = s.split(',')
		
		empty = False

	file.close()
	if empty:
		print("Пустой файл")
		return None

	field = None
	while field == None:
		print('1. Имя держателя карты')
		print('2. номер карты')
		print('3. срок действия')
		print('4. код CVV')
		print('5. банк')
		x = correct_input("Введите номер нужного поля: ", 'int+')
		if 1 <= x <= 5:
			field = x
		else:
			print('Ошибка, попробуйте еще раз')
	if field == 1:

		value = input("Введите имя держателя карты: ")
		while len(value) >= 20:
			print("Ошибка ввода имени")
			value = input("Введите имя держателя карты: ")
	elif field == 2:
		value = correct_input('Введите номер карты: ', "int+")
		value = str(value)
		while len(value) != 16:
			print("Ошибка ввода номера карты")
			value = correct_input('Введите номер карты: ', "int+")
			value = str(value)
	elif field == 3:
		value = input("Введите срок действия карты: ")
		while len(value) != 5:
			print("Ошибка ввода срока действия карты")
			value = input("Введите срок действия карты: ")
	elif field == 4:
		value = correct_input('Введите CVV код карты: ', "int+")
		value = str(value)
		while len(value) != 4:
			print("Ошибка ввода CVV кода карты")
			value = correct_input('Введите CVV код карты: ', "int+")
			value = str(value)

	elif field == 5:
		value = input("Введите название банка: ")
		while len(value) >= 20:
			print("Ошибка ввода названия банка")
			value = input("Введите название банка: ")
	print('|' + '-'*104 + '|')
	print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format('Имя держателя карты', 'номер карты', 'срок действия', 'код CVV','банк'))
	print('|' + '-'*104 + '|')
	file = open(file_name, 'r')
	NO = True
	for s in file:
		if s[-1] == '\n':
			s = s[:-1]
		l = s.split(',')
		if l[field - 1] == value:
			print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(l[0], l[1], l[2], l[3], l[4]))
			print('|' + '-'*104 + '|')
			NO = False
	if NO:
		print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format('нет данных', 'нет данных', 'нет данных', 'нет данных','нет данных'))

	file.close()

# Функция ввода поля

def enter():
	field1 = None
	
	while field1 == None :
		print('1. Имя держателя карты')
		print('2. номер карты')
		print('3. срок действия')
		print('4. код CVV')
		print('5. банк')
		x = correct_input("Введите номер нужного поля: ", 'int+')
		if 1 <= x <= 5:
			field1 = x
		else:
			print('Ошибка, попробуйте еще раз')
	if field1 == 1:

		value1 = input("Введите имя держателя карты: ")
		while len(value1) >= 20:
			print("Ошибка ввода имени")
			value1 = input("Введите имя держателя карты: ")
	elif field1 == 2:
		value1 = correct_input('Введите номер карты: ', "int+")
		value1 = str(value1)
		while len(value1) != 16:
			print("Ошибка ввода номера карты")
			value1 = correct_input('Введите номер карты: ', "int+")
			value1 = str(value1)
	elif field1 == 3:
		value1 = input("Введите срок действия карты: ")
		while len(value1) != 5:
			print("Ошибка ввода срока действия карты")
			value1 = input("Введите срок действия карты: ")
	elif field1 == 4:
		value1 = correct_input('Введите CVV код карты: ', "int+")
		value1 = str(value1)
		while len(value1) != 4:
			print("Ошибка ввода CVV кода карты")
			value1 = correct_input('Введите CVV код карты: ', "int+")
			value1 = str(value1)

	elif field1 == 5:
		value1 = input("Введите название банка: ")
		while len(value1) >= 20:
			print("Ошибка ввода названия банка")
			value1 = input("Введите название банка: ")

	return field1, value1

# Находит совпадения по одному полю

def find_by_two_fields(file_name):
	if file_name == None:
		print("Файл для работы не был указан")
		return None

	try:
		file = open(file_name, 'r')
	except:
		print("Файл не может быть открыт или его не существует")
		return
	for s in file:
		
		if s.count(',') != 4 and s != '':
			print("Ошибка, это не база данных")
			file.close()
			return None

	empty = True
	file = open(file_name, 'r')
	
	for s in file:
		if s[-1] == '\n':
			s = s[:-1]
		l = s.split(',')
		
		empty = False

	file.close()
	if empty:
		print("Пустой файл")
		return None

	field1, value1 = enter()
	field2, value2 = enter()

	while field1 == field2:
		print("Поля совпадают, введите разные поля")
		field1, value1 = enter()
		field2, value2 = enter()
	print('|' + '-'*104 + '|')
	print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format('Имя держателя карты', 'номер карты', 'срок действия', 'код CVV','банк'))
	print('|' + '-'*104 + '|')
	file = open(file_name, 'r')
	NO = True
	for s in file:
		if s[-1] == '\n':
			s = s[:-1]
		l = s.split(',')
		if l[field1 - 1] == value1 and l[field2 - 1] == value2:
			print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(l[0], l[1], l[2], l[3], l[4]))
			print('|' + '-'*104 + '|')
			NO = False
	if NO:
		print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format('нет данных', 'нет данных', 'нет данных', 'нет данных','нет данных'))
		print('|' + '-'*104 + '|')
	file.close()

def main():
	file_name = None
	print("База данных")
	while True:
		
		input_text = '(Для вывода меню введите 7). Введите номер функции: '
		func = correct_input(input_text, 'int+')

		if func == 1:

			file_name = input("Введите путь к нужному файлу: ")
			
		elif func == 2:

			file_name = init_database(file_name)

		elif func == 3:

			print_database(file_name)

		elif func == 4:

			add_line_to_database(file_name)

		elif func == 5:

			find_by_one_field(file_name)

		elif func == 6:

			find_by_two_fields(file_name)

		elif func == 7:
			 # вывод меню
		    print('------------------------------------------------------------------------------------------------')
		    print('Меню:')
		    print('1. Выбрать файл для работы')
		    print('2. Инициализировать базу данных')
		    print('3. Вывести содержимое базы данных')
		    print('4. Добавить запись в базу данных')
		    print('5. Поиск по одному полю')
		    print('6. Поиск по двум полям')
		    print('7. Вывод меню')
		    print('8. Завершение программы')
		    print('------------------------------------------------------------------------------------------------')
		elif func == 8:
			
			break
			
		else:
		    print('Ошибка, нет такой функции')

main()


