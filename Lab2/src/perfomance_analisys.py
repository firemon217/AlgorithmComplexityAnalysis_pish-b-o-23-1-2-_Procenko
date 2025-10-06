import matplotlib.pyplot as plt
import numpy as np
import timeit
from collections import deque
from linked_list import LinkedList


# Сравнение производительности list - LinkedList для вставки
def test_list_insert(n=1000):
    lst = []
    for i in range(n):
        lst.insert(0, i)

def test_linkedlist_insert(n=1000):
    ll = LinkedList()
    for i in range(n):
        ll.insert_at_start(i)

# Сравнение производительности list - deque для очереди
def test_list_queue(n=1000): # Для list
    lst = list(range(n))
    for _ in range(n):
        lst.pop(0)

def test_deque_queue(n=1000): # Для deque
    dq = deque(range(n))
    for _ in range(n):
        dq.popleft()

sizes = [100, 500, 1000, 2000, 5000]   # Разные размеры входных данных
list_insert_times = []
linkedlist_insert_times = []
list_queue_times = []
deque_queue_times = []

for size in sizes:
    print('Размер - {0}'.format(size))
    time_list = timeit.timeit("test_list_insert(size)", globals=globals(), number=10)
    time_linkedlist = timeit.timeit("test_linkedlist_insert(size)", globals=globals(), number=10)

    print("Вставка в начало")
    print(f"list.insert(0, x): {time_list:.6f} сек")
    print(f"LinkedList.insert_at_start(x): {time_linkedlist:.6f} сек\n")

    time_list_q = timeit.timeit("test_list_queue(size)", globals=globals(), number=10)
    time_deque_q = timeit.timeit("test_deque_queue(size)", globals=globals(), number=10)

    print("Очередь")
    print(f"list.pop(0): {time_list_q:.6f} сек")
    print(f"deque.popleft(): {time_deque_q:.6f} сек\n")


for n in sizes:
    # Вставка в начало
    t_list = timeit.timeit(lambda: test_list_insert(n), number=5)
    t_linked = timeit.timeit(lambda: test_linkedlist_insert(n), number=5)
    list_insert_times.append(t_list)
    linkedlist_insert_times.append(t_linked)

    # Очередь
    t_list_q = timeit.timeit(lambda: test_list_queue(n), number=5)
    t_deque_q = timeit.timeit(lambda: test_deque_queue(n), number=5)
    list_queue_times.append(t_list_q)
    deque_queue_times.append(t_deque_q)

plt.figure(figsize=(12, 5))

# list - LinkedList
plt.subplot(1, 2, 1)
plt.plot(sizes, list_insert_times, marker='o', label='list.insert(0, x)')
plt.plot(sizes, linkedlist_insert_times, marker='s', label='LinkedList.insert_at_start(x)')
plt.title("Вставка в начало: list vs LinkedList")
plt.xlabel("Количество элементов (n)")
plt.ylabel("Время выполнения (сек)")
plt.legend()
plt.grid(True)

# list - deque
plt.subplot(1, 2, 2)
plt.plot(sizes, list_queue_times, marker='o', label='list.pop(0)')
plt.plot(sizes, deque_queue_times, marker='s', label='deque.popleft()')
plt.title("Операции очереди: list vs deque")
plt.xlabel("Количество элементов (n)")
plt.ylabel("Время выполнения (сек)")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
