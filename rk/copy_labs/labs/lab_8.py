'''
1. Ввести матрицу
2. Добавить строку
3. Удалить строку
4. Добавить столбец
5. Удалить столбец
6. Найти строку, имеющую наибольшее количество повторяющихся элементов 5
7. Переставить местами строки с наибольшим и наименьшим количеством
отрицательных элементов
8. Найти столбец, имеющий наибольшее количество простых чисел 1
9. Переставить местами столбцы с максимальной и минимальной суммой
элементов
10. Вывести текущую матрицу
'''
# проверяет корректность ввода данных
def correct_input(input_text, type_number):
    text = input(input_text)

    while True:
        if type_number == 'int':
            if not cheak_int(text):
                print('Ошибка, введите целое число: ')
                text = input(input_text)
            else:
                return int(text)

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

def m_input(m):
    m = []
    i = correct_input('Введите количество строк матрицы: ', 'int+')
    j = correct_input('Введите количество столбцов матрицы: ', 'int+')
    for i_iter in range(i):
        m.append([])
        for j_iter in range(j):
            elem_input = 'Введите {}-ый элементы {}-й строки: '.format(j_iter + 1, i_iter + 1)
            m[i_iter].append(correct_input(elem_input, 'int'))
    return m


def m_output(m):
    for i in m:
        print(*i)

def m_trans(m):
    i_max = len(m)
    j_max = len(m[0])
    m_t = [[0] * i_max for i in range(j_max)]
    for i in range(i_max):
        for j in range(j_max):
            m_t[j][i] = m [i][j]
    return m_t


def m_add_str(m):
    if len(m) == 0:
        print('Ошибка, пустая матрица')
        return m
    # Проверка входных данных
    # -----------------------------------------
    k = correct_input('Введите номер строки матрицы, на место которой нужно добавить новую строку: ', 'int+')

    if k - 1 > len(m):
        print('Ошибка, под данным номером нет строки в матрице')
        m = m_add_str(m)
        return m
    # -----------------------------------------
    new_str = []
    for i in range(len(m[0])):
        elem_input = 'Введите {}-ый элемент новой строки: '.format(i + 1)
        new_str.append(correct_input(elem_input, 'int'))

    m.append(-1)
    k -= 1
    for i in range(len(m) - 1, k, -1):
        m[i] = m[i-1]
    m[k] = new_str

    return m  

def m_del_str(m):
    # Проверка входных данных
    # -----------------------------------------
    if len(m) == 0:
        print('Ошибка, нет строк в матрице')
        return m

    k = correct_input('Введите нужный номер строки матрицы: ', 'int+')
    
    if k > len(m):
        print('Ошибка, под данным номером нет строки')
        m = m_del_str(m)
        return m

    # -----------------------------------------

    # удаление элемента
    k -= 1
    for i in range(k + 1, len(m)):
            m[i-1] = m[i]
    del m[-1]
    
    return m 

def m_add_col(m):
    m = m_trans(m)
    if len(m) == 0:
        print('Ошибка, пустая матрица')
        return m
    # Проверка входных данных
    # -----------------------------------------
    k = correct_input('Введите номер столбца матрицы, на место которого нужно добавить новый столбец: ', 'int+')

    if k - 1 > len(m):
        print('Ошибка, под данным номером нет столбца в матрице')
        m = m_add_str(m)
        return m
    # -----------------------------------------
    new_str = []
    for i in range(len(m[0])):
        elem_input = 'Введите {}-ый элемент нового столбца: '.format(i + 1)
        new_str.append(correct_input(elem_input, 'int'))

    m.append(-1)
    k -= 1
    for i in range(len(m) - 1, k, -1):
        m[i] = m[i-1]
    m[k] = new_str
    m = m_trans(m)

    return m  
def m_del_col(m):
    m = m_trans(m)
    # Проверка входных данных
    # -----------------------------------------
    if len(m) == 0:
        print('Ошибка, нет столбцов в списке')
        return m

    k = correct_input('Введите нужный номер столбца матрицы: ', 'int+')
    
    if k > len(m):
        print('Ошибка, под данным номером нет столбца')
        m = m_del_str(m)
        return m

    # -----------------------------------------

    # удаление элемента
    k -= 1
    for i in range(k + 1, len(m)):
            m[i-1] = m[i]
    del m[-1]
    m = m_trans(m)
    return m 

def find_repeat_str(m):
    m_str = []
    m_temp = []
    count = float('-inf')
    for i in range(len(m)):
        m_temp.append([])
        
        for j in range(len(m[0])):
            m_temp[i].append(m[i].count(m[i][j]))

    m_list = []
    for i in range(len(m_temp)):
        m_list.append(max(m_temp[i]))
        
    print(*m[m_list.index(max(m_list))]) 


def main():
    m = list()
    while True:
        
        input_text = '(Для вывода меню введите 12). Введите номер функции: '
        f = correct_input(input_text, 'int+')
        
        if f == 1:
            m = m_input(m)
        elif f == 2:
            m = m_add_str(m)
        elif f == 3:
            m = m_del_str(m)
        elif f == 4:
            m = m_add_col(m)
        elif f == 5:
            m = m_del_col(m)
        elif f == 6:
            m = find_repeat_str(m)
        elif f == 7:
            m = change(l)
        elif f == 8:
            m = change(l)
        elif f == 9:
            m = change(l)
        elif f == 10:
            m_output(m)
        elif f == 11:
            break
        elif f == 12:
            # вывод меню
            print('---------------------------------------------------------------------------------------------')
            print('Меню:')
            print('1.  Ввести матрицу')
            print('2.  Добавить строку')
            print('3.  Удалить строку')
            print('4.  Добавить столбец')
            print('5.  Удалить столбец')
            print('6.  Найти строку, имеющую наибольшее количество повторяющихся элементов')
            print('7.  Переставить местами строки с наибольшим и наименьшим количеством отрицательных элементов')
            print('8.  Найти столбец, имеющий наибольшее количество простых чисел')
            print('9.  Переставить местами столбцы с максимальной и минимальной суммой элементов')
            print('10. Вывести текущую матрицу')
            print('11. Завершение программы')
            print(('---------------------------------------------------------------------------------------------'))
        else:
            print('Ошибка, нет такой функции')


main()









