'''
 Шимшир Эмирджан Османович ИУ7-13Б
 Вариант 21 - 5, 3.

Программа, которая позволит с использованием меню обеспечить работу со строковыми массивами:
1. Очистить список и ввести его с клавиатуры
2. Добавить элемент в произвольное место списка
3. Удалить произвольный элемент из списка (по номеру)
4. Очистить список
5. Поиск элемента наибольшей длины, не содержащего цифр
6. Замена всех заглавных согласных английских букв на строчные
7. Завершение программы

Описание функций:
correct_input - проверяет корректность ввода данных
cheak_int_plus - проверяет корректность ввода целых положительных чисел
clear_add - 1 функция Очистить список и ввести его с клавиатуры
add_in - 2 функция Добавить элемент в произвольное место списка
del_in - 3 функция Удалить произвольный элемент из списка (по номеру)
clear - 4 функция Очистить список
find_max_no_number - 5 функция Поиск элемента наибольшей длины, не содержащего цифр
change - 6 Замена всех заглавных согласных английских букв на строчные

main - основной цикл программы

описание основных веременных:
l - основной список
input_text - введенные данные в виде строки
k - хранит нужный номер элемента в списке
flag - флаг для cheak_int+
big_list - 
f - номер функции

'''
# проверяет корректность ввода данных
def correct_input(input_text):
    text = input(input_text)
    while True:
            if not cheak_int_plus(text):
                print('Ошибка, введите целое положительное число: ')
                text = input(input_text)
            else:
                return int(text)

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

def clear_add(l):
    l = []
    print('Список очищен')
    # Проверка входных данных
    # -----------------------------------------
    input_text = 'Введите количество элементов списка: '
    n = correct_input(input_text)
    # -----------------------------------------
    
    l = [0] * n

    for i in range(n):
        l[i] = input('Введите {}-й элемент списка: '.format(i+1))

    print('Список: {}'.format(l))

    return l

def add_in(l):
    # Проверка входных данных
    # -----------------------------------------
    input_text = 'Введите нужный номер элемента в списке: '
    k = correct_input(input_text)

    if k - 1 > len(l):
        print('Ошибка, под данным номером нет элемента в списке')
        l = add_in(l)
        return l
    # -----------------------------------------
    n = input('Введите элемент, который нужно вставить в нужное место в списке: ')

    l.append(-1)
    k -= 1
    for i in range(len(l) - 1, k, -1):
        l[i] = l[i-1]
    l[k] = n

    print('Список: {}'.format(l))

    return l 


def del_in(l):

    # Проверка входных данных
    # -----------------------------------------
    if len(l) == 0:
        print('Ошибка, нет элементов в списке')
        return l

    input_text = 'Введите нужный номер элемента в списке: '
    k = correct_input(input_text)
    
    if k > len(l):
        print('Ошибка, под данным номером нет элемента в списке')
        l = del_in(l)
        return l

    # -----------------------------------------

    # удаление элемента
    k -= 1
    for i in range(k + 1, len(l)):
            l[i-1] = l[i]
    del l[-1]
        

    print('Список: {}'.format(l))
    return l 

def clear(l):
    # очищение списка
    l = list()
    print('Список пуст')
    return l

def find_max_no_number(l):
    
    len_el_mx = float('-inf')
    el_mx = None
    #массив исходных цифр
    n_list = '1234567890' 
    # Поиск элемента 
    for i in l:
        for j in i:
            if j in n_list:
                break
            
        else:
            if len(i) > len_el_mx:
                len_el_mx = len(i)
                el_mx = i
    if el_mx == None:
        print('Нет такого элемента')
    else:
        print(el_mx)
    return l

def change(l):
    # массив исходных согласных
    big_list = 'QWSXZCDVFRBGTNHMJKLP'
    # замена символов
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j] in big_list:
                l[i] = l[i][:j] + l[i][j].lower() + l[i][j+1:]
    
    print('Список: {}'.format(l))
    return l


def main():
    l = list()
    while True:
        # вывод меню
        print('Меню:')
        print('1. Очистить список и ввести его с клавиатуры')
        print('2. Добавить элемент в произвольное место списка')
        print('3. Удалить произвольный элемент из списка (по номеру)')
        print('4. Очистить список')
        print('5. Поиск элемента наибольшей длины, не содержащего цифр')
        print('6. Замена всех заглавных согласных английских букв на строчные')
        print('7. Завершение программы')
        

        input_text = 'Введите номер функции: '
        f = correct_input(input_text)
        
        
        
        if f == 1:
            l = clear_add(l)
        elif f == 2:
            l = add_in(l)
        elif f == 3:
            l = del_in(l)
        elif f == 4:
            l = clear(l)
        elif f == 5:
            l = find_max_no_number(l)
        elif f == 6:
            l = change(l)
        elif f == 7:
            break
        else:
            print('Ошибка, нет такой функции')


main()
