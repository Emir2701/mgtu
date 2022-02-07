# Шимшир Эмирджан ИУ7-13Б

# Требуется написать программу, которая позволит с помощью меню выполнить следующие действия по обработке базы данных, хранящейся в бинарном файле:
# 1. Выбрать файл для работы
# 2. Инициализировать базу данных
# 3. Вывести содержимое базы данных
# 4. Добавить запись в базу данных
# 5. Удалить запись из базы данных (по номеру в файле)
# 6. Поиск по одному полю
# 7. Поиск по двум полям

# инициализация базы данных
# def init_database(file_name):

# проверка введенного файла
# def cheak_file(file_name):

# вывод базы данных
# def print_database(file_name):

# Запрашивает значения для новой строки базы данных и записывает её
# def add_line_to_database(file_name):

# удаление строки из базы данных
# def del_line(file_name):

# ввод поля
# def enter():


# поиск по одному полю
# def find_by_one_field(file_name):

# поиск по двум полям
# def find_by_two_fields(file_name):

from cheak_func import *
from struct import *

string_format = '20sQ20sh20s'
string_len = 74

# инициализация базы данных
def init_database(file_name):
    if file_name == None:
        print("Файл для работы не был указан")
        return None
    try:
        file = open(file_name, 'wb')
        file.close()
        print("Файл успешно инициализирован")
        return file_name
    except:
        print("Файл не может быть открыт или создан")
        return None

# проверка введенного файла
def cheak_file(file_name):
	if file_name == None:
		print("Файл для работы не был указан")
		return "break"
	try:
		file = open(file_name, 'rb')
		
		file.seek(0, 2)
		pointer = file.tell()

		if pointer == 0:
			return "empty"
		
		if pointer % string_len != 0:

			print("Ошибка, это не база данных")
			file.close()
			return 'break'

		file.close()
		return "continue"
		
	except:
		print("Файл не может быть открыт или его не существует")
		return "break"

# вывод базы данных
def print_database(file_name):

	if cheak_file(file_name) == "break":
		return None
	if cheak_file(file_name) == "empty":
		print("Пустой файл")
		return None


	print('|' + '-'*104 + '|')
	print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format('Имя держателя карты', 'номер карты', 'срок действия', 'код CVV','банк'))
	print('|' + '-'*104 + '|')

	file = open(file_name, 'rb')

	file.seek(0, 2)
	size = file.tell()
	file.seek(0)

	for i in range(size // string_len):

		string = file.read(string_len)
		string = list(unpack(string_format, string))
		

		string[0] = string[0].decode('utf-8')
		string[0] = string[0].replace('\x00', '')

		string[2] = string[2].decode('utf-8')
		string[2] = string[2].replace('\x00', '')

		string[4] = string[4].decode('utf-8')
		string[4] = string[4].replace('\x00', '')

		
		print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(string[0], string[1], string[2], string[3], string[4]))
		print('|' + '-'*104 + '|')

	file.close()

# Запрашивает значения для новой строки базы данных и записывает её
def add_line_to_database(file_name):

	if cheak_file(file_name) == "break":
		return None

	name = input("Введите имя держателя карты: ")

	while len(name) >= 20:
		print("Ошибка ввода имени (до 20 символов)")
		name = input("Введите имя держателя карты: ")

	number = correct_input('Введите номер карты: ', "int+")
	number = str(number)
	while len(number) != 16:
		print("Ошибка ввода номера карты (16 цифр, это число, с 0 номер не начинается)")
		number = correct_input('Введите номер карты: ', "int+")
		number = str(number)
	number = int(number)

	date = input("Введите срок действия карты: ")

	while len(date) != 5:
		print("Ошибка ввода срока действия карты (5 символов: **/**)")
		date = input("Введите срок действия карты: ")

	cvv = correct_input('Введите CVV код карты: ', "int+")
	cvv = str(cvv)
	while len(cvv) != 3:
		print("Ошибка ввода CVV кода карты (3 цифры, это число, с 0 код не начинается)")
		cvv = correct_input('Введите CVV код карты: ', "int+")
		cvv = str(cvv)
	cvv = int(cvv)
		
	bank = input("Введите название банка: ")
	while len(bank) >= 20:
		print("Ошибка ввода названия банка (до 20 символов)")
		bank = input("Введите название банка: ")
	
	string = pack(string_format, name.encode('utf-8'), number, date.encode('utf-8'), cvv, bank.encode('utf-8'))
	
	file = open(file_name, 'ab')
	file.write(string)
	print("Данные успешно добавлены")
	file.close()

