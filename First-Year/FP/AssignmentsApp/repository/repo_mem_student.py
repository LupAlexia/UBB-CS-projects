from src.domain.student import Student
from src.exceptions.duplicate_objects import DuplicateObjectException
from src.exceptions.obj_not_found import ObjectNotFoundException
from faker import Faker
import copy
import random

class InMemoryRepoStudent:
    def __init__(self):
        self._data = []

        # 20 random generated entities at startup
        fake = Faker()
        for i in range(20):
            student = Student(i, fake.name(), random.randint(1, 10))
            self._data.append(student)

    def add_student(self, student:Student):
        """
        Adds the given student to the list of students
        :param student: the student to be added
        :return: none - the function modifies the current students list
        :exception: DuplicateObjectException - if a student with that index was already added
        """
        if self.find_student(student) is not None:
            raise DuplicateObjectException('student', 'Duplicate id', student.id)

        self._data.append(student)

    def find_student(self, student:Student):
        '''
        Finds the given student in the list of students
        :param student: the student to be looked for
        :return: the student's index
        '''
        index = None
        try:
            index = self._data.index(student) # the index method returns the index of a student from the list equal with the one provided as parameter(equal <=> same id)
        except ValueError: #index() method returns ValueError if nothing was found
            return None
        return index

    def find_student_by_id(self, id):
        '''
        Finds the student in the list of students, having the given id
        :param id: the id to be looked for
        :return: the student with that id
        '''
        objects = [obj for obj in self._data if obj.id == id]
        if len(objects) != 0:
            return objects[0]
        return None

    def find_students_ids_by_group(self, group):
        '''
        Finds the students in the list of students, having the given group
        :param group: the group to be looked for
        :return: the students part of that group
        '''
        objects_ids = [obj.id for obj in self._data if obj.group == group]
        if len(objects_ids) != 0:
            return objects_ids
        return None


    def remove_student(self, student):
        '''
        Removes the given student from the list of students
        :param student: the student to be removed
        :return: none - the function modifies the current students list
        :exception: ObjectNotFoundException - if a student with that index doesn't exist
        '''
        if self.find_student(student) is None:
            raise ObjectNotFoundException('student', student.id)
        self._data.remove(student)

    def update_student(self, student):
        '''
        Updates the given student from the list of students
        :param student: the student to be updated
        :return: none - the function modifies the current students list
        :exception: ObjectNotFoundException - if a student with that index doesn't exist
        '''
        index = self.find_student(student)
        if index is None:
            raise ObjectNotFoundException('student', student.id)
        else:
            self._data[index] = student

    def get_all(self):
        '''
        Provides the list of students
        :return: the current list of students
        '''
        return self._data

    def get_all_ids(self):
        return [student.id for student in self._data]