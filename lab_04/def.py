import math as m

start_f = float(input('Введите начальное значение аргумента: '))
end_f = float(input('Введите конечное значение аргумента: '))
step_f = float(input('Введите шаг: '))

min_f = float('inf')
max_f = float('-inf')

eps = 1e-8

x = start_f

while x < end_f + eps:
	y = m.cos(x)
	if y < min_f:
		min_f = y
	if y > max_f:
		max_f = y
	x += step_f


width = 150
dist = max_f - min_f 

min_pos = min(0, int(min_f))

dist_0 = int(width / dist * abs( min_f))

x = start_f

while x < end_f + eps:
	str_x = '{:.2}'.format(x)
	y = m.cos(x)
	print(str_x, ' ' * (9 - len(str_x)), '|', end='', sep='')
	if y > 0:
		if min_f < 0:
			print(' '*dist_0, '|', end='', sep ='')
			print(' '*(int(width / dist * y)-1), '*',sep='')
		else:
			print(' '*(int(width / dist*(y - min_f))-1), '*',sep='')
	else:
		if abs(dist_0 - int(width / dist * abs(y - min_f))) < eps:
			print(' '* dist_0, '*', sep='')
		else:
			print(' '*(int(width/dist*abs(y-min_f))),'*',end='',sep='')
			print(' '*(dist_0 - int(width / dist * abs(y - min_f))-1),'|',sep='')
	x += step_f

