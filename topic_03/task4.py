def find_insert_position(sorted_list, new_element):
    left, right = 0, len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == new_element:
            return mid  # Елемент вже присутній у списку
        elif sorted_list[mid] < new_element:
            left = mid + 1
        else:
            right = mid - 1

    return left  # Повертаємо позицію для вставки нового елементу

# Приклад використання:
sorted_list = [1, 3, 5, 7, 9]
new_element = 6
position = find_insert_position(sorted_list, new_element)
print(f"Елемент {new_element} має бути вставлений на позицію {position}")
