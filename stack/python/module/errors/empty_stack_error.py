class EmptyStackError(Exception):
    message: str

    def __init__(self, message="Tried to pop in an empty Stack") -> None:
        self.message = message

        super().__init__(self.message)
