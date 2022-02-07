'''
Раужев Павел ИУ7-13Б
 
Программа предоставляет возможность работы с меню по побработке текста.
 
 
 
 
'''
 
from cheak_func import *

 
 
def output(txt):
    for st in txt:
        print(st)
    print()
 
 
def left_alignment(txt):
    for j in range(len(txt)):
        while txt[j][0] == ' ':
            txt[j] = txt[j].replace(' ', '', 1)
        if txt[j][0] == ' ': txt[j] = txt[j].replace(' ', '', 1)
    return txt
 
 
def clear(txt):
    txt = left_alignment(txt)
    for i in range(len(txt)):
        while txt[i][-1] == ' ':
            txt[i] = txt[i][:-1]
    return txt
 
 
def right_alignment(txt):
    txt = clear(txt) # Стираем пробелы справа и слева
    landmark = max(len(txt[i]) for i in range(len(txt))) # Ориентир ширины
    for i in range(len(txt)):
        while len(txt[i]) < landmark: # Добавляем в начало пробелы
            if txt[i][0] != ' ':
                txt[i] = txt[i].replace(txt[i][0], ' ' + txt[i][0], 1)
            else:
                txt[i] = txt[i].replace(' ', '  ', 1)
    return txt
 
 
def center_alignment(txt):
    txt = clear(txt) # Стираем пробелы справа и слева
    txt = right_alignment(txt) # Вправо его!
    for i in range(len(txt)):
        k = 0
        for j in range(len(txt[i])): # Считаем, сколько пробелов слева надо удалить
            if txt[i][j] == ' ':
                k += 1
            if txt[i][j] != ' ': break
        t = k // 2
        txt[i] = txt[i].replace(' ', '', t) # удаляем)
    return txt
 
 
def del_word_whole_text(txt , align_type):
    word = input('Введите слово, которое необходимо удалить: ')
    if (len(word.split())) != 1:
        print('При таком вводе учитывается только первое слово.')
        word = word.split()[0]
    for i in range(len(txt)):
        txt[i] = ' ' + txt[i] + ' '
        for j in ' "(':
            for k in ' .,;:)!?"':
                if k!=' ':
                    txt[i] = txt[i].replace(j + word + k, j+k)
                else:
                    txt[i] = txt[i].replace(j + word + k, j)
 
        txt[i] = ''.join(txt[i][1:-1])
    txt = align_type(txt)
    return txt
 
 
def replace_word_whole_text(txt, align_type):
    word = input('Введите слово, которое необходимо заменить: ')
    if (len(word.split())) != 1:
        print('При таком вводе заменится только первое слово.')
        word = word.split()[0]
    new_word = input('Введите слово, на которое необходимо заменить: ')
    if (len(new_word.split())) != 1:
        print('При таком вводе учитывается только первое слово.')
        new_word = new_word.split()[0]
    for i in range(len(txt)):
        if txt[i] == word:
            txt[i] = new_word
            continue
        txt[i] = ' ' + txt[i] + ' '
        for j in ' "(':
            for k in ' .,;:)!?"':
                txt[i] = txt[i].replace(j + word + k, j+new_word+k)
        txt[i] = ''.join(txt[i][1:-1])
    txt = align_type(txt)
    return txt
 
 
def contribution(txt, align_type):
    for i in range(len(txt)):
        if '/' in txt[i] or '*' in txt[i]:
            contr = []
            size_lim = False
            for j in range(len(txt[i])):
                symb = txt[i][j]
                if symb == ' ':
                    if size_lim:
                        contr[-1][2] += 1
                    continue
                elif symb.isdigit():
                    if size_lim:
                        contr[-1][0] += symb
                        contr[-1][2] += 1
                    else:
                        size_lim = True
                        contr.append([symb, j, 1])
                elif size_lim and symb in '*/':
                    contr[-1][0] += symb
                    contr[-1][2] += 1
                else:
                    size_lim = False
 
            for j in range(len(contr) - 1, -1, -1):  # С конца удаляем лишние символы
                contr[j][0] += ' '
                value = 0.0  # Текущее число
                temp_value = None  # Текущее значение выражения
                func = None  # функция
                for k in contr[j][0]:
                        if k.isdigit():
                            value = value * 10 + int(k)
                        else:
                            if func == None:
                                temp_value = value
                            elif func == '*':
                                temp_value *= value
                            elif func == '/':
                                if value == 0:
                                    break
                                else:
                                    temp_value /= value
                            func = k
                            value = 0
                else:
                    if temp_value != None:
                        if txt[i][contr[j][1] + contr[j][2] - 1] == ' ':
                            contr[j][2] -= 1
                        txt[i] = (txt[i][:contr[j][1]] +
                                '{:.5}'.format(temp_value) +
                                    txt[i][contr[j][1] + contr[j][2]:])
    txt = align_type(txt)
    return txt
 
 
def del_shortest_in_fattest(txt, align_type):
    fattest_st = -1
    pure_text = []
    for i in range(len(txt)):
        st = txt[i]
        for j in range(len(st)):
            if st[j] in '.,!;?': st = st.replace(st[j], ' ')
        while st.count('  ') > 0:
            st = st.replace('  ' , ' ')
        if st[0] == ' ': st = st.replace(' ' , '' , 1)
        if len(st.split()) > fattest_st: fattest_st = len(st.split()) ; num_fattest = i ; pure_text.append(st)
    shortest_w = fattest_st
    print('Текст, в котором удалили самое короткое слово {}-й строки:'.format(num_fattest+1))
    sentence = pure_text[-1].split()
    for word in sentence:
        if len(word) < shortest_w and word[-1] not in '01234567890/*': shortest_w = len(word) ; word_to_del = word
    txt[num_fattest] = txt[num_fattest].replace(word_to_del + ' ', '')
    txt[num_fattest] = txt[num_fattest].replace(word_to_del, '')
    txt = align_type(txt)
    return txt
 
 
def main():
    text = ['Momentarily he                               caught O’Brien’s ','eye. O’Brien had s9 / 3 *  4/2tood up. He had ','taken off his spectacles',' and was in the act of resettling them on his nose', 'with his characteristic gesture.']
    output(text)
    align = left_alignment
    while True:
        print(
            '1.Выровнять текст по левому краю.\n2.Выровнять текст по правому краю.\n3.Выровнять текст по ширине.\n4.Удаление всех вхождений заданного слова.\n5.Замена одного слова другим во всём тексте.\n6.Вычисление арифметических выраженийвнутри текста(по варианту).\n7.Удалить самое короткое слово в предложении, в котором слов больше всего.\n0. Завершение программы.\n')
        menu = correct_input('Введите пункт меню: ', 'int+')
        if menu == 0: print('Прощайте! Было приятно иметь с Вами дело.'); break
        if menu == 1:
            print('\nТекст выровнен по левому краю:')
            text = left_alignment(text)
            align = left_alignment
            output(text)
        if menu == 2:
            print('\nТекст выровнен по правому краю:')
            text = right_alignment(text)
            align = right_alignment
            output(text)
        if menu == 3:
            print('\nТекст выровнен по центру:')
            text = center_alignment(text)
            align = center_alignment
            output(text)
        if menu == 4:
            print('\n')
            text = del_word_whole_text(text , align)
            output(text)
        if menu == 5:
            print('\n')
            print('Внимание! Прошу учесть, что ')
            text = replace_word_whole_text(text, align)
            output(text)
        if menu == 6:
            print('\n')
            text = contribution(text, align)
            output(text)
        if menu == 7:
            print('\n')
            text = del_shortest_in_fattest(text, align)
            output(text)
 
main()
 