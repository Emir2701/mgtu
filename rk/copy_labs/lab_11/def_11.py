char = input("Введите букву: ")
text = ['Б Б ааа аввв апп аа в. ввв вв аа а а аап вв ап']

def clear(text):
	text = ' '.join(text)
	text = text.split()
	i = 0
	while i < len(text):
		for j in ' "(.,;:)!?"…«»1234567890+-*/_-—*':
			text[i] = text[i].replace(j, '')
		if text[i] == '':
			del text[i]
		else:
			i += 1
	return(text)
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
		words = clear(words)
		for j in range(len(words) - 1):
			print(words[j][0], words[j + 1][0])
			if char == words[j][0] and char == words[j + 1][0]:
				print(words[j][0], words[j + 1][0])
				word_count[i] += 1
	print(word_count)
	#print(word_count)
	print('{} предложение:'.format(mx_index(word_count) + 1))
	print(text[mx_index(word_count)])

find_max(text)
# text = ' '.join(text)
# text = text.split()
# i = 0
# while i < len(text):
# 	for j in ' "(.,;:)!?"…«»1234567890+-*/_-—*':
# 		text[i] = text[i].replace(j, '')
# 	if text[i] == '':
# 		del text[i]
# 	else:
# 		i += 1

# array = list(set(text))

# count = [0]*len(array)

# for i in range(len(count)):

# 	count[i] = text.count(array[i])


# print(array[mx_index(count)])






