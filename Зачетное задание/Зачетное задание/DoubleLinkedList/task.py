from typing import Any, Iterable, Optional, Iterator


from node import Node, DoubleLinkedNode


class LinkedList:
    def __init__(self, data: Iterable = None):
        self.len = 0
        self.head: Optional[Node] = None
        self.tail = self.head

        if data is not None:
            for value in data:
                self.append(value)

    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        append_node = Node(value)

        if self.head is None:
            self.head = self.tail = append_node
        else:
            self.linked_nodes(self.tail, append_node)
            self.tail = append_node

        self.len += 1

    def step_by_step_on_nodes(self, index: int) -> Node:
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.len:  # для for
            raise IndexError()

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        left_node.next = right_node

    def __getitem__(self, index: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        return node.value

    def __setitem__(self, index: int, value: Any) -> None:
        """ Метод устанавливает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        node.value = value

    def to_list(self) -> list:
        return [linked_list_value for linked_list_value in self]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_list()})"

    def __str__(self) -> str:
        return f"{self.to_list()}"

    def nodes_iterator(self) -> Iterator[Node]:
        current_node = self.head
        for _ in range(self.len):
            yield current_node
            current_node = current_node.next

    def clear(self):
        self.head = None
        self.tail = None

        self.len = 0


class DoubleLinkedList(LinkedList):
    @staticmethod
    def linked_nodes(left_node: DoubleLinkedNode, right_node: Optional[DoubleLinkedNode] = None) -> None:
        left_node.next = right_node
        right_node.prev = left_node

    def insert(self, x, value):
        new_node = DoubleLinkedNode(value)
        node = self.step_by_step_on_nodes(x)
        prev_node = self.step_by_step_on_nodes(x - 1)
        prev_node.next = new_node
        new_node.prev = prev_node
        node.prev = new_node
        new_node.next = node
        self.len += 1

    def count_(self, x):
        count = 0
        i = None
        y = DoubleLinkedList.nodes_iterator(self)
        for _ in range(self.len):
            i = next(y)
            if i.value == x:
                count += 1

        return count


if __name__ == "__main__":
    list_ = [1, 2, 3, 4, 5, 6, 7]
    lll = DoubleLinkedList(list_)
    print(lll)
    lll.insert(1, 5)
    print(lll)
    c = lll.count_(1)
    print(c)

