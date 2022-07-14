# Шимшир Эмирджан ИУ7-13Б

# Программа предназначена для работы с целочисленной матрицей с помощью меню:

# 1. Ввести матрицу
# 2. Добавить строку
# 3. Удалить строку
# 4. Добавить столбец
# 5. Удалить столбец
# 6. Найти строку, имеющую наибольшее количество повторяющихся элементов 5
# 7. Переставить местами строки с наибольшим и наименьшим количеством
# отрицательных элементов
# 8. Найти столбец, имеющий наибольшее количество простых чисел 1
# 9. Переставить местами столбцы с максимальной и минимальной суммой
# элементов
# 10. Вывести текущую матрицу
# 11. Завершение программы

# Основные переменные:
# input_text – приглашение ввода
# type_number – тип числа, который можно использовать в данном пункте
# text – строка, которую мы проверяем на целочисленнное (и положительное) значение
# m - матрица
# n_str - количество строк в матрице
# n_col - количество столбцов в матрице
# k - номер введенный пользователем
# m_temp - вспомогательный массив/матрица
# i_mx / i_mn - индекс подходящей строки/столбца


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

# ввод матрицы
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
# вывод матрицы 
def m_output(m):
    if len(m) == 0:
        print('пустая матрица')
    else:
        for i in range(len(m)):
          for j in range(len(m[0])):
              print('{:<10}'.format(m[i][j]),end=' ')
          print()

# добавление строки алгортмически
def m_add_str_alg(m):
    if len(m) == 0:
        n_str = 0
        n_col = correct_input('Введите количество столбцов матрицы: ', 'int+')
        k = 1
    else:
        n_str = len(m)
        n_col = len(m[0])
        # Проверка входных данных
        # -----------------------------------------
        k = correct_input('Введите номер строки матрицы, на место которой нужно добавить новую строку: ', 'int+')

        while k - 1 > n_str:
            print('Ошибка, под данным номером нет строки в матрице')
            k = correct_input('Введите номер строки матрицы, на место которой нужно добавить новую строку: ', 'int+')

        # -----------------------------------------




    
    new_str = []
    for i in range(n_col):
        elem_input = 'Введите {}-ый элемент новой строки: '.format(i + 1)
        new_str.append(correct_input(elem_input, 'int'))

    m.append(-1)
    n_str += 1
    k -= 1

    for i in range(n_str - 1, k, -1):
        m[i] = m[i-1]
        

    m[k] = new_str
    

    return m 
# добавление строки c использованием функционала python
def m_add_str_python(m):
    if len(m) == 0:
        n_str = 0
        n_col = correct_input('Введите количество столбцов матрицы: ', 'int+')
        k = 1
    else:
        n_str = len(m)
        n_col = len(m[0])
        # Проверка входных данных
        # -----------------------------------------
        k = correct_input('Введите номер строки матрицы, на место которой нужно добавить новую строку: ', 'int+')

        while k - 1 > n_str:
            print('Ошибка, под данным номером нет строки в матрице')
            k = correct_input('Введите номер строки матрицы, на место которой нужно добавить новую строку: ', 'int+')

        
        # -----------------------------------------
    new_str = []
    for i in range(n_col):
        elem_input = 'Введите {}-ый элемент новой строки: '.format(i + 1)
        new_str.append(correct_input(elem_input, 'int'))

    m.insert(k - 1, new_str)

    return m 
# добавление столбца алгортмически
def m_add_col_alg(m):

    if len(m) == 0:
        n_str = correct_input('Введите количество строк матрицы: ', 'int+')
        n_col = 0
        k = 1
        m = [[] for i in range(n_str)]

    else:
        n_str = len(m)
        n_col = len(m[0])
        # Проверка входных данных
        # -----------------------------------------
        k = correct_input('Введите номер столбца матрицы, на место которого нужно добавить новый столбец: ', 'int+')

        while k - 1 > n_col:
            print('Ошибка, под данным номером нет столбца в матрице')
            k = correct_input('Введите номер столбца матрицы, на место которого нужно добавить новый столбец: ', 'int+')
        
        # -----------------------------------------
    n_col += 1
    k -= 1
    for i in range(n_str):
        m[i].append(-1)
        for j in range(n_col - 1, k, -1):
            m[i][j] = m[i][j-1]

            
        m[i][k] = correct_input('Введите {}-ый элемент нового столбца: '.format(i + 1), 'int')
    return m
