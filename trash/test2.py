# Шимшир Эмирджан Османович ИУ7-13Б

# Программа для заданной функции:

# y = x**6 - 2 * x**5 + 1.7 * x**4 - 4.7 * x**3 - 0.8 * x**2 + 4.26 * x - 2

# Выводит таблицу значений на некотором отрезке и строит ее график
# Также программа выводит сумму и произведение вычисленных значений функции y

# Наименование переменных:

# Данные, принимаемые на вход:
# x_0 - начальное значение исследуемого отрезка
# x_n - конечное значение исследуемого отрезка
# h - шаг отрезка
# scale - количество засечек

# Переменные для вычислений:
# eps – эпсилон, с помощью которого можем сравнивать числа с плавающей точкой
# width - ширина экрана вывода графика функции 
# summ - сумма значений y
# mult - произведение значений y
# y_mn - минимальное значение y
# y_mx - максимальное значение y
# w_tabl - ширина экрана вывода таблицы значений
# i - счетчик циклов
# y - занчение функции при текущем i в цикле
# delta - число, кторое нужно прибавить к предыдущей засечке, чтобы получить текущую
# s - строка с засечками
# k1 - коэффициент, при умножении на который получаем нужное количество пробелов до *
# k3 - количество пробелов между засечками
# ox - хранит количество пробелов до оси OX
# k2 - хранит количество пробелов, которое нужно вывести после звездочки для сохранения ширины экрана
# r - выременно хранит строчку со * и необходимое количество пробелов до и после нее

# Блок с объявлением констант

eps = 1e-8
width = 160
w_tabl = 22
summ = 0
mult = 1
y_mn = float('+inf')
y_mx = float('-inf')

# Блок ввода 

x_0 = float(input('Введите начальное значение: '))
x_n = float(input('Введите конечное значение: '))
h = float(input('Введите шаг: '))

if x_0 >= x_n or h <= 0 or h >= x_n - x_0:
	while True:
		print('Ошибка')
		x_0 = float(input('Введите x_0: '))
		x_n = float(input('Введите x_n: '))
		h = float(input('Введите h: '))
		if x_0 < x_n and h > 0 and h < x_n - x_0:
			break

scale = int(input('Введите количество засечек: '))

if not 4 <= scale <= 8:
	while True:
		print('Ошибка')
		scale = int(input('Введите количество засечек: '))
		if 4 <= scale <= 8:
			break

# Вывод шапки таблицы

print(w_tabl*'-')
print('|{: ^7} | {: ^9} |'.format('x', 'y'))
print(w_tabl*'-')

# Вывод заничений таблицы
i = x_0

while i < x_n + eps:
	
	y = i**2
	
	# Подсчет суммы и произведения значений функции
	summ += y
	mult *= y

	# Поиск минимального и максимального значений функции
	if y > y_mx:
		y_mx = y
	if y < y_mn:
		y_mn = y

	if abs(i) < eps: # проблемы с выводом 0 у вещественных чисел
		print('|  {: <6.4}| {: <9.4} |'.format(0.0, y))
	else:
		print('|  {: <6.4}| {: <9.4} |'.format(i, y))
	i += h

# Ввод нижней линии таблицы
print(w_tabl*'-')

# обновление счетчика цикла 
i = 0

# вычисление вспомогательных констант
delta = (y_mx - y_mn)/(scale - 1)
k1 = width/(y_mx - y_mn)
k3 = (width - scale * 9)/(scale - 1)
s = 8*' '

# объявление 1 засечки (минимальное значение функции)
y = y_mn

while i < scale:
	if i == scale - 1:
		s += '{: >9.4}'.format(y) # последнюю засечку выравниваем по правому краю
	elif i == scale - 2:
		# к предпоследней строчке прибавляем нужное количестро пробелов
		s += '{: <9.4}'.format(y) +  int(k3)*' ' + (width - ((int(k3)*(scale - 1)) + 9*scale))*' ' 
	else:
		s += '{: <9.4}'.format(y) + int(k3)*' '

	# обновление значения засечки
	y += delta

	i += 1

# вывод засечек
print(s)

# обновление счетчика цикла
i = x_0


# расчет количества пробелов до оси OX
ox = 9 + (int(width/(y_mx - y_mn) * (0 - y_mn)) - 1)

# Вывод графика
while i < x_n + eps:

	y = i**2
	# расчет количества пробелов, которое нужно вывести после звездочки для сохранения ширины экрана
	k2 = (width - 8 - (int(width/(y_mx - y_mn) * (y - y_mn)) - 1))

	# вывод графика, пересекающего ocь X
	if y_mn <= 0 <= y_mx:
		
		if abs(i) < eps:
			r = '{:<7.4}|'.format(0.0) + (int(k1 * (y - y_mn)) - 1)*' ' + '*' + k2*' '
		else:
			r = '{:<7.4}|'.format(i) + (int(k1 * (y - y_mn)) - 1)*' ' + '*' + k2*' '
		if r[ox] != '*':
			r = r[:ox] + '|' + r[ox + 1:]

		print(r)
		
	# вывод графика, непересекающего ocь X
	else:
		if abs(i) < eps:
			print('{:<7.4}|'.format(0.0) + (int(k1 * (y - y_mn)) - 1)*' ' + '*' +  k2*' ')
		else:
			
			print('{:<7.4}|'.format(i) + (int(k1 * (y - y_mn)) - 1)*' ' + '*' +  k2*' ')

	i += h

# вывод суммы и произведения y
print('Сумма y: {:0.4f}'.format(summ))
print('Произведение y: {:0.4f}'.format(mult))