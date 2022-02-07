# Метод простого выбора
# Перегоняем по одному минимальному элементу в начало списка
def selection_sort(arr):
    for i in range(len(arr)):
        min_ind = i # Индекс минимального элемента в начале неотсортированной части
        for j in range(i + 1,len(arr)):
            if arr[j] < arr[min_ind]: 
                min_ind = j
        arr[i],arr[min_ind] = arr[min_ind],arr[i] # Минимальный элемент переставляем с текущим
    return arr


# Пузырьковая с флагом
# Сравниваем элементы попарно и максимальный перемещается в конец на каждом проходе
def bubble_sort_with_flag(arr): 
    n = len(arr) 
    for i in range(n - 1): 
        flag = True # Отсортирован ли список
        for j in range(n - 1 - i): # Максимальный элемент переходит в конец списка
            if arr[j] > arr[j + 1]: # Попарное сравнение элементов
                arr[j],arr[j+1] = arr[j+1],arr[j] 
                flag = False
        if flag: # Если элементы не переставлялись, список отсортирован
            break
    return arr


# Сортировка вставками
# В отсортированную часть вставляем элементы по очереди
def insertion_sort(alist):
    for i in range(1, len(alist)):
        temp = alist[i] # Поочерёдно проходим по элементам массива
        j = i - 1 # Берём предыдущий индекс (последний индекс в отсортированном массиве)
        while (j >= 0 and temp < alist[j]): # Пока этот индекс не вышел за пределы массива или текущий элемент меньше элемента из отсортированного массива
            alist[j + 1] = alist[j] # Переставляем элементы отсортированного массива на один вправо
            j = j - 1 # Новый индекс сравниваемого элемента сдвигаем на один влево
        alist[j + 1] = temp # Вставляем наш элемент на его место
    return alist

# Вставка с барьером
def insertionsortwithbarrier(arr): 
    arr = [0] + arr # Добавляем место для текущего элемента
    for i in range(1, len(arr)): 
        arr[0] = arr[i] # Ставим текущий элемент в нулевую позицию
        j = i - 1 # Проходимся с текущего элемента и ищем место, на которое нам нужно вставить этот элемент
        while (arr[0] < arr[j]):
            arr[j + 1] = arr[j] 
            j= j- 1
        arr[j + 1] = arr[0] # Ставим текущий элемент в нужное место
    return arr[1:]


# Вставки с бинарным поиском
def insertion_sort_with_bin_search(arr): 
    for i in range(1, len(arr)):
        temp = arr[i] # Берём текущий элемент
        left, right = 0, i # Границы отсортированного списка
        # if lo == hi: 
        #     lo += 1 
        # else:
        while left < right: # пока левая граница меньше правой
            mid = (left + right)//2 # Идём с середины и сдвигаем границы, уменьшая область вставки
            if temp < arr[mid]: 
                right = mid 
            else: 
                left = mid + 1
        j = i
        while (j > left and j > 0): # Вставляем элемент на левую границу, смещая все остальные
            arr[j] = arr[j-1] 
            j = j - 1
        arr[left] = temp
    return arr


# Сортировка Шелла (вставка с шагом)
def Shell_sort(arr):
    step = len(arr) // 2 # Задаём начальный шаг сортировки
    while step:
        for i, el in enumerate(arr): # Проходимся по всем элементам
            while i >= step and arr[i - step] > el: # Сортируем с шагом
                arr[i] = arr[i - step]
                i -= step
                arr[i] = el
        step = 1 if step == 2 else int(step * 5.0 / 11) # Меняем шаг
    return arr
 

# Сортировка расческой (пузырёк с шагом)
def comb(mas):
    step = len(mas)
    changes = True
    while step > 1 or changes:
        step = max(1, int(step / 1.25))  # minimum gap is 1
        changes = False
        for i in range(len(data) - mas): 
            j = i + step
            if mas[i] > mas[j]: # переставляем попарные элементы с шагом
                mas[i], mas[j] = mas[j], mas[i]
                changes = True
    return mas


# ѓномья сортировка
def gnome(data):
    i, size = 1, len(data)
    while i < size:
        if data[i - 1] <= data[i]: # если отсортировано, двигаемся дальше
            i += 1
        else:
            data[i - 1], data[i] = data[i], data[i - 1] # иначе меняем элементы местами и смещаемся на 1 назад, если это возможно
            if i > 1:
                i -= 1
    return data


# Реализация пирамидальной сортировки на Python
# Нахождение корня 
def heapify(array, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    
    if l < n and array[i] < array[l]:
        largest = l
    if r < n and array[largest] < array[r]:
        largest = r
    
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)
    return array
        
def heapSort(array):
    n = len(array)
    for i in range(n//2, -1, -1): # Строим дерево, в котором каждый потомок меньше родителя
        heapify(array, n, i)
    for i in range(n-1, 0, -1): # Поочерёдно убираем максимальные элементы в конец массива, ставя на их место прошлый элемент
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
    return array


# Шейкерная сортировка
def shakersort(arr): 
    left = 0
    right = len(arr) - 1
    while left < right: 
        r_new = left
        for i in range(left,right): # Смотрим только в неотсортированной части
            if arr[i] > arr[i+1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i] 
                r_new = i
        right = r_new # перемещаем границу до неотсортированной части

        l_new = right
        for i in range(right - 1, left - 1, -1):
            if (arr[i] > arr[i+1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i] 
                l_new = i
        left = l_new
    return arr




    #__________________________________________________________________________________________


