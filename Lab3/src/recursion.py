def factorial(n: int) -> int:
    """Вычисление факториала числа n рекурсивно."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Временная сложность: O(n)
# Глубина рекурсии: O(n)


def fibonacci(n: int) -> int:
    """Рекурсивное вычисление n-го числа Фибоначчи."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Временная сложность: O(2^n)
# Глубина рекурсии: O(n)


def fast_power(a: float, n: int) -> float:
    """Быстрое возведение числа a в степень n (через деление степени на 2)."""
    if n == 0:
        return 1
    if n % 2 == 0:
        half = fast_power(a, n // 2)
        return half * half
    else:
        return a * fast_power(a, n - 1)

# Временная сложность: O(log n)
# Глубина рекурсии: O(log n)