# удаление строки из базы данных
def del_line(file_name):

	if cheak_file(file_name) == "break":
		return None
	if cheak_file(file_name) == "empty":
		print("Пустой файл")
		return None

	n = correct_input("Введите номер нужной строки: ", "int+")

	file = open(file_name, 'rb+')

	file.seek(0, 2)
	size = file.tell()

	while n > (size // string_len):
		print('Нет строки под данным номером, попробуйте ещё раз')
		n = correct_input("Введите номер нужной строки: ", "int+")


	
	n -= 1
	file.seek(0,2)
	size = file.tell()
	pointer = n * string_len
	

	while pointer + string_len < size:
		file.seek(pointer + string_len)
		temp = file.read(string_len)
		file.seek(pointer)
		file.write(temp)
		pointer += string_len
	file.truncate(size - string_len)
	file.close()

# ввод поля
def enter():
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
		value = int(value)
	elif field == 3:

		value = input("Введите срок действия карты: ")
		while len(value) != 5:
			print("Ошибка ввода срока действия карты")
			value = input("Введите срок действия карты: ")

	elif field == 4:

		value = correct_input('Введите CVV код карты: ', "int+")
		value = str(value)
		while len(value) != 3:
			print("Ошибка ввода CVV кода карты")
			value = correct_input('Введите CVV код карты: ', "int+")
			value = str(value)
		value = int(value)

	elif field == 5:

		value = input("Введите название банка: ")
		while len(value) >= 20:
			print("Ошибка ввода названия банка")
			value = input("Введите название банка: ")

	return field, value

# поиск по одному полю
def find_by_one_field(file_name):

	if cheak_file(file_name) == "break":
		return None
	if cheak_file(file_name) == "empty":
		print("Пустой файл")
		return None

	field, value = enter()

	print('|' + '-'*104 + '|')
	print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format('Имя держателя карты', 'номер карты', 'срок действия', 'код CVV','банк'))
	print('|' + '-'*104 + '|')

	file = open(file_name, 'rb')

	NO = True

	file.seek(0, 2)
	size = file.tell()
	file.seek(0)

	for i in range(size // string_len):

		string = file.read(string_len)
		string = list(unpack(string_format, string))
		
		if (field - 1) % 2 == 0:
			string[field - 1] = string[field - 1].decode('utf-8')
			string[field - 1] = string[field - 1].replace('\x00', '')

		if string[field - 1] == value:

			for i in range(0, 5, 2):
				if i != field - 1:
					string[i] = string[i].decode('utf-8')
					string[i] = string[i].replace('\x00', '')

			print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(string[0], string[1], string[2], string[3], string[4]))
			print('|' + '-'*104 + '|')
			NO = False
	if NO:
		print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format('нет данных', 'нет данных', 'нет данных', 'нет данных','нет данных'))
		print('|' + '-'*104 + '|')
	file.close()

# поиск по двум полям
def find_by_two_fields(file_name):
	
	if cheak_file(file_name) == "break":
		return None
	if cheak_file(file_name) == "empty":
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

	file = open(file_name, 'rb')

	NO = True

	file.seek(0, 2)
	size = file.tell()
	file.seek(0)

	for i in range(size // string_len):

		string = file.read(string_len)
		string = list(unpack(string_format, string))
		
		if (field1 - 1) % 2 == 0:
			string[field1 - 1] = string[field1 - 1].decode('utf-8')
			string[field1 - 1] = string[field1 - 1].replace('\x00', '')

		if (field2 - 1) % 2 == 0:
			string[field2 - 1] = string[field2 - 1].decode('utf-8')
			string[field2 - 1] = string[field2 - 1].replace('\x00', '')

		if string[field1 - 1] == value1 and string[field2 - 1] == value2:

			for i in range(0, 5, 2):
				if i != field1 - 1 and i != field2 - 1:
					string[i] = string[i].decode('utf-8')
					string[i] = string[i].replace('\x00', '')

			print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(string[0], string[1], string[2], string[3], string[4]))
			print('|' + '-'*104 + '|')
			NO = False
	if NO:
		print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format('нет данных', 'нет данных', 'нет данных', 'нет данных','нет данных'))
		print('|' + '-'*104 + '|')
	file.close()


def main():

	file_name = None
	print("База данных банковских карт")

	while True:
		
		input_text = '(Для вывода меню введите 8). Введите номер функции: '
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

			del_line(file_name)

		elif func == 6:

			find_by_one_field(file_name)

		elif func == 7:

			find_by_two_fields(file_name)

		elif func == 8:
			 # вывод меню
		    print('------------------------------------------------------------------------------------------------')
		    print('Меню:')
		    print('1. Выбрать файл для работы')
		    print('2. Инициализировать базу данных')
		    print('3. Вывести содержимое базы данных')
		    print('4. Добавить запись в базу данных')
		    print('5. Удалить запись из базы данных (по номеру в файле)')
		    print('6. Поиск по одному полю')
		    print('7. Поиск по двум полям')
		    print('8. Вывод меню')
		    print('9. Завершение программы')
		    print('------------------------------------------------------------------------------------------------')
		elif func == 9:
			
			break
			
		else:
		    print('Ошибка, нет такой функции')

main()


