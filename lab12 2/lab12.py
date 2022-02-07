'''


'''

import os
import num_check as nc


def give_birth(filename):
    file = open(filename, 'w+')
    file.close()
    print('Вами был создан файл "' + filename + '"')


def file_choice():
    while True:
        print('Файл, который вы хотите выбрать, существует?')
        choice_1 = input('Да/Нет (+/-): ')
        if choice_1 in ['Да', 'да', 'yes', 'Yes', 'существует', '1', 'exist', '+']:
            filename = input('Введите имя файла (путь к нему, если хотите создать не в папке программы): ')
            if filename[-4:] != '.txt': filename += '.txt'
            if os.path.exists(filename):
                print('Вами был выбран файл "' + filename + '"')
            else:
                print('Вы ошиблись, такого файла нет. Будет создан файл с таким именем и местоположением.')
                give_birth(filename)
        if choice_1 in ['Нет', 'нет', 'no', 'No', 'не существует', '0', '-']:
            print('В таком случае мы создадим пустой файл.')
            filename = input('Введите имя файла (путь к нему, если хотите создать не в папке программы): ')
            if filename[-4:] != '.txt': filename += '.txt'
            if os.path.exists(filename):
                print('Файл "' + filename + '" уже существует и был выбран Вами.')
            else:
                print('Будет создан файл с таким именем и местоположением.')
                give_birth(filename)
        return filename


# Нельзя хранить ДБ целиком, но можно хранить ифнормацию о каждой ячейке)()()))()()
def info_for_db_output(filename):
    with open(filename, 'r') as f:
        db = []
        st = []
        for line in f:
            for elem in line.strip().split(';'):
                st.append(len(elem))
            db.append(st)
            st = []
    info_of_cols = []
    trans_db = list(zip(*db))
    for i in range(len(trans_db)):
        info_of_cols.append(max(trans_db[i]))
    return info_of_cols


def db_output(filename):
    info_of_cols = info_for_db_output(filename)
    with open(filename, 'r') as f:

        for line in f:
            st = line.strip().split(';')
            for i in range(len(info_of_cols)):
                print('{:<{width}}'.format(st[i], width=info_of_cols[i] + 1), end=' ')
            print()


def db_input(filename, num_of_pols, num_of_recs):
    print('Сейчас Вам предстоит ввод БД в файл.')
    print(
        'Для справки: разделителем явлется символ ";", но Вам вводить его не требуется.',
        'Ввод осуществляется путем ввода записи, причем каждого ее поля с новой строки после приглашения.')
    with open(filename, 'w') as f:
        for j in range(num_of_recs):
            st = ''
            for i in range(num_of_pols):
                cell = input('Введите {}-ое поле {}-й записи: '.format(i + 1, j + 1))
                cell = cell.replace(';', '')  # на случай ввода не по правилам
                st += cell + ';'
            st = st[:-1]
            f.write(st + '\n')


def db_initialize(filename):
    if os.path.exists(filename):
        print('Файл "' + filename + '" был очищен.')
        num_of_pols = nc.input_rauzh('Введите число полей: ', 'natural')
        num_of_recs = nc.input_rauzh('Введите число записей: ', 'natural')
        db_input(filename, num_of_pols, num_of_recs)
    else:
        print('Такого файла нет. Был создан файл с таким именем и местоположением.')
        give_birth(filename)
        num_of_pols = nc.input_rauzh('Введите число полей: ', 'natural')
        num_of_recs = nc.input_rauzh('Введите число записей: ', 'natural')
        db_input(filename, num_of_pols, num_of_recs)


def add_rec(filename):
    print('Сейчас будет добавлена запись в', '"' + filename + '".')
    mem = len(info_for_db_output(filename))
    print(mem)
    with open(filename, 'a') as f:
        st = ''
        for i in range(mem):
            cell = input('Введите {}-ое поле: '.format(i + 1))
            cell = cell.replace(';', '')  # на случай ввода не по правилам
            st += cell + ';'
        st = st[:-1]
        f.write('\n' + st)


def search_by_1_field(filename):
  print('Вами был выбран пункт поиска записи по одному полю.')
  print('В случае, если введенному Вами полю соответствует несколько записей, будут выведены на экран все таковые.')
  field = input('Введите поле, по которому будет осуществлен поиск: ')
  with open(filename , 'r') as f:
    k=0
    for line in f:
      st = line.strip().split(';')
      for each in st:
        if each == field:
          k+=1
          print(*st)
    if k == 0: print('Записи по указанному полю не найдены.')


def search_by_2_fields(filename):
  print('Вами был выбран пункт поиска записи по двум полям.')
  print('В случае, если введенным Вами полям соответствует несколько записей, будут выведены на экран все таковые.')
  field_1 = input('Введите первое поле, по которому будет осуществлен поиск: ')
  field_2 = input('Введите второе поле, по которому будет осуществлен поиск: ')
  with open(filename , 'r') as f:
    k = 0
    for line in f:
      st = line.strip().split(';')
      for i in range(len(st)):
        if st[i] == field_1:
          for j in range(len(st)):
            if j != i and st[j] == field_2:
              k += 1
              print(*st)

    if k == 0: print('Записи по указанному полю не найдены.')


def main():
    print('Добро пожаловать в меню работы с файлом! Ознакомьтесь с нашими возможностями:')
    print('По умолчанию выбран файл "F1_tracks.txt"')
    filename = 'F1_tracks.txt'
    while True:
        print('\nВыбран файл', '"' + filename + '".',
              '\n1. Выбрать файл для работы',
              '\n2. Инициализировать базу данных',
              '\n3. Вывести содержимое базы данных',
              '\n4. Добавить запись в базу данных',
              '\n5. Поиск по одному полю',
              '\n6. Поиск по двум полям',
              '\nЛюбой символ, не являющийся цифрой от 1 до 6 будет расчитан как кнопка выхода из программы.\n')
        menu = input('Выберите пункт меню: ')
        if menu == '1':
            filename = file_choice()
        if menu == '2':
            print('Вы хотите инициализировать выбранный файл(1) или другой(0)?')
            choice = input('1/0: ')
            while not choice in ['1', '0']:
                choice = input('1/0: ')
            if choice == '0':
                filename = input('Введите имя (полное, если файл не в папке программы) файла для инициализации: ')
                if filename[-4:] != '.txt': filename += '.txt'
                print('Сейчас будет инициализирован файл', '"' + filename + '".')
                db_initialize(filename)
            else:
                print('Сейчас будет инициализирован файл', '"' + filename + '".')
                db_initialize(filename)
        if menu == '3':
            print('Вывод содержимого файла', filename + ':')
            db_output(filename)
        if menu == '4':
            add_rec(filename)
        if menu == '5':
            search_by_2_fields(filename)
        if menu == '6':
            if menu == '5':
                search_by_1_field(filename)



if __name__ == '__main__':
    main()