# добавление столбца c использованием функционала python
def m_add_col_python(m):

    if len(m) == 0:
        n_str = correct_input('Введите количество строк матрицы: ', 'int+')
        n_col = 0
        k = 1
        m = [[] for i in range(n_str)]
    else:
        n_str = len(m)
        n_col = len(m[0])
        # Проверка входных данных
        # -----------------------------------------
        k = correct_input('Введите номер столбца матрицы, на место которого нужно добавить новый столбец: ', 'int+')

        while k - 1 > n_col:
            print('Ошибка, под данным номером нет столбца в матрице')
            k = correct_input('Введите номер столбца матрицы, на место которого нужно добавить новый столбец: ', 'int+')
        
        # -----------------------------------------
    
    for i in range(n_str):
        m[i].insert(k-1, correct_input('Введите {}-ый элемент нового столбца: '.format(i + 1), 'int'))
    return m

# удаление столбца алгоритмически
def m_del_col_alg(m):
    # Проверка входных данных
    # -----------------------------------------
    if len(m) == 0:
        print('Ошибка, пустая матрица')
        return m
    n_str = len(m)
    n_col = len(m[0])

    if n_col == 1:
        return []

    k = correct_input('Введите нужный номер столбца матрицы: ', 'int+')
    
    while k > n_col:
        print('Ошибка, под данным номером нет столбца')
        k = correct_input('Введите нужный номер столбца матрицы: ', 'int+')

    # -----------------------------------------

    # удаление элемента

    k -= 1
    for i in range(n_str):
        for j in range(k + 1, n_col):
            m[i][j - 1] = m[i][j]
        del m[i][-1]
    return m

# удаление столбца c использованием функционала python

def m_del_col_python(m):
    # Проверка входных данных
    # -----------------------------------------
    if len(m) == 0:
        print('Ошибка, пустая матрица')
        return m
    n_str = len(m)
    n_col = len(m[0])

    if n_col == 1:
        return []

    k = correct_input('Введите нужный номер столбца матрицы: ', 'int+')
    
    while k > n_col:
        print('Ошибка, под данным номером нет столбца')
        k = correct_input('Введите нужный номер столбца матрицы: ', 'int+')

    # -----------------------------------------

    # удаление элемента

    
    for i in range(n_str):
        m[i].pop(k - 1)
    return m

# удаление строки алгоритмически
def m_del_str_alg(m):
    # Проверка входных данных
    # -----------------------------------------
    if len(m) == 0:
        print('Ошибка, пустая матрица')
        return m

    n_str = len(m)
    n_col = len(m[0])

    if n_str == 1:
        return []

    k = correct_input('Введите нужный номер строки матрицы: ', 'int+')
    
    while k > n_str:
        print('Ошибка, под данным номером нет строки')
        k = correct_input('Введите нужный номер строки матрицы: ', 'int+')
    
    # -----------------------------------------

    # удаление элемента
    k -= 1
    for i in range(k + 1, n_str):
            m[i-1] = m[i]
    del m[-1]
    
    return m 
# удаление строки c использованием функционала python
def m_del_str_python(m):
    # Проверка входных данных
    # -----------------------------------------
    if len(m) == 0:
        print('Ошибка, пустая матрица')
        return m

    n_str = len(m)
    n_col = len(m[0])

    if n_str == 1:
        return []

    k = correct_input('Введите нужный номер строки матрицы: ', 'int+')
    
    while k > n_str:
        print('Ошибка, под данным номером нет строки')
        k = correct_input('Введите нужный номер строки матрицы: ', 'int+')

    # -----------------------------------------

    # удаление элемента
    m.pop(k-1)
    
    return m 
def mx_index(m):
    mx = m[0]
    mx_ind = 0
    for i in range(1, len(m)):
        if mx < m[i]:
            mx = m[i]
            mx_ind = i
    return mx_ind

