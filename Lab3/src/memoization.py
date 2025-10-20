import time
from recursion import fibonacci

# Мемоизированная версия
def fibonacci_memo(n: int, memo=None) -> int:
    if memo is None: # Инициализация словаря мемоизации при первом вызове O(1)
        memo = {} # O(1)

    if n == 0: # Базовые случаи
        return 0 # O(1)
    if n == 1: # O(1) 
        return 1 # O(1)
    
    if n in memo: # Проверяем, не вычисляли ли мы уже это значение
        return memo[n] # O(1)

    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo) # Рекурсивный шаг с сохранением результата O(n)
    return memo[n] # O(1)

# Сравнение производительности
if __name__ == "__main__":
    n = 35

    start = time.time()
    print(f"Наивный Фибоначчи({n}) = {fibonacci(n)}")
    print(f"Время работы (наивный): {time.time() - start:.4f} сек")

    start = time.time()
    print(f"Мемоизированный Фибоначчи({n}) = {fibonacci_memo(n)}")
    print(f"Время работы (мемоизация): {time.time() - start:.4f} сек")
