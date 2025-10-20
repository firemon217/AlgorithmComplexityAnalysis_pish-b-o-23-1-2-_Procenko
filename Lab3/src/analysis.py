import time
import matplotlib.pyplot as plt
from recursion import fibonacci
from memoization import fibonacci_memo 
from recursion_tasks import walk_directory, hanoi
import os

# 1. Экспериментальное исследование времени вычисления Фибоначчи
n_values = [10, 20, 25, 30, 35]
times_naive = []
times_memo = []

for n in n_values:
    start = time.time()
    fibonacci(n)
    end = time.time() - start
    times_naive.append(end)
    print( f"time for fibonacci - {end}" )

    start = time.time()
    fibonacci_memo(n)
    end = time.time() - start
    times_memo.append(end)
    print( f"time for memo fibonacci - {end}" )

# 2. Визуализация времени выполнения
plt.figure(figsize=(10, 6))
plt.plot(n_values, times_naive, marker='o', label='Наивный Фибоначчи')
plt.plot(n_values, times_memo, marker='o', label='Мемоизированный Фибоначчи')
plt.xlabel('n')
plt.ylabel('Время выполнения (сек)')
plt.title('Сравнение времени выполнения рекурсивного вычисления Фибоначчи')
plt.legend()
plt.grid(True)
plt.savefig('fibonacci_time_comparison.png')
plt.show()

# Пример использования (заменить 'root_dir' на путь к вашей тестовой директории)
root_dir = '.'  # текущий каталог
max_depth = walk_directory(root_dir)
print(f"Максимальная глубина рекурсии для обхода файловой системы: {max_depth}")

# 4. Ханойские башни
print("\nРешение задачи Ханойских башен для n=3")
hanoi(3)

# 5. Анализ результатов
print("\nАнализ результатов:")
print("Наивный алгоритм Фибоначчи имеет экспоненциальный рост времени выполнения O(2^n),")
print("потому что каждая функция вызывает две предыдущие функции рекурсивно, что ведет к множественному пересчету одних и тех же значений.")
print("Мемоизация изменяет сложность до линейной O(n), так как каждое значение вычисляется только один раз и сохраняется в словаре.")
