from struct import *




file = open("base.bin", "rb+")

string_format = '20sQ20sh20s'
string_len = 74


file.seek(0,2)
size = file.tell()
file.seek(0)

for i in range(size // string_len):

		string = list(unpack(string_format, file.read(string_len)))
		



		string[2] = string[2].decode('utf-8')
		string[2] = string[2].replace('\x00', '')

		
	
		string = string[2].split("/")
		string = list(map(int, string))

		# просрочка

		if (string[1] <= 21 and not (string[1] == 21 and string[0] == 12)):
			pointer = file.tell()
			temp = pointer
			

			for i in range(pointer, size, string_len):

				file.seek(i)
				number = file.read(string_len)
				file.seek(i - string_len)
				file.write(number)

			size -= string_len
			file.truncate(size)
			file.seek(temp - string_len)


file.close()



