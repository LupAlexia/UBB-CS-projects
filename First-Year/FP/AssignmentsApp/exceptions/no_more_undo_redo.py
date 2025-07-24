class NoMoreUndoException(Exception):
    def __init__(self, message = 'No more undos!'):
        super().__init__(message)

class NoMoreRedoException(Exception):
    def __init__(self, message = 'No more redos!'):
        super().__init__(message)
        self._message = message
