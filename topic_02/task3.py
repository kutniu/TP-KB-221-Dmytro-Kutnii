def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Ділення на нуль не дозволено."
    return x / y

def calculator_match(value1, value2, operation):
     match operation:
        case '+': return add(value1, value2)
         
        case '-': return subtract(value1, value2)
         
        case '*': return multiply(value1, value2)
         
        case '/': return divide(value1, value2)
         
        case _: return "Невірний ввід даних. Будь ласка, введіть +, -, *, або /."

# Введення даних
value1 = float(input("Введіть перше значення: "))
value2 = float(input("Введіть друге значення: "))
operation = input("Введіть операцію (+, -, *, /): ")

result = calculator_match(value1, value2, operation)
print(f"Результат: {result}")