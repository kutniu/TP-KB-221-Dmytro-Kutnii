def insert_into_sorted_list(arr, target):
    sorted_arr = sorted(arr + [target])
    index = sorted_arr.index(target)
    arr[:] = sorted_arr 
    return index


sorted_list = [1, 3, 5, 7, 9]
new_element = 4
position = insert_into_sorted_list(sorted_list, new_element)
print("Позиція для вставки:", position)
print("Оновлений список:", sorted_list)
