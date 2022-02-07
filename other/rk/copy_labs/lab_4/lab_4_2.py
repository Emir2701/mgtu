# y = x**6 - 2 * x**5 + 1.7 * x**4 - 4.7 * x**3 - 0.8 * x**2 + 4.26 * x - 2

x_0 = float(input('Введите x_0: '))
x_n = float(input('Введите x_n: '))
h = float(input('Введите h: '))

eps = 1e-8
scale = 0
width = 160
list_x = []
list_y = []

while not 4 <= scale <= 8:
	scale = int(input('Введите количество засечек: '))
	if 4 <= scale <= 8:
		break
	else:
		print('Ошибка')


print(22*'-')
print('|{: ^7} | {: ^9} |'.format('x', 'y'))
print(22*'-')


i = x_0

while i < x_n + eps:
	
	y = i**6 - 2 * i**5 + 1.7 * i**4 - 4.7 * i**3 - 0.8 * i**2 + 4.26 * i - 2

	list_y.append(round(y, 4))
	list_x.append(round(i, 4))

	if abs(i) < eps:
		print('|  {: <6.4}| {: <9.4} |'.format(0.0, y))
	else:
		print('|  {: <6.4}| {: <9.4} |'.format(i, y))
	i += h


print(22*'-')



y_mn = min(list_y)
y_mx = max(list_y)

x_mn = min(list_x)
x_mx = max(list_x)

i = 0
j = (width - scale * 9)/(scale - 1)

delta = (y_mx - y_mn)/(scale - 1)

s = 8*' '

y = y_mn

while i < scale:
	if i == scale - 1:
		s += '{: <9.4}'.format(y)
	elif i == scale - 2:
		s += '{: <9.4}'.format(y) +  int(j)*' ' + (width - ((int(j)*(scale - 1)) + 9*scale))*' '
	else:
		s += '{: <9.4}'.format(y) + int(j)*' '
		
	y += delta
	i += 1
print(s)
print(len(s))
i = 0



ox = 9 + (int(width/(y_mx - y_mn) * (0 - y_mn)) - 1)

while i < len(list_x):
	y = list_x[i]**6 - 2 * list_x[i]**5 + 1.7 * list_x[i]**4 - 4.7 * list_x[i]**3 - 0.8 * list_x[i]**2 + 4.26 * list_x[i] - 2
	if y_mn <= 0 <= y_mx:
		a = (width - 8 - (int(width/(y_mx - y_mn) * (y - y_mn)) - 1))
		r = '{:<7.4}|'.format(list_x[i]) + (int(width/(y_mx - y_mn) * (y - y_mn)) - 1)*' ' + '*' + a*' '
		if r[ox] != '*':
			r = r[:ox] + '|' + r[ox + 1:]

		print(r)
		#print(len(r))
		
	else:
		print('{:<7.4}|'.format(list_x[i]) + (int(width/(y_mx - y_mn) * (y - y_mn)) - 1)*' ' + '*')
	#print('{:<5.4}|'.format(list_x[i]) + int(width/(y_mx - y_mn) * abs(y_mn) - 1)*' ' + '|' )
	#print('{:<7.4}|'.format(list_x[i]) + int(width/(y_mx - y_mn) * (y - y_mn))*' ' + '*')
	i += 1
	