from collections import deque

# Проверка сбалансированности скобок с использованием стека
def is_balanced_brackets(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack

# Симуляция очереди печати (используем deque)
def print_queue_simulation(jobs):
    queue = deque(jobs)
    while queue:
        current = queue.popleft()
        print(f"Печатается задание: {current}")
    print("Все задания напечатаны.")

# Проверка палиндрома (используем deque)
def is_palindrome(s):
    dq = deque(s.lower().replace(" ", ""))
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

# Пример использования
if __name__ == "__main__":
    # Проверка скобок
    expr = "{[()()]}"
    print(f"Строка {expr} сбалансирована? ->", is_balanced_brackets(expr))

    # Очередь печати
    print("\nОчередь печати:")
    print_queue_simulation(["Документ1", "Отчёт", "Скан"])

    # Палиндром
    word = "шалаш"
    print(f"\n'{word}' -> палиндром? ->", is_palindrome(word))