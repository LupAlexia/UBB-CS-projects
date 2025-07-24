from src.domain.grade import Grade
from src.domain.student import Student
from src.exceptions.duplicate_objects import DuplicateObjectException
from src.exceptions.obj_not_found import ObjectNotFoundException
from src.services.services_assignment import ServicesAssignment
from src.services.sevices_undo import FunctionCall, Operation


class StudentLateDTO:
    def __init__(self, student_id,  ungraded):
        self.__student_id = student_id
        self.__ungraded = ungraded

    @property
    def student_id(self):
        return self.__student_id

    @property
    def ungraded_assignments(self):
        return self.__ungraded

class StudentTopDTO: # data transfer object between service and ui
    def __init__(self, student_id, average_grade):
        self.__student_id = student_id
        self.__average_grade = average_grade

    @property
    def student_id(self):
        return self.__student_id

    @property
    def average_grade(self):
        return self.__average_grade

    def __lt__(self, other):
        return isinstance(other, StudentTopDTO) and self.__average_grade < other.__average_grade


class ServicesGrade:
    def __init__(self, grade_repository, undo_service):
        """
        Constructor for the services
        :param repository:
        """
        self._repo = grade_repository
        self._undo_service = undo_service

    def add_grade(self, assignment_id, student_id, grade):
        """
        Adds a grade to the repository
        """
        g = Grade(assignment_id, student_id, grade)
        try:
            self._repo.add_grade(g)

            fc_undo = FunctionCall(self._repo.remove_grade, g)
            fc_redo = FunctionCall(self._repo.add_grade, g)
            op = Operation(fc_undo, fc_redo)
            self._undo_service.record_operation(op)
        except DuplicateObjectException as e:
            raise  # re-throw the exception into class ui

    def update_grade(self, assignment_id, student_id, grade):
        old_grade = self._repo.find_grade_with_assignment_student_id(assignment_id, student_id)
        new_grade = Grade(assignment_id, student_id, grade)
        try:
            self._repo.update_grade(new_grade)

            fc_undo = FunctionCall(self._repo.update_grade, old_grade)
            fc_redo = FunctionCall(self._repo.update_grade, new_grade)
            op = Operation(fc_undo, fc_redo)
            self._undo_service.record_operation(op)
        except ObjectNotFoundException:
            raise
    def remove_by_student_id(self, student_id):
        grades = self._repo.find_grades_with_student_id(student_id)
        if grades is not None:
            for grade in grades:
                self._repo.remove_grade(grade)
        return grades

    def remove_by_assignment_id(self, assignment_id):
        grades = self._repo.find_grades_with_assignment_id(assignment_id)
        if grades is not None:
            for grade in grades:
                self._repo.remove_grade(grade)
        return grades

    def filter_by_assignment(self, assignment_id): # students that received an assignment, sorted desc by grade
        grades = self._repo.find_grades_with_assignment_id(assignment_id)
        grades.sort(key = lambda grade: grade.value, reverse = True)

        return grades

    def find_late_students(self):
        student_assign_ids = {} # dictionary to connect student id with the list of assignments late to be handed in

        for grade in self._repo.get_all():
            if grade.value == 0: # assignment late to be handed in if ungraded and deadline before current date
                if grade.student not in student_assign_ids:
                    student_assign_ids[grade.student] = {grade.assignment}
                else:
                    student_assign_ids[grade.student].add(grade.assignment)

        result = []
        for student_id in student_assign_ids:
            result.append(StudentLateDTO(student_id, student_assign_ids[student_id]))
        return result

    def sort_desc_by_average(self):
        student_sum = {} # a dictionary to connect student id with the sum of his grades
        nb_assign = [] # nb[i] number of graded assignments of student with id i
        grades = self._repo.get_all()
        for i in range(1000):
            nb_assign.append(0)

        for grade in grades:
            if grade.value > 0:
                if grade.student not in student_sum:
                    student_sum[grade.student] = grade.value
                else:
                    student_sum[grade.student] += grade.value
                nb_assign[grade.student] += 1

        result = []
        for student_id in student_sum:
            result.append(StudentTopDTO(student_id, round(student_sum[student_id] / nb_assign[student_id], 2)))
        result.sort(reverse=True)
        return result

    def getRepo(self):
        return self._repo

    def print_list(self):
        return self._repo.get_all()

    def print_list_by_ungraded(self, student_id):
        return self._repo.filter_by_ungraded(student_id)

