def is_float(n):  # Проверка флоат ли числовое значение введенной строки
    if (n.count('e') == 1 and n.count('E') == 0) or (n.count('e') == 0
                                                     and n.count('E') == 1):
        n = n.lower()
        if n.count('.e') != 0 or n.count('e.') != 0: return False
        e_val = n.split('e')
        if len(e_val) == 2:

            if (e_val[1]).isdigit():
                val = e_val[0].split('.')
                if len(val) == 1 and e_val[0].isdigit():
                    return True
                elif len(val) == 2 and val[0].isdigit() and val[1].isdigit():
                    return True
                else:
                    return False
            elif (e_val[1][1:]).isdigit() and e_val[1][0] == '-':
                val = e_val[0].split('.')
                if len(val) == 1 and e_val[0].isdigit():
                    return True
                elif len(val) == 2 and val[0].isdigit() and val[1].isdigit():
                    return True
                else:
                    return False
            else:
                return False
    elif n.isdigit():
        return True
    else:
        val = n.split('.')
        if len(val) == 1 and n[0].isdigit():
            return True
        elif len(val) == 2 and val[0].isdigit() and val[1].isdigit():
            return True
        else:
            return False


def is_int(n):
    # Если у числа есть знак
    if n[0] == '+' or n[0] == '-':
        n = n[1:]
    return n.isdigit()


def input_rauzh(st, typ):  # ввод числа
    n = input(st)
    n = n.replace(',', '.')
    while True:
        # Если пустая строка
        if not n:
            n = input(st)
        # Если нужно целое число
        elif typ == 'int':
            if is_int(n):
                return int(n)
            else:
                print('Введите целое число.')
                n = input(st)
        elif typ == 'natural':
            if n.isdigit():
                return int(n)
            elif n[0] == '0' and n[1:].isdigit():
                return int(n)
            else:
                print('Введите натуральное число.')
                n = input(st)
        elif typ == 'float':
            if n == 'stop':
                return n
            elif n[0] == '-' and is_float(n[1:]):
                return float(n)
            elif is_float(n):
                return float(n)
            else:
                print('Введите действительное число.'); n = input(st)
        elif typ == 'symbol':
            if len(n) == 1:
                return n
            else:
                print('Введите 1 символ.'); n = input(st)
