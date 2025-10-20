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


def walk_directory(path, indent=0, current_depth=1):
    """Рекурсивный обход файловой системы с выводом дерева каталогов и файлов."""
    if not os.path.exists(path):
        print("Путь не существует")
        return 0
    max_found_depth = current_depth
    for item in sorted(os.listdir(path)):
        full_path = os.path.join(path, item)
        print(" " * indent + f"- {item} - {current_depth}")
        if os.path.isdir(full_path):
            sub_depth = walk_directory(full_path, indent + 2, current_depth + 1)
            max_found_depth = max(max_found_depth, sub_depth)
    return max_found_depth

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
