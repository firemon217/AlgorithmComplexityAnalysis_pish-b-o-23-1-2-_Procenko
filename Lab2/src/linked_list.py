class Node:
    """Класс узла списка"""
    def __init__(self, data):
        self.data = data    # O(1)
        self.next = None    # O(1)

class LinkedList:
    """Класс связного списка"""
    def __init__(self):
        self.head = None    # Первый элемент списка O(1)
        self.tail = None    # Хвост списка для вставки в конце O(1)
        self.size = 0    # Размер O(1)

    def insert_at_start(self, data):
        """Добавление элемента в начало"""
        new_node = Node(data)    # Создание узла O(1) + 0(1)
        new_node.next = self.head   # Передаем ссылку на элемент, который ранее был первым 0(1)
        self.head = new_node    # Ставим элемент как голову списка 0(1)
        if self.tail is None:   # Если хвост пустой 0(1)
            self.tail = new_node   # Назначаем элемент 0(1)
        self.size += 1  # Увеличиваем поле размера 0(1)
    # Итог 0(1)

    def insert_at_end(self, data):
        """Добавление элемента в конец"""
        new_node = Node(data)   # Создание узла O(1) + 0(1)
        if not self.head:   # Если головы нет 0(1)
            self.head = self.tail = new_node    # Назначаем эелемнт как голову и хвост 0(1)
        else:   # Если голова есть 0(1)
            self.tail.next = new_node   # Назначаем хвосту ссылку на новый элемент 0(1)
            self.tail = new_node    # Новый элемент становится хвостом 0(1)
        self.size += 1 # Увеличиваем поле размера 0(1)
    # Итог 0(1)

    def delete_from_start(self):
        """Удаление элемента из начала"""
        if not self.head:   # Если головы нет 0(1)
            return None    # Выходим из функции, удалять нечего 0(1)
        data = self.head.data   # Иначе назначаем возврат головы 0(1)
        self.head = self.head.next   # Иначе назначаем возврат головы 0(1)
        if not self.head:   # Если список стал пустым O(1)
            self.tail = None    # Убираем ссылку на хвост O(1)
        self.size -= 1   # Уменьшаем счётчик размера списка O(1)
        return data    # Возвращаем последний элемент
    # Итог 0(1)

def traversal(self):
    """Обход списка"""
    result = []    # Создаём пустой список, куда будем складывать значения узлов O(1)
    current = self.head    # Начинаем обход с головы списка (первого узла) O(1)
    while current:    # Пока текущий элемент существует (не достигнут конец списка) O(n) — цикл выполняется n раз
        result.append(current.data)    # Добавляем значение текущего узла в список результатов O(1) на каждой итерации
        current = current.next    # Переходим к следующему узлу по ссылке next O(1) на каждой итерации
    return result    # Возвращаем итоговый список значений после обхода O(1)
    # Итоговая O(n)