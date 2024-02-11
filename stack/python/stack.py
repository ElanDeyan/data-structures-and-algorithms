from typing import Collection, Generic, Iterator, Self, TypeVar, override
from collections.abc import Sequence

from state_error import EmptyStackError

E = TypeVar("E")


class Stack(Collection, Generic[E]):
    _internal_list: list[E]
    _iterator_index: int = -1

    def __init__(self) -> None:
        super().__init__()
        self._internal_list = []

    @classmethod
    def from_sequence(cls, sequence: Sequence[E]) -> Self:
        stack = cls()

        for item in sequence:
            stack.push(item)

        return stack

    def push(self, element: E) -> None:
        self._internal_list.append(element)

    def pop(self) -> E:
        if len(self._internal_list) > 0:
            return self._internal_list.pop()
        else:
            raise EmptyStackError()

    def try_pop(self) -> E | None:
        try:
            return self.pop()
        except EmptyStackError:
            return None

    def clear(self) -> None:
        self._internal_list.clear()

    @property
    def peek(self) -> E:
        if len(self._internal_list) > 0:
            return self._internal_list[-1]
        else:
            raise EmptyStackError()

    @property
    def try_peek(self) -> E | None:
        try:
            return self.peek
        except EmptyStackError:
            return None

    @property
    def is_empty(self) -> bool:
        return len(self._internal_list) == 0

    @override
    def __len__(self) -> int:
        return len(self._internal_list)

    @override
    def __contains__(self, element: object) -> bool:
        return element in self._internal_list

    @override
    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> E:
        if self._iterator_index >= -len(self._internal_list):
            item = self._internal_list[self._iterator_index]
            self._iterator_index -= 1

            return item
        else:
            self._iterator_index = -1
            raise StopIteration
