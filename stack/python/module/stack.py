"""A Stack implementation.

Raises:
    EmptyStackError: When tried to pop or peek when the stack is empty.
    StopIteration: StopIteration: To stop the iteration process.

Returns:
    Stack: A class that represents this data-structure.
"""

from typing import Collection, Generic, Iterator, Self, TypeVar, override
from collections.abc import Sequence

from module.errors.empty_stack_error import EmptyStackError

E = TypeVar("E")


class Stack(Collection, Generic[E]):
    """Linear data-structure that follows LIFO policy.

    Args:
        Collection : Base class that describes actual class as a Collection.
        Generic (E): For compatibility reasons, base class that describes the content of this class should have the same type.

    Raises:
        EmptyStackError: When `peek` and `pop` operations are made when the stack is empty.
        StopIteration: To stop the iteration process.

    Returns:
        Stack[E]: An instance of Stack.
    """

    _internal_list: list[E]
    _iterator_index: int = -1

    def __init__(self) -> None:
        """Initializes the instance of an empty stack."""
        super().__init__()
        self._internal_list = []

    @classmethod
    def from_sequence(cls, sequence: Sequence[E]) -> Self:
        """Factory constructor to initialize an instance of stack from a [sequence].

        Args:
            sequence (Sequence[E]): A sequence, like list, tuple, etc. It'll be iterated over from start to the end.

        Returns:
            Self: An instance of Stack filled with the [sequence] elements.
        """
        stack = cls()

        for item in sequence:
            stack.push(item)

        return stack

    def push(self, element: E) -> None:
        """Adds [element] to top of the stack.

        Args:
            element (E): Element to be added.
        """
        self._internal_list.append(element)

    def pop(self) -> E:
        """Removes the element at the top of the stack (the last added one).

        Raises:
            EmptyStackError: When the stack has no elements, this exception will be raised.

        Returns:
            E: The last element added in the stack.
        """
        if len(self._internal_list) > 0:
            return self._internal_list.pop()
        else:
            raise EmptyStackError()

    def try_pop(self) -> E | None:
        """Removes the element at the top of the stack (the last added one). Alternative that returns `None` instead to raise `EmptyStackError`.

        Returns:
            E | None: Last element added in the stack, `None` if the stack is empty.
        """
        try:
            return self.pop()
        except EmptyStackError:
            return None

    def clear(self) -> None:
        """Clear the stack of all of its elements."""
        self._internal_list.clear()

    def peek(self) -> E:
        """The element at the 'top' of the stack.

        Raises:
            EmptyStackError: When the stack is empty.

        Returns:
            E: The element at the 'top' of the stack, without remove it.
        """
        if len(self._internal_list) > 0:
            return self._internal_list[-1]
        else:
            raise EmptyStackError()

    def try_peek(self) -> E | None:
        """The element at top of the stack. Alternative that not raises to `peek`.

        Returns:
            E | None: The element at the top of the stack, `None` if the stack is empty.
        """
        try:
            return self.peek()
        except EmptyStackError:
            return None

    @property
    def is_empty(self) -> bool:
        """Check if the stack is empty.

        Returns:
            bool: `True` if the stack is empty, `False` otherwise.
        """
        return len(self._internal_list) == 0

    @override
    def __len__(self) -> int:
        """Number of items in the stack.

        Returns:
            int: Number of items in the stack.
        """
        return len(self._internal_list)

    @override
    def __contains__(self, element: object) -> bool:
        """Checks if the [element] is in the Stack.

        Args:
            element (object): Element to be searched.

        Returns:
            bool: `True` if the element is in the stack, `False` otherwise.
        """
        return element in self._internal_list

    @override
    def __iter__(self) -> Iterator[E]:
        """Iterator of the stack in LIFO order.

        Yields:
            Iterator[E]: An iterator of the actual stack in LIFO order.
        """
        return self

    def __next__(self) -> E:
        """The next element of the stack in LIFO order for the iterator.

        Raises:
            StopIteration: To stop the iteration process.

        Returns:
            E: Next element of the stack.
        """
        if self._iterator_index >= -len(self._internal_list):
            item = self._internal_list[self._iterator_index]
            self._iterator_index -= 1

            return item
        else:
            self._iterator_index = -1
            raise StopIteration