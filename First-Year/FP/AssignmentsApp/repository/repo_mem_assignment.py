from datetime import datetime

from src.domain.assignment import Assignment
from src.exceptions.duplicate_objects import DuplicateObjectException
from src.exceptions.obj_not_found import ObjectNotFoundException
from faker import Faker
import copy
import random

class InMemoryRepoAssignment:
    def __init__(self):
        self._data = []

        # 20 random generated entities at startup
        fake = Faker()
        descriptions = [
            "Write an essay on global warming.",
            "Solve the attached set of algebra problems.",
            "Prepare a presentation on a historical event.",
            "Complete the biology lab report.",
            "Read and summarize Chapter 5 of the textbook.",
            "Write a poem about nature.",
            "Research and create a report on renewable energy."]
        start_date = datetime(2024, 1, 1)
        end_date = datetime(2024, 12, 31)
        for i in range(20):
            assignment = Assignment(i, random.choice(descriptions), fake.date_time_between(start_date=start_date, end_date=end_date).strftime("%Y-%m-%d"))
            self._data.append(assignment)

    def add_assignment(self, assignment:Assignment):
        """
        Adds the given assignment to the list of assignments
        :param assignment: the assignment to be added
        :return: none - the function modifies the current assignments list
        """
        if self.find_assignment(assignment) is not None:
            raise DuplicateObjectException('assignment', 'Duplicate id', assignment.id)

        self._data.append(assignment)

    def find_assignment(self, assignment:Assignment):
        '''
        Finds the given assignment in the list of assignments
        :param assignment: the assignment to be looked for
        :return: the assignment's index
        '''
        index = None
        try:
            index = self._data.index(assignment) # the index method returns the index of an assignment from the list equal with the one provided as parameter(equal <=> same id)
        except ValueError:
            return None
        return index

    def find_assignment_by_id(self, id):
        '''
        Finds the assignment in the list of assignments, having the given id
        :param id: the id to be looked for
        :return: the assignment with that id
        '''
        objects = [obj for obj in self._data if obj.id == id]
        if len(objects) != 0:
            return objects[0]
        return None

    def remove_assignment(self, assignment:Assignment):
        """
        Removes the given assignment from the list of assignments
        :param assignment: the assignment to be removed
        :return: none - the function modifies the current assignments list
        """
        if self.find_assignment(assignment) is None:
            raise ObjectNotFoundException('assignment', assignment.id)
        self._data.remove(assignment)

    def update_assignment(self, assignment:Assignment):
        """
        Updates the given assignment of the list of assignments
        :param assignment: the assignment to be updated
        :return: none - the function modifies the current assignments list
        """
        index = self.find_assignment(assignment)
        if index is None:
            raise ObjectNotFoundException('assignment', assignment.id)
        else:
            self._data[index] = assignment

    def get_all(self):
        return self._data

    def get_all_ids(self):
        return [assignment.id for assignment in self._data]