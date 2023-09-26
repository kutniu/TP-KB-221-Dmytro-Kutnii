# Введення даних
value1 = float(input("Введіть перше значення: "))
value2 = float(input("Введіть друге значення: "))
operation = input("Введіть операцію (+, -, *, /): ")

# Виконання дій
if operation == '+':
    result = value1 + value2
    print(f"{value1} + {value2} = {result}")
elif operation == '-':
    result = value1 - value2
    print(f"{value1} - {value2} = {result}")
elif operation == '*':
    result = value1 * value2
    print(f"{value1} * {value2} = {result}")
elif operation == '/':
    # Перевірка ділення на нуль
    if value2 == 0:
        print("Ділення на нуль не дозволено.")
    else:
        result = value1 / value2
        print(f"{value1} / {value2} = {result}")
else:
    print("Невірний ввід даних. Будь ласка, введіть +, -, *, або /.")
