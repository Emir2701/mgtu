# проверяет корректность ввода данных
def correct_input(input_text, type_number):
	text = input(input_text)

	while True:
		if type_number == 'int':
			if not cheak_int(text):
				print('Ошибка, введите целое число: ')
				text = input(input_text)
			else:
				return int(text)

		if type_number == 'int+':
			if not cheak_int_plus(text):
				print('Ошибка, введите целое положительное число: ')
				text = input(input_text)
			else:
				return int(text)
# проверяет корректность ввода целых чисел
def cheak_int(text):
	flag = True
	cheak_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '+']
	text = list(text)
	for i in text:
		if i not in cheak_list:
			flag = False
			
	if len(text) == 0:
		flag = False
	elif (text[0] != '-' and text.count('-') == 1) or text.count('-') > 1 or (len(text) == 1 and text[0] == '-') \
	or (text[0] != '+' and text.count('+') == 1) or text.count('+') > 1 or (len(text) == 1 and text[0] == '+'):
		flag = False
	
	return flag
# проверяет корректность ввода целых положительных чисел
def cheak_int_plus(text):
	flag = True
	cheak_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	text = list(text)
	for i in text:
		if i not in cheak_list:
			flag = False
			
	if len(text) == 0:
		flag = False
	elif text[0] == '0':
		flag = False
	
	return flag

def m_input(m):
	
	i = correct_input('Введите количество строк матрицы: ', 'int+')
	j = correct_input('Введите количество столбцов матрицы: ', 'int+')
	for i_iter in range(i):
		m.append([])
		for j_iter in range(j):
			elem_input = 'Введите {}-ый элементы {}-й строки: '.format(j_iter + 1, i_iter + 1)
			m[i_iter].append(correct_input(elem_input, 'int'))
	return m

def m_trans(m):
    if len(m) == 0:
        print('Ошибка, пустая матрица')
        return m
    i_max = len(m)
    j_max = len(m[0])
    m_t = [[0] * i_max for i in range(j_max)]
    for i in range(i_max):
        for j in range(j_max):
            m_t[j][i] = m [i][j]
    return m_t

def m_output(m):
	for i in m:
		print(*i)

m = list()
m = m_input(m)
m_output(m)
m = m_trans(m)
m_output(m)




