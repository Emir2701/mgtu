# Караакотова Наталья ИУ7-13Б

# Программа предназначена для работы с текстом через меню

# Переменные, принимаемые программой на вход:
# n – номер пункта меню
# word – слово, которое нужно заменить или удалить

# Переменные функций проверки введённого значения:
# text – приглашение ввода
# type_1 – тип числа, который можно использовать в данном пункте
# n – строка, которую мы проверяем на целочисленнное (и положительное) значение

# Переменные для вычислений:
# text – текст
# align – выравнивание
# l – список длин строк
# p – список количества разрывов между словами в строке
# line – список символов строки
# ad – сколько пробелов надо добавить после каждого слова
# ost – сколько дополнительных пробелов нужно добавить
# word_1 – слово, которое нужно заменить
# word_2 – слово, на которое нужно заменить
# calculations – массив с арифметическим выражением
# in_text – находимся внутри выражения
# value – значение выражения
# temp_value – текущее значение выражения
# func – арифметическая операция




text = ['Наташа',
		'Он отпер дверь своим        ключом и вошел, а следом, в смущении сдернув кепку, ', 
        '        шагнул молодой парень. Что-то в его грубой одежде сразу же', 
        'выдавало моряка, и в 2 *4 / 3*22/22 просторном холле, где они оказались, он был явно не к месту. Он не знал, куда девать кепку,', 
        ' стал было        засовывать  ее в карман пиджака, но тот, другой, отобрал ее. Отобрал ', 
        'спокойно, естественно,  и парень, которому тут,', 
        ' видно,          было не по себе,    в душе поблагодарил его. «Понимает, – подумал он. ', 
        '– Поможет, все обойдется».']


# Проверка введённого значения
def check_num(text, type_1):
	text_1 = str(input(text))

	while True:
		# Если пустая строка
		if not text_1:
			text_1 = input(text)

		# Если нужно целое положительное число
		if type_1 == '+':
			if positive(text_1):
					return int(text_1)
			else:
				print('Введите целое положительное число.')
				text_1 = input(text)
			

# Проверка на целое положительное:
def positive(n):
    # Если у числа есть знак
    if n[0] == '+':
        n = n[1:]
    # Число не ноль
    if n[0] == '0':
    	return False
    return n.isdigit()


# Удаление ненужных пробелов
def del_space(text_1):
	l = [0] * len(text_1)
	p = [0] * len(text_1)
	for i in range(len(text_1)):
		line = list(text_1[i]) 
		line.append(' ')
		j = 0
		while j < len(line):
		 	if line[j] == ' ':
		 		if j == 0 or line[j - 1] == ' ':
		 			line.pop(j)
		 			j -= 1
		 		else:
		 			p[i] += 1
		 	j += 1
		p[i] -= 1
		line.pop(-1)
		text_1[i] = ''.join(line)
		l[i] = len(text_1[i])
	return text_1, l, p


# Выравнивание по левому краю
def left(text_1):
	text_1, l, p = del_space(text_1)
	return text_1


# Выравнивание по правому краю
def right(text_1):
	text_1, l, p = del_space(text_1)
	for i in range(len(text_1)):
		text_1[i] = ' ' * (max(l) - len(text_1[i])) + text_1[i]
	return text_1
		

# Выравнивание по ширине 
def width(text_1):
	text_1, l, p = del_space(text_1)
	for i in range(len(text_1)):
		line = list(text_1[i])

		if p[i] == 0:
			ad = 0
		else:
			ad = (max(l) - l[i]) // p[i] # Сколько пробелов добавить
		
		if p[i] == 0:
			ost = 0
		else:
			ost = (max(l) - l[i]) % p[i] # Остаточные
		ost_1 = 0
		for j in range(len(line)):
			if line[j] == ' ':
				line[j] += ' ' * ad
				if ost_1 < ost:
					line[j] += ' ' 
					ost_1 += 1

		text_1[i] = ''.join(line)
	return text_1


# Удаление слов во всём тексте
def del_word(text_1, align_1):
	word = input('Введите слово, которое нужно удалить: ')
	print()

	while not word:
		print('Вы не ввели слово.')
		print()
		word_1 = input('Введите слово, которое нужно удалить: ')
		print()
	
	if len(word.split()) != 1:
		print("Удалится только первое слово.")
		print()
		word = word.split()[0]
	for i in range(len(text_1)):
		text_1[i] = ' ' + text_1[i] + ' '
		for j in ' "(':
			for k in ' .,:;)!?"':
				text_1[i] = text_1[i].replace(j + word + k, j + k)
		text_1[i] = ''.join(text_1[i][1:-1])
	text_1 = align_1(text_1)
	return text_1

# Замена слова во всём тексте
def replace_word(text_1, align_1):
	word_1 = input("Введите слово, которое нужно заменить: ")
	print()

	while not word_1:
		print('Вы не ввели слово.')
		print()
		word_1 = input("Введите слово, которое нужно заменить: ")
		print()

	if len(word_1.split()) != 1:
		print("Только первое слово будет заменено.")
		print()
		word_1 = word_1.split()[0]

	word_2 = input("Введите новое слово: ")
	print()

	while not word_2:
		print('Вы не ввели слово.')
		print()
		word_2 = input("Введите новое слово: ")
		print()

	if len(word_2.split()) != 1:
		print("Только на первое слово будет заменено.")
		print()
		word_2 = word_2.split()[0]

	for i in range(len(text_1)):
		if text_1[i] == word_1:
			text_1[i] = word_2
			continue
		text_1[i] = ' ' + text_1[i] + ' '
		for j in ' "(':
			for k in ' .,:;)!?"':
				text_1[i] = text_1[i].replace(j + word_1 + k, 
						j + word_2 + k)
		text_1[i] = ''.join(text_1[i][1:-1])
	text_1 = align_1(text_1)
	return text_1
	

