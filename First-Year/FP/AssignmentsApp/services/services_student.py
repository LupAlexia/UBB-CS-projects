from src.domain.student import Student
from src.exceptions.obj_not_found import ObjectNotFoundException
from src.repository.repo_text_student import TextFileRepoStudent
from src.repository.repo_binary_student import BinaryFileRepoStudent
from src.repository.repo_mem_student import InMemoryRepoStudent
from src.exceptions.incorrect_input import IncorrectInputException
from src.exceptions.duplicate_objects import DuplicateObjectException
from src.services.sevices_undo import FunctionCall, Operation, CascadedOperation


class ServicesStudent:
    def __init__(self, student_repository, undo_service, grade_service):
        """
        Constructor for the services
        :param repository:
        """
        self._repo = student_repository
        self._undo_service = undo_service
        self._grade_service = grade_service

    def add_student(self, id, name, group):
        """
        Adds a student to the repository
        :param id: student id
        :param name: student name
        :param group: student group
        :return: none - the function modifies the current students list
        :exception: DuplicateObjectException - if a student with that index was already added
        """
        s = Student(id, name, group)
        try:
            self._repo.add_student(s)

            fc_undo = FunctionCall(self._repo.remove_student, s)
            fc_redo = FunctionCall(self._repo.add_student, s)
            op = Operation(fc_undo, fc_redo)
            self._undo_service.record_operation(op)

        except DuplicateObjectException as e:
            raise # re-throw the exception into class ui

    def remove_student(self, id):
        '''
        Removes the student with the given id from the list of students
        :param id: the student's id
        :return: none - the function modifies the current students list
        :exception: ObjectNotFoundException - if a student with that index doesn't exist
        '''
        try:
            student = self._repo.find_student_by_id(id)
            if student is None:
                raise ObjectNotFoundException('student', id)

            self._repo.remove_student(student)
            fc_undo = FunctionCall(self._repo.add_student, student)
            fc_redo = FunctionCall(self._repo.remove_student, student)
            operations = [Operation(fc_undo, fc_redo)]

            # Remove all grades for this assignment
            grades_repository = self._grade_service.getRepo()
            grades = self._grade_service.remove_by_student_id(id)
            for grade in grades:
                fc_undo = FunctionCall(grades_repository.add_grade, grade)
                fc_redo = FunctionCall(grades_repository.remove_grade, grade)
                operations.append(Operation(fc_undo, fc_redo))

            self._undo_service.record_operation(CascadedOperation(*operations))
        except ObjectNotFoundException as e:
            raise

    def update_student(self, id, name, group):
        '''
        Updates the given student from the list of students
        :param id: the student's id
        param name: new student name
        :param group: new student group
        :return: none - the function modifies the current students list
        :exception: ObjectNotFoundException - if a student with that index doesn't exist
        '''
        old_student = self._repo.find_student_by_id(id)
        new_student = Student(id, name, group)
        try:
            self._repo.update_student(new_student)

            fc_undo = FunctionCall(self._repo.update_student, old_student)
            fc_redo = FunctionCall(self._repo.update_student, new_student)
            op = Operation(fc_undo, fc_redo)
            self._undo_service.record_operation(op)
        except ObjectNotFoundException:
            raise

    def check_student_exists(self, id):
        try:
            student = self._repo.find_student_by_id(id)
            if student is None:
                raise ObjectNotFoundException('student', id)

            return True
        except ObjectNotFoundException as e:
            raise

    def find_student_by_id(self, id):
        student = self._repo.find_student_by_id(id)
        if student is None:
            return None
        return student

    def find_students_ids_by_group(self, group):
        students_ids = self._repo.find_students_ids_by_group(group)
        if students_ids is None:
            return None
        return students_ids


    def print_list(self):
        return self._repo.get_all()


