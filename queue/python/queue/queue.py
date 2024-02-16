"""
    Queue implementation in python lang
"""

from collections import deque
from collections.abc import Collection, Iterator
from typing import Generic, Optional, Self, Sequence, TypeVar, override

from python.queue.full_queue_exception import FullQueueException
from python.queue.empty_queue_exception import EmptyQueueException

E = TypeVar("E")


class Queue(Collection, Generic[E]):
    """
    A data-structure that follows FIFO (First-in, First-out) rule.
    Internally, uses deque for better performance in enqueue and dequeue methods.
    """

    _internal_deque: deque[E]
    _max_capacity: Optional[int]
    _iterator_index: int = 0

    def __init__(self, *, max_capacity: Optional[int] = None) -> None:
        self._internal_deque = deque(maxlen=max_capacity)
        self._max_capacity = max_capacity

    @classmethod
    def from_sequence(
        cls, sequence: Sequence[E], *, max_capacity: Optional[int] = None
    ) -> Self:
        if max_capacity is not None and len(sequence) > max_capacity:
            raise ValueError(
                "Your sequence's length must be less or equal your max capacity"
            )

        queue = cls(max_capacity=max_capacity)

        for item in sequence:
            queue.enqueue(item)

        return queue

    @property
    def max_capacity(self) -> Optional[int]:
        return self._max_capacity

    @max_capacity.setter
    def max_capacity(self, new_capacity: Optional[int]):
        if new_capacity is not None:
            if new_capacity < len(self):
                raise ValueError(
                    f"Your new capacity shouldn't be less than the len of the queue, {len(self)}"
                )
            else:
                self._max_capacity = new_capacity
        elif self.max_capacity is not None:
            self._max_capacity = None

    def enqueue(self, element: E) -> None:
        if self.max_capacity is not None and len(self) > self.max_capacity:
            raise FullQueueException()
        self._internal_deque.append(element)

    def dequeue(self) -> E:
        if self.is_not_empty:
            return self._internal_deque.popleft()
        else:
            raise EmptyQueueException()

    def try_dequeue(self) -> Optional[E]:
        try:
            return self._internal_deque.popleft()
        except EmptyQueueException:
            return None

    @property
    def peek(self) -> E:
        if self.is_not_empty:
            return self._internal_deque[0]
        else:
            raise EmptyQueueException()

    def try_peek(self) -> Optional[E]:
        try:
            return self.peek
        except EmptyQueueException:
            return None

    @property
    def is_full(self) -> bool:
        '''Checks if the queue is full of capacity
        ::
        '''
        return self.max_capacity is not None and len(self) == self.max_capacity

    @property
    def is_not_full(self) -> bool:
        """Checks if the queue is not full, assuming if there's a max_capacity.

        :returns: `True` if the number of elements in queue is less than `self.max_capacitiy`, `False` otherwise
        :rtype: bool
        """
        return not self.is_full

    @property
    def is_empty(self) -> bool:
        """Checks if the queue is empty

        :returns: `True` if the queue has not elements, `False` otherwise
        :rtype: bool
        """
        return len(self) == 0

    @property
    def is_not_empty(self) -> bool:
        """Checks if the queue is not empty

        :returns: `True` if has elements, otherwise `False`
        :rtype: bool
        """
        return not self.is_empty

    def clear(self) -> None:
        """Clears queue elements"""
        self._internal_deque.clear()

    @override
    def __len__(self) -> int:
        return len(self._internal_deque)

    @override
    def __contains__(self, item: E) -> bool:
        return item in self._internal_deque

    @override
    def __iter__(self) -> Iterator[E]:
        return self

    @override
    def __next__(self) -> E:
        if self._iterator_index < len(self):
            item = self._internal_deque[self._iterator_index]
            self._iterator_index += 1

            return item
        else:
            self._iterator_index = 0
            raise StopIteration
