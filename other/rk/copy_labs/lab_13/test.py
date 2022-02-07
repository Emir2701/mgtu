from struct import *

string_format = '20sQ20si20s'

name = 'Emir Shimshir'
number = 9999999999999999
date = '01/23'
ccv = 321
bank = 'Сбер'

len_str = 76
b = pack(string_format, name.encode('utf-8'), number, date.encode('utf-8'), ccv, bank.encode('utf-8'))
c = pack(string_format, name.encode('utf-8'), 2, date.encode('utf-8'), 2, bank.encode('utf-8'))

f = open('test2.bin', 'wb')
#print(b)
f.write(b)
f.write(c)
f.close()

f = open('test2.bin', 'rb')
f.seek(0, 2)
pointer = f.tell()
print(pointer)
f.seek(0)
b = f.read(len_str)
#print(b)

b = unpack(string_format, b)
b = list(b)
b[0] = b[0].decode('utf-8')
b[2] = b[2].decode('utf-8')
b[4] = b[4].decode('utf-8')


for i in b:

	print(i,end=' ')
print()


b = f.read(len_str)
#print(b)
b = unpack(string_format, b)
b = list(b)
b[0] = b[0].decode('utf-8')
b[2] = b[2].decode('utf-8')
b[4] = b[4].decode('utf-8')


for i in b:

	print(i,end=' ')
print()

f.close()


# from struct import *

# string_format = 'i'

# len_str = 1
# number = 99999
# b = pack(string_format, number)

# f = open('test2.bin', 'wb')
# #print(b)
# f.write(b)
# #f.write(c)
# f.close()

# f = open('test2.bin', 'rb')
# b = f.read(len_str)
# b = unpack(string_format, b)
# print(b)

# f.close()

