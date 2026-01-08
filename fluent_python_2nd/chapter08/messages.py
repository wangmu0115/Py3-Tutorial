from typing import Optional

from _builtins.pprint import console_print


def show_count(count: int, singular: str, plural: Optional[str] = None):
    if count == 1:
        return f"1 {singular}"
    else:
        return f"{str(count) if count else 'no'} {plural if plural else singular + 's'}"


# python -m fluent_python_2nd.chapter08.messages
if __name__ == "__main__":
    console_print(show_count(0, "part"))
    console_print(show_count(1, "part"))
    console_print(show_count(2, "part"))
    console_print(show_count(1, "child"))
    console_print(show_count(2, "child"))
    console_print(show_count(2, "child", "children"))
