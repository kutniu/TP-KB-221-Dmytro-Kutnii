from functions import add, subtract, multiply, divide

def get_numbers():
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))
    return a, b

def perform_addition():
    a, b = get_numbers()
    result = add(a, b)
    print("Результат додавання:", result)

def perform_subtraction():
    a, b = get_numbers()
    result = subtract(a, b)
    print("Результат віднімання:", result)

def perform_multiplication():
    a, b = get_numbers()
    result = multiply(a, b)
    print("Результат множення:", result)

def perform_division():
    a, b = get_numbers()
    result = divide(a, b)
    print("Результат ділення:", result)
