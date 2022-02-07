"""
Виногадов Илья

В файле in.txt записаны дробные числа в 8-ричной системе счисления, по одному в строке, разделитель целой и дробной части - точка.
Требуется:
1. Перевести числа из исходного файла в 16-ричную систему счисления и переписать их в файл out1.txt по одному в строке в том же порядке.
2. Переписать строки файла out1.txt в файл out2.txt, отсортировав их по увеличению длин.
Обработку файлов производить построчно, содержимое файла читать в память целиком запрещается. Списки, множества, словари, кортежи для сортировки не использовать.
"""

# 
# 1
# 

with open("in.txt") as f, open("out1.txt", "w") as out:
    while True:
        line = f.readline()
        if not line:
            break 
        
        whole, frac = line.strip().split(".")   # целые числа это подмножество вещественных
        frac_digits = len(frac)
        frac_denom = 8 ** frac_digits
        whole_dec = int(whole, base=8)

        frac_dec = int(frac, base=8)

        whole_16 = hex(whole_dec)[2:]
        print(whole_dec, frac_dec, whole_16)
        frac_16 = ""
        
        while frac_dec:
            frac_dec *= 16 
            frac_16 += hex(frac_dec // frac_denom)[2:]
            frac_dec %= frac_denom
        print(f"{whole_16}.{frac_16}", file=out)

        
#
# 2
#
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

# 10+9