"""Defining Generator Functions with Extra State

Problem:
    You would like to define a generator function,
    but it involves extra state that you would like to expose to the user somehow.

Solution:
    yield
"""

from collections import deque


class LineHistory:
    def __init__(self, lines, max_history_lines: int = 3):
        self.lines = lines
        self.history = deque(maxlen=max_history_lines)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


if __name__ == "__main__":
    with open("fluent_python/iter_gene/lines.txt") as fp:
        line_history = LineHistory(fp)
        for line in line_history:
            if "Rust" in line:
                for hlineno, hline in line_history.history:
                    print(f"{hlineno}. {hline}")
