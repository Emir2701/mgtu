# 1) в файле 1.txt записана неубывающая последовательность чисел (каждое с новой строки) 
# и в файле 2.txt так же, нужно в файл 3.txt переписать эти числа тоже в неубывающем порядке,
# можно держать в памяти за раз только по одному числу из каждого файла

f1 = open("1.txt", "r")
f2 = open("2.txt", "r")
f3 = open("3.txt", "w")


i1 = f1.readline()
i2 = f2.readline()

while i1.strip() != "" or i2.strip() != "":
	if i1.strip() != "" and i2.strip() != "":
		if int(i1) > int(i2):
			f3.write(i2)
			i2 = f2.readline()
		else:
			f3.write(i1)
			i1 = f1.readline()
	elif i1.strip() == "":
		f3.write(i2)
		i2 = f2.readline()
	else:
		f3.write(i1)
		i1 = f1.readline()

f1.close()
f2.close()
f3.close()


