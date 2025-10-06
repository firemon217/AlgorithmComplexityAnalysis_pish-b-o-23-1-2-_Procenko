import timeit
from collections import deque
from linked_list import LinkedList


# Сравнение производительности list vs LinkedList для вставки
def test_list_insert(n=1000):
    lst = []
    for i in range(n):
        lst.insert(0, i)

def test_linkedlist_insert(n=1000):
    ll = LinkedList()
    for i in range(n):
        ll.insert_at_start(i)

time_list = timeit.timeit("test_list_insert()", globals=globals(), number=10)
time_linkedlist = timeit.timeit("test_linkedlist_insert()", globals=globals(), number=10)

print("Вставка в начало")
print(f"list.insert(0, x): {time_list:.6f} сек")
print(f"LinkedList.insert_at_start(x): {time_linkedlist:.6f} сек\n")

# Сравнение производительности list vs deque для очереди
def test_list_queue(n=1000):
    lst = list(range(n))
    for _ in range(n):
        lst.pop(0)

def test_deque_queue(n=1000):
    dq = deque(range(n))
    for _ in range(n):
        dq.popleft()

time_list_q = timeit.timeit("test_list_queue()", globals=globals(), number=10)
time_deque_q = timeit.timeit("test_deque_queue()", globals=globals(), number=10)

print("Очередь")
print(f"list.pop(0): {time_list_q:.6f} сек")
print(f"deque.popleft(): {time_deque_q:.6f} сек")