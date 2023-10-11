def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        raise ValueError("Ділення на нуль неможливе")
    return x / y

while True:
    try:
        operation = input("Виберіть операцію (+, -, *, /) або 'q' для виходу: ")
        
        if operation == 'q':
            break
        
        if operation not in '+-*/':
            print("Невірна операція. Будь ласка, виберіть операцію зі списку.")
            continue

        x = float(input("Введіть перше число: "))
        y = float(input("Введіть друге число: "))

        if operation == '+':
            result = addition(x, y)
        elif operation == '-':
            result = subtraction(x, y)
        elif operation == '*':
            result = multiplication(x, y)
        else:
            result = division(x, y)

        print(f"Результат: {result}")

    except ValueError as e:
        print(f"Помилка: {e}")
    except ZeroDivisionError:
        print("Помилка: Ділення на нуль неможливе")
    except Exception as e:
        print(f"Сталася помилка: {e}")
