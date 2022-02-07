# y = x**6 - 2 * x**5 + 1.7 * x**4 - 4.7 * x**3 - 0.8 * x**2 + 4.26 * x - 2

# x_0 = -1.1
# h = 0.1
# x_n = 1.2

scale = -1

while not 4 <= scale <= 8:
	scale = int(input('Введите количество засечек: '))
	if 4 <= scale <= 8:
		break
	else:
		print('Ошибка')

print('scale = {}'.format(scale))

print(20*'-')
print('|{: ^7} | {: ^7} |'.format('x', 'y'))
print(20*'-')


x_0 = -1.1
h = 0.1
x_n = 1.2
eps = 1e-8
list_x = []
list_y = []
i = x_0
while i <= x_n:
	
	y = i**6 - 2 * i**5 + 1.7 * i**4 - 4.7 * i**3 - 0.8 * i**2 + 4.26 * i - 2

	list_y.append(round(y, 4))
	list_x.append(round(i, 4))

	if abs(i) < eps:
		print('|  {: <6.4}| {: <7.4} |'.format(0.0, y))
	else:
		print('|  {: <6.4}| {: <7.4} |'.format(i, y))
	i += h

print(20*'-')

print(list_y)
print(list_x)
s = 6*' '

width = 80

j = (width - scale * 7)/(scale - 1)

y_0 = x_0**6 - 2 * x_0**5 + 1.7 * x_0**4 - 4.7 * x_0**3 - 0.8 * x_0**2 + 4.26 * x_0 - 2
y_n = x_n**6 - 2 * x_n**5 + 1.7 * x_n**4 - 4.7 * x_n**3 - 0.8 * x_n**2 + 4.26 * x_n - 2

delta = (y_0- y_n)/(scale - 1)

n = 0
i = x_0

while n < scale:
	
	s += '{:^7.4}'.format(y) + int(j)*' '
	y += delta 
	n += 1

print(s)
i = x_0 

while i <= 1.2:
	if abs(i) < eps:
		print('{:<5.4}|'.format(0.0))
	else:
		print('{:<5.4}|'.format(i))
	i += h

