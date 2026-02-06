"""A Sentence as a sequence of words"""

import re
import reprlib


class SentenceV1:
    def __init__(self, text: str):
        self._text = text
        self._words = re.compile(r"\w+").findall(text)

    def __getitem__(self, index):
        return self._words[index]

    def __len__(self):
        return len(self._words)

    def __repr__(self):
        return f"{self.__class__.__name__}({reprlib.repr(self._text)})"


class SentenceV2:
    def __init__(self, text: str):
        self._text = text

    def __repr__(self):
        return f"{self.__class__.__name__}({reprlib.repr(self._text)})"

    def __iter__(self):
        return SentenceV2Iterator(re.compile(r"\w+").findall(self._text))


class SentenceV2Iterator:
    def __init__(self, words):
        self._words = words
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._words):
            raise StopIteration()
        word = self._words[self._index]
        self._index += 1
        return word


class SentenceV3:
    def __init__(self, text):
        self._text = text
        self._words = re.compile(r"\w+").findall(text)

    def __repr__(self):
        return f"{self.__class__.__name__}({reprlib.repr(self._text)})"

    def __iter__(self):
        for word in self._words:
            yield word


def display(sentence):
    print("\n", "=" * 40, sentence.__class__.__name__, "=" * 40)
    print(sentence)
    for word in sentence:
        print(word, end=", ")
    print()
    print(list(sentence))


if __name__ == "__main__":
    s1 = SentenceV1('"The time has come," the Walrus said,')
    display(s1)
    s2 = SentenceV2('"The time has come," the Walrus said,')
    display(s2)
    s3 = SentenceV3('"The time has come," the Walrus said,')
    display(s3)
