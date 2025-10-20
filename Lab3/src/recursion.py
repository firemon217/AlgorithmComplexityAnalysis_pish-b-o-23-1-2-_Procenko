def factorial(n: int) -> int:
    """Вычисление факториала числа n рекурсивно."""
    if n == 0 or n == 1: # Базовые случаи
        return 1
    return n * factorial(n - 1)

# Временная сложность: O(n)
# Глубина рекурсии: O(h)


def fibonacci(n: int) -> int:
    """Рекурсивное вычисление n-го числа Фибоначчи."""
    if n <= 1: # Базовые случаи 
        return n
    return fibonacci(n - 1) + fibonacci(n - 2) # Временная сложность: O(2^n)

# Временная сложность: O(2^n)
# Глубина рекурсии: O(h)


def fast_power(a: float, n: int) -> float:
    """Быстрое возведение числа a в степень n (через деление степени на 2)."""
    if n == 0: # Базовые случаи 
        return 1
    if n % 2 == 0:
        half = fast_power(a, n // 2) # Рекурсивный вызов
        return half * half
    else: # n нечетное
        return a * fast_power(a, n - 1) # Рекурсивный вызов

# Временная сложность: O(log n)
# Глубина рекурсии: O(log h)