def mn_index(m):
    mn = m[0]
    mn_ind = 0
    for i in range(1, len(m)):
        if mn > m[i]:
            mn = m[i]
            mn_ind = i
    return mn_ind

# Найти строку, имеющую наибольшее количество повторяющихся элементов
def find_repeat_str(m):
    # Проверка входных данных
    # -----------------------------------------
    if len(m) == 0:
        print('Ошибка, пустая матрица')
        return m
    # -----------------------------------------
    m_temp = []
    
    for i in range(len(m)):
        m_temp.append([])
        
        for j in range(len(m[0])):
            m_temp[i].append(m[i].count(m[i][j]))

   
    for i in range(len(m_temp)):
        m_temp[i] = max(m_temp[i])

    if max(m_temp) == 1:
        print('Нет повторяющихся элементов ни в одной строке')
    else:
        
        for i in range(len(m[0])):
              print('{:<10}'.format(m[mx_index(m_temp)]),end=' ')
        print()

# Переставить местами строки с наибольшим и наименьшим количеством отрицательных элементов
def change_str_mn_mx_minus(m):
    # Проверка входных данных
    # -----------------------------------------
    if len(m) < 2:
        print('Ошибка, в матрице меньше 2 строк')
        return m
    # -----------------------------------------

    n_str = len(m)
    n_col = len(m[0])
    m_temp = [0]*n_str

    for i in range(n_str):
        for j in range(n_col):
            if m[i][j] < 0:
                m_temp[i] += 1

    i_mn = mn_index(m_temp)
    i_mx = mx_index(m_temp)

    m[i_mx], m[i_mn] = m[i_mn], m[i_mx]
    
    return m
# Проверка числа на простоту
def prime(x):
    if x > 0:
        if x == 1:
            return False
        for i in range(2, x//2 + 1):
            if x % i == 0:
                return False
        return True
    return False

# Найти столбец, имеющий наибольшее количество простых чисел
def find_col_max_prime(m):
    # Проверка входных данных
    # -----------------------------------------
    if len(m) == 0:
        print('Ошибка, пустая матрица')
        return m
    # -----------------------------------------
    n_str = len(m)
    n_col = len(m[0])
    m_temp = [0]*n_col

    for i in range(n_str):
        for j in range(n_col):
            if prime(m[i][j]):
                m_temp[j] += 1

    if max(m_temp) == 0:
        print('Нет простых чисел ни в одном столбце')

    else:
        k = mx_index(m_temp)

        for i in range(n_str):
            print(m[i][k])
            
# Переставить местами столбцы с максимальной и минимальной суммой элементов
def change_col_mn_mx_sum(m):
    # Проверка входных данных
    # -----------------------------------------
    if len(m) == 0:
        print('Ошибка, пустая матрица')
        return m
    if len(m[0]) < 2:
        print('Ошибка, в матрице меньше 2 столбцов')
        return m
    # -----------------------------------------

    n_str = len(m)
    n_col = len(m[0])
    m_temp = [0]*n_col

    for i in range(n_str):
        for j in range(n_col):
            m_temp[j] += m[i][j]

    i_mn = mn_index(m_temp)
    i_mx = mx_index(m_temp)

    for i in range(n_str):
        m[i][i_mx], m[i][i_mn] = m[i][i_mn], m[i][i_mx]
    return m

def main():
    m = list()
    while True:
        
        input_text = '(Для вывода меню введите 12). Введите номер функции: '
        f = correct_input(input_text, 'int+')
        
        if f == 1:
            m = m_input(m)
        elif f == 2:
            m = m_add_str_alg(m) # измените _alg на _python для смены способа реализации
        elif f == 3:
            m = m_del_str_alg(m) # измените _alg на _python для смены способа реализации
        elif f == 4:
            m = m_add_col_alg(m) # измените _alg на _python для смены способа реализации
        elif f == 5:
            m = m_del_col_alg(m) # измените _alg на _python для смены способа реализации
        elif f == 6:
            find_repeat_str(m)
        elif f == 7:
            m = change_str_mn_mx_minus(m)
        elif f == 8:
            find_col_max_prime(m)
        elif f == 9:
            m = change_col_mn_mx_sum(m)
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
