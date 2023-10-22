data = [{'name': 'John', 'grade': 40},
        {'name': 'Emily', 'grade': 35},
        {'name': 'Michael', 'grade': 88},
        {'name': 'David', 'grade': 22},
        {'name': 'Sophia', 'grade': 30},
        {'name': 'Oliver', 'grade': 55}]

parameter = input("Виберіть ключ для сортування (name або grade): ")
reverse_sort = input("Сортувати від більшого до меншого (yes/no)? ").lower()

reverse = False
if reverse_sort == 'yes':
    reverse = True

def sort_data(data, parameter, reverse):
    if parameter == 'name':
        return sorted(data, key=lambda x: x['name'], reverse=reverse)
    elif parameter == 'grade':
        return sorted(data, key=lambda x: x['grade'], reverse=reverse)
    else:
        print("Неправильний ключ сортування.")
        return data

sorted_data = sort_data(data, parameter, reverse)

for item in sorted_data:
    print(f"Name: {item['name']}, Grade: {item['grade']}")
