import os

def binary_search(arr, target, left=0, right=None):
    """Рекурсивный бинарный поиск."""
    if right is None: # Инициализация правой границы O(1)
        right = len(arr) - 1
    if left > right: # Проверка границ O(1)
        return -1
    mid = (left + right) // 2 # Вычисление среднего индекса O(1)
    if arr[mid] == target: # Проверка на равенство O(1)
        return mid # Элемент найден O(1)
    elif arr[mid] > target: # Рекурсивный вызов для левой половины O(log n)
        return binary_search(arr, target, left, mid - 1) 
    else: # Рекурсивный вызов для правой половины O(log n)
        return binary_search(arr, target, mid + 1, right)

# Временная сложность: O(log n)
# Глубина рекурсии: O(log h)


def walk_directory(path, indent=0):
    """Рекурсивный обход файловой системы с выводом дерева каталогов и файлов."""
    if not os.path.exists(path): # Проверка существования пути O(1)
        print("Путь не существует") # O(1)
        return 
    for item in os.listdir(path): # Перебор элементов в каталоге O(N)
        full_path = os.path.join(path, item) # Полный путь к элементу O(1)
        print(" " * indent + f"- {item}") # Вывод элемента с отступом O(1)
        if os.path.isdir(full_path): # Проверка, является ли элемент каталогом O(1)
            walk_directory(full_path, indent + 2) # Рекурсивный вызов для подкаталога O(n)

# Временная сложность: O(N), где N — количество файлов и папок
# Глубина рекурсии: O(H), где H — максимальная глубина вложенности каталогов


def hanoi(n, source="A", target="C", auxiliary="B"):
    """Решение задачи Ханойских башен для n дисков."""
    if n == 1:
        print(f"Переместить диск 1 с {source} на {target}")
        return
    hanoi(n - 1, source, auxiliary, target)
    print(f"Переместить диск {n} с {source} на {target}")
    hanoi(n - 1, auxiliary, target, source)

# Временная сложность: O(2^n)
# Глубина рекурсии: O(h)
