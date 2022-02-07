# В файле in.txt записаны дробные числа в 8-ричной системе счисления, 
# по одному в строке, разделитель целой и дробной части - точка.
# Требуется:
# 1. Перевести числа из исходного файла в 16-ричную систему счисления и 
#переписать их в файл out1.txt по одному в строке в том же порядке.
# 2. Переписать строки файла out1.txt в файл out2.txt, отсортировав их по увеличению длин.

# Обработку файлов производить построчно, содержимое файла читать в память целиком запрещается. 
#Списки, множества, словари, кортежи для сортировки не использовать.
def from_8_to_16(number_8):
	from_8_to_2 = {"0":"000", "1":"001", "2":"010", "3":"011", \
			  	   "4":"100", "5":"101", "6":"110", "7":"111"}
	
	
	first_part_8, second_part_8 = number_8.split(".")[0], number_8.split(".")[1]
	first_part_2 = ""
	second_part_2 = ""
	for i in first_part_8:
		first_part_2 += from_8_to_2[i]
	for i in second_part_8:
		second_part_2 += from_8_to_2[i]
	first_part_2 = "0" * (4 - len(first_part_2) % 4) + first_part_2
	second_part_2 = second_part_2 + "0" * (4 - len(second_part_2) % 4) 
	number_2 = first_part_2 + "." + second_part_2

	form_2_to_16 = {"0000":"0", "0001":"1", "0010":"2", "0011":"3", \
					"0100":"4", "0101":"5", "0110":"6", "0111":"7", \
					"1000":"8", "1001":"9", "1010":"A", "1011":"B", \
					"1100":"C", "1101":"D", "1110":"E", "1111":"F"}
	
	pos= 0
	number_16 = ""
	while pos < len(number_2):
		s = number_2[pos:pos + 4]
		if "." in s:
			number_16 += "."
		
			pos += 1
		else:
			number_16 += form_2_to_16[s]

			pos += 4

	if number_16[0] == '0':
		number_16 = number_16[1:]
	if number_16[-1] == '0':
		number_16 = number_16[:-1]
	return number_16
# print(from_8_to_16("213.21312"))
fr = open("in.txt", "r")
fw = open("out1.txt", "w")
s = fr.readline()

while s.strip() != "":
	fw.write(from_8_to_16(s.strip()) + "\n")
	s = fr.readline()
	
fr.close()
fw.close()

with open("out1.txt") as f, open("out2.txt", "w+") as out:    # просили out1.txt отсортировать
    while True:
        line = f.readline()
        if not line:
            break 
        
        line_length = len(line)
        
        out.seek(0)
        while True:
            test_line_start = out.tell()
            test_line = out.readline()
            if not test_line:
                break
            test_line_len = len(test_line)
            if test_line_len > line_length:
                out.seek(test_line_start)
                break 
        
        old_line = line 
        cursor_to_write = out.tell()
        cursor_to_read = cursor_to_write
        
        while old_line:
            out.seek(cursor_to_read)
            test_line = out.readline()
            cursor_to_read = out.tell()
            out.seek(cursor_to_write)
            out.write(old_line)
            cursor_to_write = out.tell()
            old_line = test_line