# Вычисление значения арифметического выражения в тексте
def calc(text_1, align_1):
	for i in range(len(text_1)):
		# Массив арифметического выражения
		calculations = []
		# В тексте ли мы находимся?
		in_text = False
		for j in range(len(text_1[i])):
			sumbol = text_1[i][j]
			# Если пробел
			if sumbol == ' ':
				if in_text:
					calculations[-1][2] += 1
				continue
			# Если число
			elif sumbol.isdigit():
				if in_text:
					calculations[-1][0] += sumbol
					calculations[-1][2] += 1
				else:
					in_text = True
					calculations.append([sumbol, j, 1]) # [выражение, индекс начала, количество знаков в выражении]
			# Если умножение или деление
			elif in_text and sumbol in '*/':
				calculations[-1][0] += sumbol
				calculations[-1][2] += 1
			else:
				in_text = False

		for j in range(len(calculations) - 1, -1, -1): # Идём с конца, чтобы удалять ненужные символы
			calculations[j][0] += ' '
			value = 0.0 # Текущее число
			temp_value = None # Текущее значение выражение
			func = None # функция
			for k in calculations[j][0]:
				if k.isdigit():
					value = value * 10 + int(k)
				else:
					if func == None:
						temp_value = value
					elif func == '*':
						temp_value *= value
					elif func == '/':
						if value == 0:
							break
						else:
							temp_value /= value
					func = k
					value = 0
			
			if temp_value != None:
				# Удаление одного пробела
				if text_1[i][calculations[j][1]+calculations[j][2]-1] == ' ':
					calculations[j][2] -= 1

				# Замена выражения на ответ
				text_1[i] = (text_1[i][:calculations[j][1]] +
						'{:.4}'.format(temp_value) +
						text_1[i][calculations[j][1]+calculations[j][2]:])

	text_1 = align_1(text_1)
	return text_1


# Удалить самое короткое слово в предложении, в котором слов больше всего.
def del_short_word(text_1):
	p = [] # Текущее предложение
	ps = [] # Массив предложений
	max_i = 0 # Индекс предложения с максимальным количеством слов
	for i in range(len(text_1)):
		line = text_1[i].split() # Массив элементов текущей строки
		for j in range(len(line)):
			word = line[j] 
			if word[-1] == '.':
				p.append(word)
				ps.append(p)
				if len(p) > len(ps[max_i]):
					max_i = len(ps)-1
				p = []
			else:
				p.append(word)

	ind_w = 0 # идекс самого короткого слова
	st_short = 0 # начало самого короткого слова
	end_short = len(ps[max_i][0]) - 1 # конец самого короткого слова
	min_len = end_short - st_short # минимальная длина слова
	for i in range(len(ps[max_i])):
		word = ps[max_i][i]
		st_ind = -1
		end_ind = -1
		for j in range(len(word)):
			if word[j].isalpha():
				st_ind = j
				break
		for j in range(len(word) - 1, -1, -1):
			if word[j].isalpha():
				end_ind = j
				break
		len_w = end_ind - st_ind	
		if st_ind != -1 and (len_w < min_len):
			min_len = len_w
			ind_w = i
			st_short = st_ind
			end_short = end_ind

	# Удаление слова
	ps[max_i][ind_w] = ps[max_i][ind_w][:st_short] + ps[max_i][ind_w][end_short + 1:]
	if ps[max_i][ind_w] == '':
		ps[max_i].pop(ind_w)
	print(*ps[max_i])
	print()


# Вывод текста
def print_text(text_1):
	for i in range(len(text_1)):
		print(text_1[i])

align = left
text, l, p = del_space(text)

# Работа с меню
while True:
	print('Меню:\n',
		  '1. Выровнять текст по левому краю\n',
		  '2. Выровнять текст по правому краю\n',
		  '3. Выровнять текст по ширине\n',
		  '4. Удаление всех вхождений заданного слова\n',
		  '5. Замена одного слова другим во всём тексте\n',
		  '6. Вычисление арифметических выражений внутри текста (по варианту)\n',
		  '7. Удалить самое короткое слово в предложении, в котором слов больше всего.\n',
		  '8. Завершить программу.')
	print()
	n = check_num('Введите пункт меню: ', '+')
	print()

	if n == 1:
		text = left(text)
		align = left
		print_text(text)
		print()

	elif n == 2:
		text = right(text)
		align = right
		print_text(text)
		print()

	elif n == 3:
		text = width(text)
		align = width
		print_text(text)
		print()

	elif n == 4:
		text = del_word(text, align)
		print_text(text)
		print()

	elif n == 5:
		text = replace_word(text, align)
		print_text(text)
		print()

	elif n == 6:
		text = calc(text, align)
		print_text(text)
		print()

	elif n == 7:
		del_short_word(text)

	elif n == 8:
		break

	else:
		print('Пункта меню с таким номером нет.')
		print()









