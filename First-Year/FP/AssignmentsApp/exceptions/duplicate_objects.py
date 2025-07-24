class DuplicateObjectException(Exception):
    def __init__(self, obj, message, id):
        super().__init__(message)
        self._id = id
        self._message = message
        self._obj = obj

    def __str__(self):
        return f'{self._message}: {self._obj} with id {self._id} already exists!'