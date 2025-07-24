from src.domain.grade import Grade
from src.domain.assignment import Assignment
from faker import Faker
import copy
import random

from src.exceptions.duplicate_objects import DuplicateObjectException
from src.exceptions.obj_not_found import ObjectNotFoundException
from src.repository.repo_mem_assignment import InMemoryRepoAssignment
from src.repository.repo_mem_student import InMemoryRepoStudent


class InMemoryRepoGrade:
    def __init__(self):
        self._data = []

        #20 random generated entities at startup
        student_repo = InMemoryRepoStudent()
        assignment_repo = InMemoryRepoAssignment()
        for i in range(20):
            assignment_id = random.choice(assignment_repo.get_all_ids())
            student_id = random.choice(student_repo.get_all_ids())
            grade = Grade(assignment_id, student_id, random.randint(0, 10))

            # We can t have two assignments with the same student and assignment id s
            if self.find_grades_with_student_id(student_id) and self.find_grades_with_assignment_id(assignment_id):
                i = i - 1
            else:
                self._data.append(grade)

    def add_grade(self, grade:Grade):
        """
        Adds the given grade to the list of grades
        :param grade: the grade to be added
        :return: none - the function modifies the current grades list
        """
        if self.find_grade(grade) is not None:
            raise DuplicateObjectException('this assignment to student', 'Duplicate assignment to student', grade.student)

        self._data.append(grade)

    def update_grade(self, grade:Grade):
        index = self.find_grade(grade)
        if index is None:
            raise ObjectNotFoundException('grade', grade.student)
        else:
            self._data[index] = grade

    def find_grade(self, grade:Grade):
        index = None
        try:
            index = self._data.index(grade) # the index method returns the index of a grade from the list equal with the one provided as parameter(equal <=> same ids)
        except ValueError:
            return None
        return index

    def find_grades_with_student_id(self, student_id):
        objects = [obj for obj in self._data if obj.student == student_id]
        if len(objects) != 0:
            return objects
        return None

    def find_grades_with_assignment_id(self, assignment_id):
        objects = [obj for obj in self._data if obj.assignment == assignment_id]
        if len(objects) != 0:
            return objects
        return None

    def find_grade_with_assignment_student_id(self, assignment_id, student_id):
        objects = [obj for obj in self._data if (obj.assignment == assignment_id and obj.student == student_id)]
        if len(objects) != 0:
            return objects[0]
        return None

    def remove_grade(self, grade:Grade):
        self._data.remove(grade)

    def filter_by_ungraded(self, student_id):
        return [grade.assignment for grade in self._data if grade.student == student_id and grade.value == 0]

    def get_all(self):
        return self._data
