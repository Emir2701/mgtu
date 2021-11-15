import math as m

x_0 = float(input())
x_n = float(input())
h = float(input())


eps = h/2

y_mn = float('+inf')
y_mx = float('-inf')


i = x_0

while i < x_n + eps:
	y = abs(i) - 1

	if y > y_mx:
		y_mx = y

	if y < y_mn:
		y_mn = y


	i += h

width = 160



print(y_mx, y_mn)
ox = int(width/(y_mx - y_mn) * (0 - y_mn) - 1) + 10


i = x_0

while i < x_n +eps:
	y = abs(i) - 1
	
	if y_mn < 0 < y_mx:

		if abs(i) < eps:
			r = '{: <8.4}|'.format(0.0) + int(width/(y_mx - y_mn) * (y - y_mn) - 1)*' ' + '*' 
			r += (width - len(r))*' '
		else:
			r = '{: <8.4}|'.format(i) + int(width/(y_mx - y_mn) * (y - y_mn) - 1)*' ' + '*' 
			r += (width - len(r))*' '
		if r[ox] != '*':
			r = r[:ox] + '|' + r[ox + 1:]
	else:
		if abs(i) < eps:
			r = '{: <8.4}|'.format(0.0) + int(width/(y_mx - y_mn) * (y - y_mn) - 1)*' ' + '*' 
			
		else:
			r = '{: <8.4}|'.format(i) + int(width/(y_mx - y_mn) * (y - y_mn) - 1)*' ' + '*' 
	print(r)
	i += h
			