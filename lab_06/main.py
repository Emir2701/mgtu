'''
 Шимшир Эмирджан Османович ИУ7-13Б
# Вариант 1

Программа, которая позволит с использованием меню обеспечить работу с числовыми массивами:
1. Проинициализировать список первыми N элементами заданного в л/р 5 ряда
2. Очистить список и ввести его с клавиатуры
3. Добавить элемент в произвольное место списка
4. Удалить произвольный элемент из списка (по номеру)
5. Очистить список
6. Найти значение K-го экстремума в списке
7. Убывающая последовательность целых чётных чисел.

Описание функций:
correct_input - проверяет корректность ввода данных
cheak_int_plus - проверяет корректность ввода целых положительных чисел
cheak_int - проверяет корректность ввода целых чисел
cheak_float - проверяет корректность ввода вещественных чисел
func_1 - 1 функция в меню работы со списком
func_2 - 2 функция в меню работы со списком
func_3 - 3 функция в меню работы со списком
func_4 - 4 функция в меню работы со списком
func_5 - 5 функция в меню работы со списком
func_6 - 6 функция в меню работы со списком
func_7 - 7 функция в меню работы со списком
main - основной цикл программы

описание основных веременных:
l - основной список
input_text - введенные данные в виде строки
k - хранит нужный номер элемента в списке
flag - флаг для cheak_int cheak_float
x - аргумент для 1 функции
element - текущий элемент для 1 функции
f - номер функции

'''



# проверяет корректность ввода данных
def correct_input(input_text, type_number):
	text = input(input_text)
	while True:
		if type_number == 'int':
			if not cheak_int(text):
				print('Ошибка, введите целое число: ')
				text = input(input_text)
			else:
				return int(text)

		if type_number == 'float':
			if not cheak_float(text):
				print('Ошибка, введите действительное число: ')
				text = input(input_text)
			else:
				return float(text)
		if type_number == 'int+':
			if not cheak_int_plus(text):
				print('Ошибка, введите целое положительное число: ')
				text = input(input_text)
			else:
				return int(text)
# проверяет корректность ввода целых чисел
def cheak_int(text):
	flag = True
	cheak_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '+']
	text = list(text)
	for i in text:
		if i not in cheak_list:
			flag = False
			
	if len(text) == 0:
		flag = False
	elif (text[0] != '-' and text.count('-') == 1) or text.count('-') > 1 or (len(text) == 1 and text[0] == '-') \
	or (text[0] != '+' and text.count('+') == 1) or text.count('+') > 1 or (len(text) == 1 and text[0] == '+'):
		flag = False
	
	return flag
# проверяет корректность ввода целых положительных чисел
def cheak_int_plus(text):
	flag = True
	cheak_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	text = list(text)
	for i in text:
		if i not in cheak_list:
			flag = False
			
	if len(text) == 0:
		flag = False
	elif text[0] == '0':
		flag = False
	
	return flag
# проверяет корректность ввода вещественных чисел
def cheak_float(text):
	flag = True
	cheak_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', 'e', '-', '+']
	text = list(text)
	

	for i in text:
		if i not in cheak_list:
			flag = False
	if len(text) == 0:
		flag = False
	elif text.count('-') > 1 and 'e' not in text or text.count('+') > 1 and 'e' not in text\
	or len(text) == 1 and text[0] == '-' or (len(text) == 1 and text[0] == '+'):
		flag = False

	elif (text[0] == '.' and text.count('.') == 1) or (text[0] == 'e' and text.count('e') == 1) or text.count('e') > 1 or text.count('.') > 1 \
	or 'e' in text and cheak_int(''.join(text[text.index('e') + 1:])) == False:
		
		flag = False

	

	return flag




def func_1(l):

	# Проверка входных данных
	# -----------------------------------------
	input_text = 'Введите количество элементов списка: '
	n = correct_input(input_text, 'int+')
	# -----------------------------------------
	
	print('y = 1 + x^2/2! + x^4/4! + ... + x^(2n)/(2n)! + ...')

	# Проверка входных данных
	# -----------------------------------------
	input_text = 'Введите значение аргумента: '
	x = correct_input(input_text, 'float')
	# -----------------------------------------

	# расчет нужных членов ряда
	element = 1
	l.append(element)
	for i in range(1, n):
		element *= x**2/(2*i*(2*i - 1))
		l.append(round(element, 4))
	print('Список: {}'.format(l))

	return l

