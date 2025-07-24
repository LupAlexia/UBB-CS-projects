class IncorrectInputException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self._message = message

    def __str__(self):
        return f'Your input is not correct: {self._message}'