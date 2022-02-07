import math as m

x_0 = float(input('Введите начальное значение: '))
x_n = float(input('Введите конечное значение: '))
h = float(input('Введите шаг: '))

i = x_0
eps = h/2

y_mx = float('-inf')
y_mn = float('+inf')

while i < x_n + eps:
	y = m.cos(i)

	if y > y_mx:
		y_mx = y
	if y < y_mn:
		y_mn = y
	i += h



width = 160

i = x_0

ox = int(width/(y_mx - y_mn) * (0 - y_mn) - 1) + 11



while i < x_n + eps:
	y = m.cos(i)

	k = width - 9 - int(width/(y_mx - y_mn) * (y - y_mn) - 1) 
	if y_mn <= 0 <= y_mx:

		

		s = '{:!<9.4}|'.format(i) + int(width/(y_mx - y_mn) * (y - y_mn) - 1)*' ' + '*' + k*' '
		if s[ox] != '*':
			s = s[:ox] + '|' + s[ox + 1:]

	else:
		

		s = '{:!<9.4}|'.format(i) + int(width/(y_mx - y_mn) * (y - y_mn) - 1)*' ' + '*'

	print(s)
	i += h
