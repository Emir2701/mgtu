n = int(input("Введите номер строки: "))

f = open("1.txt", "r+")

s = f.readline()
pointer = 0
num_str = 1
while num_str != n and s.strip() != "":
	pointer += len(s)
	s = f.readline()
	num_str += 1
while s.strip() != "":
	s = f.readline()
	f.seek(pointer)
	f.write(s)
	pointer += len(s)
	f.seek(pointer + len(s))
#f.truncate(f.tell())

f.close()
