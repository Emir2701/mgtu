# Шимшир Эмирждан ИУ7-13Б
'''

Программа для вычисления приближённого значения интеграла 
двумя разными методами: метод трапеций и метод парабол.

# Данные, принимаемые на вход программой:
# start – начальное значение функции
# end – конечное значение функции
# n1 – первое количество участков разбиения
# n2 – второе количество участков разбиения
# eps – значение точности

# Переменные для вычислений:
# s_t_1, s_t_2, s_p_1, s_p_2 – вычисление инеграла методом трапеций (n1, n2) и методом парабол (n1, n2)
# not_err – вычисление интеграла с помощью известной первообразной
# abs_err_m(номер метода)_(номер разбиения)  – вычисление абсолютной погрешности
# relative_err_m(номер метода)_(номер разбиения) – вычисление относительной погрешности
# less_good – менее точный метод
# count – количество разбиений для менее точного метода

'''
import math

def func(x):
	return x**2

def integral(x):
	return x**3/3

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
	text = text.lower()
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

# метод трапеций
def trap(start, end, n):

	dx = (end - start)/n 
	summ = 0
	x_start = start
	while x_start < end:
		summ += ((func(x_start) + func(x_start + dx))/2) * dx
		x_start += dx
	
	return summ

# метод парабол
def parab(start, end, n):
	dx = (end - start)/n 
	summ = 0
	x_start = start
	while x_start < end:
		summ += ((func(x_start) + 4*func(x_start + dx) + func(x_start + 2*dx))/6) * 2*dx
		x_start += 2 * dx
	
	return summ

print('-' * 55)
print('Программа для вычисления приближённого значения интеграла \n\
двумя разными методами: метод трапеций и метод парабол.')
print('-' * 55)

# Ввод данных
start = correct_input('Введите начало отрезка: ', 'float')
end = correct_input('Введите конец отрезка: ', 'float')

while end <= start:
	print('Ошибка, конечное значение должно быть больше начального.')
	end = correct_input('Введите конец отрезка: ', 'float')

n1 = correct_input('Введите количество участков разбиения: ', "int+")
n2 = correct_input('Введите количество участков разбиения: ', "int+")

# Вычисление интегралов разными методами
s_t_1 = trap(start, end, n1)
s_t_2 = trap(start, end, n2)
s_p_1 = parab(start, end, n1)
s_p_2 = parab(start, end, n2)

print('-' * 55)
print('|', ' ' * 27, '| {: <10.4}| {: <10.4}|'.format(float(n1), float(n2)))
print('-' * 55)
print('| Метод трапеций              |', '{: <10.4}|'.format(s_t_1), '{: <10.4}|'.format(s_t_2))
print('-' * 55)
if n1 % 2 != 0 and n2 % 2 != 0:
	print('| Метод парабол               |', '{: ^10.4}|'.format('---'), '{: ^10.4}|'.format('---'))
elif n1 % 2!= 0:
	print('| Метод парабол               |', '{: ^10.4}|'.format('---'), '{: <10.4}|'.format(s_p_2))
elif n2 % 2 != 0:
	print('| Метод парабол               |', '{: <10.4}|'.format(s_p_1), '{: ^10.4}|'.format('---'))
else:
	print('| Метод парабол               |', '{: <10.4}|'.format(s_p_1), '{: <10.4}|'.format(s_p_2))
print('-' * 55)

# Вычисление интеграла с помощью известной первообразной
not_err = integral(end) - integral(start)

# Вычисление абсолютной погрешности
abs_err_s_t_1 = abs(not_err - s_t_1)
abs_err_s_t_2 = abs(not_err - s_t_2)

abs_err_s_p_1 = abs(not_err - s_p_1)

abs_err_s_p_2 = abs(not_err - s_p_2)

print('Абсолютная погрешность метода трапеций при разбиении на {:} участка: {: <10.4}'.format(n1, abs_err_s_t_1))
print('Абсолютная погрешность метода трапеций при разбиении на {:} участка: {: <10.4}'.format(n2, abs_err_s_t_2))
if n1 % 2 == 0:
	print('Абсолютная погрешность метода парабол при разбиении на {:} участка: {: <10.4}'.format(n1, abs_err_s_p_1))
if n2 % 2 == 0:
	print('Абсолютная погрешность метода парабол при разбиении на {:} участка: {: <10.4}'.format(n2, abs_err_s_p_2))
print()

# Вычисление относительной погрешности
relative_err_s_t_1 = abs_err_s_t_1 / abs(not_err) * 100
relative_err_s_t_2 = abs_err_s_t_2 / abs(not_err) * 100

relative_err_s_p_1 = abs_err_s_p_1 / abs(not_err) * 100

relative_err_s_p_2 = abs_err_s_p_2 / abs(not_err) * 100

print('Относительная погрешность метода трапеций при разбиении на {:} участка: {: <10.4}'.format(n1, relative_err_s_t_1))
print('Относительная погрешность метода трапеций при разбиении на {:} участка: {: <10.4}'.format(n2, relative_err_s_t_2))
if n1 % 2 == 0:
	print('Относительная погрешность метода парабол при разбиении на {:} участка: {: <10.4}'.format(n1, relative_err_s_p_1))
if n2 % 2 == 0:
	print('Относительная погрешность метода парабол при разбиении на {:} участка: {: <10.4}'.format(n2, relative_err_s_p_2))

less_good = ''
# Определение наиболее точного метода


if n1 % 2 != 0 and n2 % 2 != 0:
	print('Методы невозможно сравнить, потому что при таких разбиениях метод парабол не работает.')
else:
	if n1 % 2 == 0:
		m = abs_err_s_p_1
		count = n1
	else:
		m = abs_err_s_p_2
		count = n2

	if abs_err_s_t_1 < m:
		less_good = 'парабол'
		method = parab
		print('Mетод трапеций точнее метода парабол.')

	else:
		less_good = 'трапеций'
		method = trap
		print('Метод парабол точнее метода трапеций.')

	eps = correct_input('Введите точность, с которой нужно вычислить интеграл: ', 'float')

	
	while not abs(method(start, end, count) - method(start, end, 2 * count)) < eps:
	    count *= 2

	print('Интеграл по методу', less_good, 'будет вычеслен с заданной точностью, если количество участков разбиения будет равно: ', count)
	print('Значение при данном разбиении: {:.4}'.format(method(start, end, count)))




