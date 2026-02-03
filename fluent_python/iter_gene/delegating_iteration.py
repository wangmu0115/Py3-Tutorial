"""Delegating Iteration

Problem:
    You have built a custom container object that internally holds a list, tuple, or some other iterable.
    You would like to make iteration work with your new container.

Solution:
    iter()
    __iter__()
    __next__()
"""


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return f"{self.__class__.__name__}(value={self._value!r}, children={self._children!r})"

    def add_child(self, child: Node):
        self._children.append(child)

    def __iter__(self):
        """Python's iterator protocol requires `__iter__()` to return a special iterator object
        that implements a `__next__()` method to carry out the actual iteration.
        """
        return iter(self._children)


if __name__ == "__main__":
    root = Node(0)
    root.add_child(Node(1))
    root.add_child(Node(2))
    for n in root:
        print(n)
