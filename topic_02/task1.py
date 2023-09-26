import math

def solve_quadratic(a, b, c):
    # Обчислюємо дискримінант
    D = b**2 - 4*a*c
    
    if D < 0:
        # Розв'язок не існує для D < 0
        return "Розв'язків немає"
    elif D == 0:
        # Один розв'язок, що повторюється для D == 0
        x = -b / (2*a)
        return f"Один розв'язок: x = {x}"
    else:
        # Два розв'язки для D > 0
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        return f"Два розв'язки: x1 = {x1}, x2 = {x2}"

# Введення даних
a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
c = float(input("Введіть c: "))

result = solve_quadratic(a, b, c)
print(result)
