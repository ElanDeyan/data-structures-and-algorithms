class FullQueueException(Exception):

    message: str

    def __init__(self, message: str = "The queue is full of capacity. Dequeue or increase its capacity.") -> None:
        self.message = message
        super().__init__(message)