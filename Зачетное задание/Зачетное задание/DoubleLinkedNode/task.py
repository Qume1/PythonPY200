from typing import Any, Optional


class Node:
    def __init__(self, value: Any, next_: Optional["Node"] = None):

        self.value = value
        self.next = next_

    def __repr__(self) -> str:
        return f"Node({self.value}, {None})" if self.next is None else f"Node({self.value}, Node({self.next}))"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def is_valid(cls, node: Any) -> None:
        if not isinstance(node, (type(None), cls)):
            raise TypeError

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, node):
        self.is_valid(node)
        self._next = node


class DoubleLinkedNode(Node):
    def __init__(self, value, next_, prev):
        super().__init__(value, next_)
        self.prev = prev

    def __repr__(self):
        next_repr: str = str(None) \
            if self.next is None \
            else f"DoubleLinkedNode({self.next.value}, {None}, {None})"
        prev_repr: str = str(None) \
            if self.next is None \
            else f"DoubleLinkedNode({self.prev.value}, {None}, {None})"
        return f"DoubleLinkedNode({self.value}, {next_repr}, {prev_repr})"

    def __str__(self):
        return super().__str__()



if __name__ == "__main__":
    ...
