# Шимшир Эмирджан ИУ7-13Б

# Лабораторная работа No11 “Текстовый редактор”

# Написать программу для выполнения некоторых операций с текстом. 
# Вводить текст не требуется, он должен быть задан в исходном тексте программы 
# в виде списка строк (при выводе на экран каждый элемент этого списка должен начинаться с новой строки).
# Программа должна позволять с помощью меню выполнить следующие действия:


# 1. Выровнять текст по левому краю
# 2. Выровнять текст по правому краю
# 3. Выровнять текст по ширине
# 4. Удаление всех вхождений заданного слова
# 5. Замена одного слова другим во всём тексте
# 6. Вычисление арифметических выражений внутри текста умножение и деление
# 7. Найти предложение с максимальным количеством слов, в котором гласные чередуются с согласными.
# 8. Завершение программы

# Основные переменные:

# text – массив строк
# align -тип форматирование



from cheak_func import *

# Выровнять текст по левому краю
def left(text):
	for i in range(len(text)):
		text[i] = " ".join(text[i].split())
	return text
# Выровнять текст по правому краю
def right(text):

	text = left(text)
	mx = max(map(len, text))

	for i in range(len(text)):
		text[i] = (mx - len(text[i])) * ' ' + text[i]

	return text



# Выравнивание по ширине 
def width(text):
	l = [0] * len(text)
	p = [0] * len(text)
	text = left(text)

	for i in range(len(text)):

		l[i] = len(text[i])
		p[i] = text[i].count(' ')
	
	for i in range(len(text)):

		

		line = list(text[i])

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

		text[i] = ''.join(line)
	return text
		
		


	return text

def output(text):
	for i in text:
		print(i)
	print()
# Удаление всех вхождений заданного слова
def del_word(text, align):

	word = input('Введите слово, которое необходимо удалить: ')
	if  not word == '': 
		if (len(word.split())) != 1:
			print('При таком вводе учитывается только первое слово.')
			word = word.split()[0]
	for i in range(len(text)):
		text[i] = ' ' + text[i] + ' '
		for j in ' "(':
			for k in ' .,;:)!?"':
				if k!=' ':
					text[i] = text[i].replace(j + word + k, j+k)
				else:
					text[i] = text[i].replace(j + word + k, j)

		text[i] = text[i][1:-1]
	text = align(text)
	return text

# Замена одного слова другим во всём тексте
def repl_word(text, align):

	word = input('Введите слово, которое необходимо заменить: ')
	while word == '':
		print('Нельзя заменить пустую строку')
		word = input('Введите слово, которое необходимо заменить: ')
	
	if (len(word.split())) != 1:
		print('При таком вводе заменится только первое слово.')
		word = word.split()[0]
	new_word = input('Введите слово, на которое необходимо заменить: ')

	while new_word == '':
		print('Нельзя заменить пустую строку')
		new_word = input('Введите слово, которое необходимо заменить: ')
	

	if (len(new_word.split())) != 1:
		print('При таком вводе учитывается только первое слово.')
		new_word = new_word.split()[0]
	for i in range(len(text)):
		if text[i] == word:
			text[i] = new_word
			continue
		text[i] = ' ' + text[i] + ' '
		for j in ' "(':
			for k in ' .,;:)!?"':
				text[i] = text[i].replace(j + word + k, j+new_word+k)
		text[i] = text[i][1:-1]
	text = align(text)
	return text

# Вычисление значения арифметического выражения в тексте
def math(text, align):
	for i in range(len(text)):
		# Массив арифметического выражения
		calculations = []
		# В тексте ли мы находимся?
		in_text = False
		for j in range(len(text[i])):
			sumbol = text[i][j]
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
							temp_value = None
							break
						else:
							temp_value /= value
					func = k
					value = 0
			
			if temp_value != None:
				# Удаление одного пробела
				if text[i][calculations[j][1]+calculations[j][2]-1] == ' ':
					calculations[j][2] -= 1

				# Замена выражения на ответ
				text[i] = (text[i][:calculations[j][1]] +
						'{:.4}'.format(temp_value) +
						text[i][calculations[j][1]+calculations[j][2]:])

	text = align(text)
	return text


# Найти предложение с максимальным количеством слов, в котором гласные чередуются с согласными.

