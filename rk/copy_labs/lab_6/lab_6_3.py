def correct_input(input_text, text_error, type_number):
	text = input(input_text)
	while True:
		if type_number == 'int':
			if not cheak_int(text):
				print(text_error)
				text = input(input_text)
			else:
				return int(text)

		if type_number == 'float':
			if not cheak_float(text):
				print(text_error)
				text = input(input_text)
			else:
				return float(text)




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

def cheak_float(text):
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

input_text = 'Введите число: '
text_error = 'Ошибка, введите число'

print(correct_input(input_text, text_error, 'float'))

