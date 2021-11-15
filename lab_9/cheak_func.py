def correct_input(input_text, type_number):
	text = input(input_text)
	while True:
		if type_number == 'int':
			if not cheak_int(text):
				print('Ошибка, введите целое число: ')
				text = input(input_text)
			else:
				return int(text)

		if type_number == 'float':
			if not cheak_float(text):
				print('Ошибка, введите действительное число: ')
				text = input(input_text)
			else:
				return float(text)
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
# проверяет корректность ввода вещественных чисел
def cheak_float(text):
	text = text.lower()
	flag = True
	cheak_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', 'e', '-', '+']
	text = list(text)
	
	for i in text:
		if i not in cheak_list:
			flag = False
	if len(text) == 0:
		flag = False
	elif text.count('-') > 1 and 'e' not in text or text.count('+') > 1 and 'e' not in text\
	or len(text) == 1 and text[0] == '-' or (len(text) == 1 and text[0] == '+'):
		flag = False

	elif (text[0] == '.' and text.count('.') == 1) or (text[0] == 'e' and text.count('e') == 1) or text.count('e') > 1 or text.count('.') > 1 \
	or 'e' in text and cheak_int(''.join(text[text.index('e') + 1:])) == False:
		
		flag = False

	return flag