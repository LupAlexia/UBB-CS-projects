class Student:
    def __init__(self, id, name, group):
        self.__id = id
        self.__name = name
        self.__group = group

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def group(self):
        return self.__group
    @group.setter
    def group(self, group):
        self.__group = group

    def __str__(self):
        return "Student_id: " + str(self.__id) + " Name: " + str(self.__name) + " Group: " +str(self.__group)
    def __eq__(self, s): # Two students are considered equal if their ids are equal
        return isinstance(s, Student) and self.id == s.id