def is_good(string):

	glas = 'aeyuioAEYUIOыуаеиоюэёяЯЫУАЕИОЮЭЁ'
	soglas = 'qzwsxdcrfvtgbhnjmklpQZWSXDCRFVTGBHNJMKLPйфцчвскмпнртгшлбщдзжхЙФЦЧВСКМПНРТГШЛБЩДЗЖХ'

	if string[0] in glas:
		base = glas
	else:
		base = soglas

	for i in string:
		if i in base:
			if base == glas:
				base = soglas
			else:
				base = glas
		else:
			return False
	#print(string)
	return True 

def mx_index(m):
    mx = m[0]
    mx_ind = 0
    for i in range(1, len(m)):
        if mx < m[i]:
            mx = m[i]
            mx_ind = i
    return mx_ind

def find_max(text):
	text = ' '.join(text)
	text = " ".join(text.split())
	text = text.split('. ')

	for i in range(len(text) - 1):
		text[i] += '.'
	word_count = [0] * len(text)
	#print(text)
	for i in range(len(text)):
		words = text[i].split()
		#print(words)
		for j in range(len(words)):
			if is_good(words[j]):
				word_count[i] += 1
	#print(word_count)
	print('{} предложение:'.format(mx_index(word_count) + 1))
	print(text[mx_index(word_count)])



def main():
	
	text = ['Слово',
	'Я скажу то,            что для тебя не новость. Мир не такой уж',
	'солнечный и приветливый. Это очень опасное,',
	'жёсткое место. И если только дашь слабину, он',
	'опрокинет с         такой силой тебя, что больше уже',
	'не встанешь. Ни ты, ни 2 *4 / 3*22/22  я, никто на свете не бьёт',
	' так сильно, как жизнь. Совсем не важно, как ты',
	'ударишь, а важно, КАКОЙ ДЕРЖИШЬ УДАР, как',
	' двигаешься вперёд. Будешь идти — ИДИ, если с',
	'         испугу не свернёшь. Только так побеждают. Если',
	' знаешь, чего ты стОишь,2 + 2 иди и бери своё, но будь',
	' готов удары держать, а не плакаться и говорить:', 
	'          «Я ничего не добился из-за него, из-за 2 * 2 неё, из-за',
	' кого-то». Так делают трУсы, а ты не трус. Быть',
	' этого не может. …я всегда                буду тебя любить, что бы',
	' ни случилось. Ты мой сын — плоть от плоти, самое',
	' дорогое,                что у меня есть. Но пока ты не ',
	'поверишь в себя, жизни не будет.']

	print("Исходный текст:")
	print("-" * max(map(len, text)))
	output(text)
	print("-" * max(map(len, text)))
	
	align = left

	while True:

		input_text = '(Для вывода меню введите 9). Введите номер функции: '
		f = correct_input(input_text, 'int+')

		if f == 1:

			text = left(text)
			print('\nТекст выровнен по левому краю:\n')
			print("-" * max(map(len, text)))
			output(text)
			print("-" * max(map(len, text)))
			align = left

		elif f == 2:

			text = right(text)
			print('\nТекст выровнен по правому краю:\n')
			print("-" * max(map(len, text)))
			output(text)
			print("-" * max(map(len, text)))
			align = right

		elif f == 3:
			text = width(text)
			print('\nТекст выровнен по ширине:\n')
			print("-" * max(map(len, text)))
			output(text)
			print("-" * max(map(len, text)))
			align = width
		elif f == 4:
			text = del_word(text, align)
			print("-" * max(map(len, text)))
			output(text)
			print("-" * max(map(len, text)))

		elif f == 5:
			text = repl_word(text, align)
			print("-" * max(map(len, text)))
			output(text)
			print("-" * max(map(len, text)))

		elif f == 6:
			text = math(text, align)
			print("-" * max(map(len, text)))
			output(text)
			print("-" * max(map(len, text)))

		elif f == 7:
		    find_max(text)
		elif f == 8:
		    break
		elif f == 9:
		    # вывод меню
		    print('------------------------------------------------------------------------------------------------')
		    print('Меню:')
		    print('1. Выровнять текст по левому краю')
		    print('2. Выровнять текст по правому краю')
		    print('3. Выровнять текст по ширине')
		    print('4. Удаление всех вхождений заданного слова')
		    print('5. Замена одного слова другим во всём тексте')
		    print('6. Вычисление арифметических выражений внутри текста умножение и деление')
		    print('7. Найти предложение с максимальным количеством слов, в котором гласные чередуются с согласными.')
		    print('8. Завершение программы')
		    print('------------------------------------------------------------------------------------------------')
		else:
		    print('Ошибка, нет такой функции')

main()


