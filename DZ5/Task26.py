a = int(input("Введите число "))
b = int(input("Введите степень числа(целое неотрицательно число) "))

def func(a, b):
    if b == 0:
        return 1

    return a * func(a, b - 1)

print(func(a, b))