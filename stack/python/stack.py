from typing import Self
from collections.abc import Sequence

from state_error import EmptyStackError


class Stack[E]:
    _internal_list: list[E]

    def __init__(self) -> None:
        super().__init__()
        self._internal_list = []

    @classmethod
    def from_sequence(cls, sequence: Sequence[E]) -> Self:
        stack: Stack[E] = cls()

        for item in sequence:
            stack.push(item)

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
