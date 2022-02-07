# Шимшир Эмирджан Османович ИУ7-13Б


def func_1(l):
	n = int(input('Введите количество эелементов списка: '))
	print('y = 1 + x^2/2! + x^4/4! + ... + x^(2n)/(2n)! + ...')
	x = float(input('Введите значение аргумента: '))
	element = 1
	l = []
	l.append(element)
	for i in range(1, n):
		element *= x**2/(2*i*(2*i - 1))
		l.append(round(element, 4))
	print('Список: {}'.format(l))
	return l

def func_2(l):
	print('Список очищен')
	l = list(map(float, input('Введите элементы списка через пробел: ').split()))
	print('Список: {}'.format(l))

	return l

def func_3(l):

	
	k = int(input('Введите нужный номер элемента в списке: '))
	
	if k > 0:
		k -= 1

	if k > len(l):
		print('Ошибка, под данным номером нет элемента в списке')
		return l

	n = float(input('Введите значание числа, которое нужно вставить в нужное место в списке: '))

	l.isert(k, n)

	print('Список: {}'.format(l))
	return l 

def func_4(l):

	k = int(input('Введите нужный номер элемента в списке: '))
	if k > len(l):
		print('Ошибка, под данным номером нет элемента в списке')
		return l
	k -= 1
	l.pop(k)
	print('Список: {}'.format(l))
	return l 

def func_5(l):
	l = list()
	print('Список пуст')
	return l

def main():
	l = list()
	while True:
		print('Функции:')
		print('1 - Проинициализировать список первыми N элементами заданного в л/р 5 ряда')
		print('2 - Очистить список и ввести его с клавиатуры')
		print('3 - Добавить элемент в произвольное место списка')
		print('4 - Удалить произвольный элемент из списка (по номеру)')
		print('5 - Очистить список')
		f = int(input('Введите номер функции: '))
		
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


main()




