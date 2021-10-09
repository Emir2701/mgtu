# Шимшир Эмирджан Османович ИУ7-13Б

# Программа считает объем, площадь полной поверхности и
# площадь боковой поверхности шарового сегмента

# наименование переменных:

# Вывод:
# v - объем
# s_side - площадь боковой поверхности
# s_total - площадь полной поверхности

# Ввод:
# r - радиус основания шарового сегмента
# h - высота шарового сегмента

# Блок ввода:

# импорт занчения пи из библиотеки math
from math import pi 

r = float(input('Введите радиус основания шарового сегмента: '))
h = float(input('Введите высоту шарового сегмента: '))

if r <= 0:
	print('Ошибка. Радиус не может быть отрицательным или равным 0')
elif h <= 0:
	print('Ошибка. Высота не может быть отрицательной или равной 0')
else:
	
	# Блок вычислений:
	
	v = (pi*h*(3 * r**2 + h**2))/6 # подсчет объема шарового сегмента
	s_side = pi*(r**2 + h**2) # подсчет площади боковой поверхности шарового сегмента
	s_total = s_side + pi*r**2 # подсчет площади полной поверхности шарового сегмента
	
	# Блок вывода:
	
	print('объем шарового сегмента = {:.4f}'.format(v))
	print('площадь боковой поверхности шарового сегмента = {:.4f}'.format(s_side))
	print('площадь полной поверхности шарового сегмента = {:.4f}'.format(s_total))
