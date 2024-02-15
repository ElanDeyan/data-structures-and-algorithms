"""
    Queue implementation in python lang
"""

from collections import deque
from typing import Generic, Optional, Self, Sequence, TypeVar

from queue.empty_queue_exception import EmptyQueueException

E = TypeVar("E")


class Queue(Generic[E]):
    _internal_deque: deque[E]
    _max_capacity: Optional[int]

    def __init__(self,*, max_capacity: Optional[int] = None) -> None:
        self._internal_deque = deque(maxlen=max_capacity)
        # self.max_capacity = max_capacity

    @classmethod
    def from_sequence(cls, sequence: Sequence[E], *, max_capacity: Optional[int] = None) -> Self:

        if max_capacity is not None and len(sequence) > max_capacity:
            raise ValueError("Your sequence's length must be less or equal your max capacity")

        queue = cls(max_capacity=max_capacity)

        for item in sequence:
            queue.enqueue(item)

        return queue
    
    @property
    def max_capacity(self) -> Optional[int]:
        return self._max_capacity
    
    # @max_capacity.setter
    # def max_capacity(self, new_capacity: Optional[int]) -> None:
        # TODO: Create private increase capacity and assertion methods


    def enqueue(self, element: E) -> None:
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
    def is_empty(self) -> bool:
        return len(self) == 0

    @property
    def is_not_empty(self) -> bool:
        return not self.is_empty
    
    def __len__(self) -> int:
        return len(self._internal_deque)
