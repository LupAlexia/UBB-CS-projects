class Grade:
    def __init__(self, assignment, student, value):
        self.__assignment = assignment
        self.__student = student
        self.__value = value

    @property
    def assignment(self):
        return self.__assignment

    @assignment.setter
    def assignment(self, assignment):
        self.__assignment = assignment

    @property
    def student(self):
        return self.__student

    @student.setter
    def student(self, student):
        self.__student = student

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    def __str__(self):
        return "Assignment id: " + str(self.__assignment) + " Student id: " + str(self.__student) + " Grade value: " + str(self.__value)
    def __eq__(self, g):
        return isinstance(g, Grade) and self.__student == g.student and self.assignment == g.assignment