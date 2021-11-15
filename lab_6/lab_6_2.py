

def cheak_int(lst):
	l = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	lst = list(lst)
	flag = True
	for i in lst:
		if i not in l or (lst[0] == '0' and len(lst) > 1):
			flag = False
	return flag

def cheak_float(lst):
	l = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', 'e', '-', '+']
	lst = list(lst)
	flag = True
	
	if lst.count('e') > 1 or lst.count('.') > 1:
		flag = False
		

	elif 'e' in lst and  not (lst[lst.index('e') + 1] == '-' or lst[lst.index('e') + 1] == '+'):
		flag = False
	elif 'e' in lst and lst.index('e') == 0:
		flag = False
		
	else:
		for i in lst:
			if i not in l or (lst[0] == '0' and len(lst) > 1):
				flag = False
				
	return flag




def func_1(l):
	lst = input('Введите количество элементов списка: ')
	if cheak_int(lst) == True:
		n = int(lst)

	else:
		print('Ошибка, введите целое число')
		l = func_1((l))
		return l

	l = []

	if n < 1:
		print('Ошибка, отрицательное количество элементов')
		l = func_1(l)
		return l 
	if n == 0:
		print('Список: {}'.format(l))
		return l
	
	
	print('y = 1 + x^2/2! + x^4/4! + ... + x^(2n)/(2n)! + ...')
	lst = input('Введите значение аргумента: ')
	if cheak_float(lst) == True:
		x = float(lst)
	else:
		
		print('Ошибка, введите число')
		l = func_1((l))
		return l

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
	lst = input('Введите количество элементов списка: ')
	if cheak_int(lst) == True:
		n = int(lst)

	else:
		print('Ошибка, введите целое число')
		l = func_2(l)
		return l

	l = [0] * n
	for i in range(n):

		lst = input('Введите {}-й элемент списка: '.format(i+1))
		if cheak_float(lst) == True:
			l[i] = float(lst)
		else:
			
			print('Ошибка, введите число')
			l = func_2(l)
			return l

	print('Список: {}'.format(l))

	return l

def func_3(l):

	lst = input('Введите нужный номер элемента в списке: ')
	if cheak_int(lst) == True:
		k = int(lst)

	else:
		print('Ошибка, введите целое число')
		l = func_3(l)
		return l


	
	if k > len(l) or k < 0:
		print('Ошибка, под данным номером нет элемента в списке')
		l = func_3(l)
		return l

	lst = input('Введите значание числа, которое нужно вставить в нужное место в списке: ')
	if cheak_float(lst) == True:
		n = float(lst)
	else:
		
		print('Ошибка, введите число')
		l = func_3(l)
		return l


	l.insert(k - 1, n)

	print('Список: {}'.format(l))
	return l 

def func_4(l):
	if len(l) == 0:
		print('Ошибка, нет элементов в списке')
		return l

	lst = input('Введите нужный номер элемента в списке: ')
	if cheak_int(lst) == True:
		k = int(lst)

	else:
		print('Ошибка, введите целое число')
		l = func_4(l)
		return l
	
	if k > len(l):
		print('Ошибка, под данным номером нет элемента в списке')
		l = func_4(l)
		return l
	k -= 1
	l.pop(k)

	print('Список: {}'.format(l))
	return l 

def func_5(l):
	l = list()
	print('Список пуст')
	return l

def func_6(l):
	k = int(input('Введите номер экстремума: '))
	if k <= 0:
		print('Ошибка, номер экстремума не может быть отрицательным или равным 0')
		l = func_6(l)
		return l
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
	

	for i in range(i+1, len(l)):
		if l[i - 1] > l[i] and l[i - 1] == int(l[i - 1]) and l[i - 1] % 2 == 0 and \
		l[i] == int(l[i]) and l[i] % 2 == 0:
			l_temp.append(l[i])
			if len(l_temp) > len(l_mx):
				l_mx = l_temp

		
		else:
			l_temp = [l[i]]
	
	print('Список: {}'.format(l_mx))		
	return l_mx






 
def main():
	l = list()
	while True:
		print('Меню:')
		print('1 - Проинициализировать список первыми N элементами заданного в л/р 5 ряда')
		print('2 - Очистить список и ввести его с клавиатуры')
		print('3 - Добавить элемент в произвольное место списка')
		print('4 - Удалить произвольный элемент из списка (по номеру)')
		print('5 - Очистить список')
		print('6 - Найти значение K-го экстремума в списке')
		print('7 - Убывающая последовательность целых чётных чисел')
		print('0 - Завершение программы')

		lst = input('Введите номер функции: ')
		if cheak_int(lst) == True:
			f = int(lst)

		else:
			print('Ошибка, введите целое число')
			continue
		
		
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




