class EmptyStackError(Exception):
    """The stack has no elements.

    Args:
        Exception (Exception): Base class for exceptions

    Attributes:
        message (str): A message to be presented when raised.
    """

    message: str

    def __init__(self, message="Tried to pop in an empty Stack") -> None:
        """Initializes the Exception class with an optional message

        Args:
            message (str, optional): Message about the operation that raises the Exception. Defaults to "Tried to pop in an empty Stack".
        """
        self.message = message

        super().__init__(self.message)