def func_2(l):
	l = []
	print('Список очищен')
	# Проверка входных данных
	# -----------------------------------------
	input_text = 'Введите количество элементов списка: '
	n = correct_input(input_text, 'int+')
	# -----------------------------------------
	
	l = [0] * n

	# Проверка входных данных
	# -----------------------------------------
	for i in range(n):
		input_text = 'Введите {}-й элемент списка: '.format(i+1)
		l[i] = correct_input(input_text, 'float')
	# -----------------------------------------

	print('Список: {}'.format(l))

	return l

def func_3(l):
	
	# Проверка входных данных
	# -----------------------------------------
	input_text = 'Введите нужный номер элемента в списке: '
	k = correct_input(input_text, 'int+')

	if k > len(l) or k < 0:
		print('Ошибка, под данным номером нет элемента в списке')
		l = func_3(l)
		return l
	# -----------------------------------------
	
	# Проверка входных данных
	# -----------------------------------------
	input_text = 'Введите значание числа, которое нужно вставить в нужное место в списке: '
	n = correct_input(input_text, 'float')
	
	# -----------------------------------------

	# вставка
	l.insert(k - 1, n)

	print('Список: {}'.format(l))
	return l 

def func_4(l):

	# Проверка входных данных
	# -----------------------------------------
	if len(l) == 0:
		print('Ошибка, нет элементов в списке')
		return l

	input_text = 'Введите нужный номер элемента в списке: '
	k = correct_input(input_text, 'int+')
	
	if k > len(l):
		print('Ошибка, под данным номером нет элемента в списке')
		l = func_4(l)
		return l

	# -----------------------------------------
	k -= 1
	# удаление элемента
	l.pop(k)

	print('Список: {}'.format(l))
	return l 

def func_5(l):
	# очищение списка
	l = list()
	print('Список пуст')
	return l

def func_6(l):

	# Проверка входных данных
	# -----------------------------------------
	input_text = 'Введите номер экстремума: '
	k = correct_input(input_text, 'int+')
	j = 0
	# -----------------------------------------
	j = 0
	for i in range(1, len(l) - 1):
		if l[i-1] < l[i] > l[i+1] or l[i-1] > l[i] < l[i+1]:
			j += 1
		if j == k:
			print('{} экстремум равен: {}'.format(k, l[i]))

			return l 
	
	print('Нет {} экстремума'.format(k))
	return l

def func_7(l):
	l_c = list()
	l_c = l.copy()
	# Проверка входных данных
	# -----------------------------------------
	if len(l) == 0:
		print('Нет элементов в списке')
		return l
	for i in range(len(l)):
	
		if l[i] % 2 == 0:
			l_temp = [l[i]]
			l_mx = l_temp
			break
	else:
		print('Нет четных чисел')
		return l

	# -----------------------------------------

	for i in range(i+1, len(l)):
		if l[i - 1] > l[i] and l[i - 1] == int(l[i - 1]) and l[i - 1] % 2 == 0 and \
		l[i] == int(l[i]) and l[i] % 2 == 0:
			l_temp.append(l[i])
			if len(l_temp) > len(l_mx):
				l_mx = l_temp

		
		else:
			l_temp = [l[i]]
	
	print('Список: {}'.format(l_mx))		
	return l_c






 
def main():
	l = list()
	while True:
		# вывод меню
		print('Меню:')
		print('1 - Проинициализировать список первыми N элементами заданного в л/р 5 ряда')
		print('2 - Очистить список и ввести его с клавиатуры')
		print('3 - Добавить элемент в произвольное место списка')
		print('4 - Удалить произвольный элемент из списка (по номеру)')
		print('5 - Очистить список')
		print('6 - Найти значение K-го экстремума в списке')
		print('7 - Убывающая последовательность целых чётных чисел')
		print('0 - Завершение программы')
		

		input_text = 'Введите номер функции: '
		f = correct_input(input_text, 'int')
		
		
		
		if f == 1:
			l = func_1(l)
		elif f == 2:
			l = func_2(l)
		elif f == 3:
			l = func_3(l)
		elif f == 4:
			l = func_4(l)
		elif f == 5:
			l = func_5(l)
		elif f == 6:
			l = func_6(l)
		elif f == 7:
			l = func_7(l)
		elif f == 0:
			break
		else:
			print('Ошибка, нет такой функции')


main()
