# Шимшир Эмирджан
# ИУ7-13Б

# Пузырьковая с флагом
# Сравниваем элементы попарно и максимальный перемещается в конец на каждом проходе
def bubble_sort_F(array): 
    n = len(array) 
    for i in range(n - 1): 
        flag = True # Отсортирован ли список
        for j in range(n - 1 - i): # Максимальный элемент переходит в конец списка
            if array[j] > array[j + 1]: # Попарное сравнение элементов
                array[j],array[j+1] = array[j+1],array[j] 
                flag = False
        if flag: # Если элементы не переставлялись, список отсортирован
            break
    


def main():
	print("Пузырьковая сортировка с флагом")
	array = list(map(int, input("Введите нужные числа через пробел: ").split()))
	bubble_sort_F(array)
	print("Отсортированный список: ")
	print(*array)

main()
