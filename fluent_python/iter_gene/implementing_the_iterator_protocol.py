"""Implementing the Iterator Protocol

Problem:
    You are building custom objects on which you would like to support iteration,
    but would like an easy way to implement the iterator protocol.

Solution:
    yield
    yield from
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
        return iter(self._children)

    def depth_first(self):
        yield self
        if self._children:
            for c in self:
                yield from c.depth_first()


class Node2:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return f"{self.__class__.__name__}(value={self._value!r}, children={self._children!r})"

    def add_child(self, child: Node):
        self._children.append(child)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        return DepthFirstIterator(self)


class DepthFirstIterator:
    def __init__(self, node: Node2):
        self.node = node
        self.children_iter = None
        self.child_iter = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.children_iter is None:
            self.children_iter = iter(self.node)
            return self.node
        elif self.child_iter:
            try:
                next_child = next(self.child_iter)
                return next_child
            except StopIteration:
                self.child_iter = None
                return next(self)
        else:
            self.child_iter = next(self.children_iter).depth_first()
            return next(self)


if __name__ == "__main__":
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))
    root.add_child(child1)
    root.add_child(child2)

    for n in root.depth_first():
        print(n)

    root = Node2(0)
    child1 = Node2(1)
    child2 = Node2(2)
    child1.add_child(Node2(3))
    child1.add_child(Node2(4))
    child2.add_child(Node2(5))
    root.add_child(child1)
    root.add_child(child2)

    for n in root.depth_first():
        print(n)
