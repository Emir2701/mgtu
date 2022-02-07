print('Программа находит самый длинный полиндром в списке строк')
l = list(input('Введите строки через пробелы: ').split())
print('Список строк: {}'.format(l))

change = False
p_mx = ''

for i in l:
	if i == i[::-1] and len(i) > len(p_mx):
		p_mx = i
		change = True

if change == True:
	print('самый длинный полиндром: {}'.format(p_mx))
else:
	print('нет полиндрома в строке')