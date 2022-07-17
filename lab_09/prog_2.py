# Шимшир Эмирждан ИУ7-13Б

# Программа предназначена поиска максимального элемента над главной диагональю и минимального под побочной 

# Данные, принимаемые на вход программой:
# n – количество строк и столбцов в квадратной матрице

# Переменные для вычислений:
# matrix – матрица
# max_up_main – максимальный текущий элемент
# min_down_not_main – минимальный текущий элемент

from cheak_func import *
	
def main():

	#------------------------------------------------------------------------------------------------
	print('Условие:')
	print('-'*78)
	print('2. \nНайти максимальное значение над главной диагональю \n\
и минимальное - под побочной диагональю.')
	print('-'*78)
	n = correct_input('Введите размерность квадратной матрицы: ', 'int+')
	#------------------------------------------------------------------------------------------------


	# Заполнение квадратной матрицы
	matrix = [[0]*n for i in range(n)]

	for i in range(n):
		for j in range(n):
			matrix[i][j] = correct_input('Введите {}-ый элемент {}-й строки: '.format(j + 1, i + 1), 'float')

	# Вывод матрицы
	for i in range(n):
		for j in range(n):
			print('{:<10.4}'.format(matrix[i][j]),end=' ')
		print()
	# Обработка исключения
	if n == 1:
		print('В матрице 1 элемент')
		return 0 

	# Поиск максимального элемента над главной диагональю и минимального под побочной

	max_up_main = matrix[0][1]
	min_down_not_main = matrix[1][n-1]

	for i in range(n):
		for j in range(i + 1, n):
			
			if max_up_main < matrix[i][j]:
				max_up_main = matrix[i][j]

	for i in range(n):
		for j in range(n-1, n-1 - i, -1):
			
			if min_down_not_main > matrix[i][j]:
				min_down_not_main = matrix[i][j]

	print('Максимум над главной диагональю: {}'.format(max_up_main))
	print('Минимум под побочной диагональю: {}'.format(min_down_not_main))



if __name__ == '__main__':
	main()