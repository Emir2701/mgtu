from cheak_func import *

def main():
	
	print('Условие:')
	print('-'*78)
	print('6. \nЗадана матрица D и массив I, содержащий номера строк, для которых \n\
необходимо определить максимальный элемент. Значения максимальных элементов\n\
запомнить в массиве R. Определить среднее арифметическое вычисленных максимальных значений. \n\
Напечатать матрицу D, массивы I и R, среднее арифметическое значение.')
	print('-'*78)

	n_str = correct_input('Введите количество строк матрицы D: ', 'int+')
	n_col = correct_input('Введите количество столбцов матрицы D: ', 'int+')

	matrix_D = [[0]*n_col for i in range(n_str)]
	
	for i in range(n_str):
		for j in range(n_col):
			matrix_D[i][j] = correct_input('Введите {}-ый элемент {}-й строки матрицы D: '.format(j + 1, i + 1), 'float')
	while True:
		n = correct_input('Введите количество элементов массива I: ', 'int+')
		if n <= n_str:
			break
		else:
			print('количество элементов массива I больше числа строк в матрице D')

	list_I = [0] * n 

	for i in range(n):
		while True:
			list_I[i] = correct_input('Введите {}-ый номер строки, для которой \
необходимо определить максимальный элемент: '.format(i + 1), 'int+')
			
			if list_I[i] <= n_str and list_I.count(list_I[i]) == 1:
				break
			else:
				print('нет строки матрицы D под данным номером или данный номер строки был введен ранее')

	list_I = list(set(list_I))

	list_R = []

	for i in range(n_str):
		if i + 1 in list_I:
			list_R.append(max(matrix_D[i]))

	av = sum(list_R)/len(list_R)

	print('Матрица D:')

	for i in range(n_str):
		for j in range(n_col):
			print('{:<10}'.format(matrix_D[i][j]), end=' ')
		print()

	print('Массив I:')
	print(*list_I)


	print('Массив R:')
	print(*list_R)

	print('среднее арифметическое вычисленных максимальных значений:')
	print(av)

if __name__ == '__main__':
	main()