from src.domain.assignment import Assignment
from src.exceptions.duplicate_objects import DuplicateObjectException
from src.exceptions.obj_not_found import ObjectNotFoundException
from src.services.sevices_undo import FunctionCall, Operation, CascadedOperation


class ServicesAssignment:
    def __init__(self, assignment_repository, undo_service, grade_service):
        """
        Constructor for the services
        :param repository:
        """
        self._repo = assignment_repository
        self._undo_service = undo_service
        self._grade_service = grade_service

    def add_assignment(self, id, descript, deadline):
        """
        Adds an assignment to the repository
        :param id: assignment id
        :param descript: assignment description
        :param deadline: assignment deadline
        :return:none - the function modifies the current assignments list
        :exception: DuplicateObjectException - if an assignment with that index was already added
        """
        a = Assignment(id, descript, deadline)
        try:
            self._repo.add_assignment(a)

            fc_undo = FunctionCall(self._repo.remove_assignment, a)
            fc_redo = FunctionCall(self._repo.add_assignment, a)
            op = Operation(fc_undo, fc_redo)
            self._undo_service.record_operation(op)
        except DuplicateObjectException as e:
            raise# re-throw the exception into class ui

    def remove_assignment(self, id):
        '''
        Removes the assignment with the given id from the repository
        :param id: the assignment's id
        :return: none - the function modifies the current assignments list
        :exception: ObjectNotFoundException - if an assignment with that index doesn't exist
        '''
        try:
            assignment = self._repo.find_assignment_by_id(id)
            if assignment is None:
                raise ObjectNotFoundException('assignment', id)

            self._repo.remove_assignment(assignment)
            fc_undo = FunctionCall(self._repo.add_assignment, assignment)
            fc_redo = FunctionCall(self._repo.remove_assignment,assignment)
            operations = [Operation(fc_undo, fc_redo)]

            #Remove all grades for this assignment
            grades_repository = self._grade_service.getRepo()
            grades = self._grade_service.remove_by_assignment_id(id)
            for grade in grades:
                fc_undo = FunctionCall(grades_repository.add_grade, grade)
                fc_redo = FunctionCall(grades_repository.remove_grade, grade)
                operations.append(Operation(fc_undo, fc_redo))

            self._undo_service.record_operation(CascadedOperation(*operations))
        except ObjectNotFoundException as e:
            raise

    def update_assignment(self, id, descript, deadline):
        """
        Adds an assignment from the repository
        :param id: assignment id
        :param descript: new assignment description
        :param deadline: new assignment deadline
        :return:none - the function modifies the current assignments list
        :exception: ObjectNotFoundException - if an assignment with that index doesn't exist
        """
        old_assignment = self._repo.find_assignment_by_id(id)
        new_assignment = Assignment(id,descript, deadline)
        try:
            self._repo.update_assignment(new_assignment)

            fc_undo = FunctionCall(self._repo.update_assignment, old_assignment)
            fc_redo = FunctionCall(self._repo.update_assignment, new_assignment)
            op = Operation(fc_undo, fc_redo)
            self._undo_service.record_operation(op)
        except ObjectNotFoundException:
            raise

    def check_assignment_exists(self, id):
        try:
            assignment = self._repo.find_assignment_by_id(id)
            if assignment is None:
                raise ObjectNotFoundException('assignment', id)

            return True
        except ObjectNotFoundException as e:
            raise

    def find_assignment_by_id(self, id):
        assignment = self._repo.find_assignment_by_id(id)
        return assignment

    def print_list(self):
        return self._repo.get_all()


    def undo(self):
        cnt = 0
        for _ in self._repo.get_history():
            cnt += 1
        if cnt > 1:
            self._repo.undo()
        else:
            raise ValueError("\nError: No more undos!\n")