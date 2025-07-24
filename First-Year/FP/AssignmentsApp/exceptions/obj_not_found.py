class ObjectNotFoundException(Exception):
    def __init__(self, obj, id):
        super().__init__(obj)
        self._obj = obj
        self._id = id

    def __str__(self):
        return f' The {self._obj} with id {self._id} was not found!'
