'''
Защита 9
Дана прямоугольная матрица целых чисел. Отсортировать по возрастанию все элементы (лентой).

например:
9 2
1 4
выход:
1 2
4 9 
'''

n_str = int(input('Введите количество строк: '))
n_col = int(input('Введите количество столбцов: '))

matrix = []
array = []

for i in range(n_str):
	matrix.append([])
	for j in range(n_col):

		elem = int(input('Введите {}-ый символ {}-й строки матрицы D: '.format(j + 1, i + 1)))

		array.append(elem)
		matrix[i].append(elem)

array.sort()
print(array)

for i in range(n_str):
	for j in range(n_col):
		matrix[i][j] = array[j + n_col*i]

for i in matrix:
	print(*i)




