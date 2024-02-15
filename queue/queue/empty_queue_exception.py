class EmptyQueueException(Exception):
    def __init__(self, message: str = "Invalid operation for an empty Queue") -> None:
        self.message = message

        super().__init__(self.message)
