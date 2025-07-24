class Assignment:
    def __init__(self, id, descript, deadline):
        self.__id = id
        self.__descript = descript
        self.__deadline = deadline

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def descript(self):
        return self.__descript

    @descript.setter
    def descript(self, descript):
        self.__descript = descript

    @property
    def deadline(self):
        return self.__deadline

    @deadline.setter
    def deadline(self, deadline):
        self.__deadline = deadline

    def __str__(self):
        return "Assignment_id: " + str(self.__id) + " Description: " + str(self.__descript) + " Deadline: " + str(self.__deadline)
    def __eq__(self, a): # Two assignments are considered equal if their ids are equal
        return isinstance(a, Assignment) and self.__id == a.id