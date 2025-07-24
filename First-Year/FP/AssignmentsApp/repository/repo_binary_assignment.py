from datetime import datetime

from src.repository.repo_mem_assignment import InMemoryRepoAssignment
from src.domain.assignment import Assignment
from faker import Faker
import copy
import random
import pickle
import os

class BinaryFileRepoAssignment(InMemoryRepoAssignment):
    def __init__(self, bin_file):
        super().__init__()
        self._bin_file = bin_file
        self._data = self.load_from_file(self._bin_file)

        if len(self._data) > 0:
            pass
        else:
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
                assignment = Assignment(i, random.choice(descriptions),fake.date_time_between(start_date=start_date, end_date=end_date).strftime("%Y-%m-%d"))
                self._data.append(assignment)
            self.save_to_file(bin_file)

    def add_assignment(self, assignment: Assignment):
        """
        Adds the given assignment to the list of assignments by calling the add function of parent class.
        Then saves the modifications to the binary file
        :param assignment: the assignment to be added
        :return: none - the function modifies the current assignments list
        """
        super().add_assignment(assignment)
        self.save_to_file("assignments.pkl")

    def remove_assignment(self, assignment:Assignment):
        """
        Removes the given assignment from the list of assignments by calling the remove function of parent class.
        Then saves the modifications to the binary file
        :param assignment: the assignment to be added
        :return: none - the function modifies the current assignments list
        """
        super().remove_assignment(assignment)
        self.save_to_file("assignments.pkl")

    def update_assignment(self, assignment:Assignment):
        """
        Updates the given assignment from the list of assignments by calling the update function of parent class.
        Then saves the modifications to the binary file
        :param assignment: the assignment to be added
        :return: none - the function modifies the current assignments list
        """
        super().update_assignment(assignment)
        self.save_to_file("assignments.pkl")


    @staticmethod
    def load_from_file(pkl_file):
        """
        Loads the list from a binary file
        :param pkl_file:
        :return:
        """
        if not os.path.exists(pkl_file):
            return []  # Return an empty list if the file doesn't exist

        with open(pkl_file, "rb") as file:
            temp_data = []
            while True:
                try:
                    assignment = pickle.load(file)
                    temp_data.append(assignment)
                except EOFError:
                    break
        file.close()
        return temp_data

    def save_to_file(self, pkl_file):
        """
        Saves the list to a binary file
        :param pkl_file:
        :return:
        """
        file = open(pkl_file, "wb")
        for assignment in self._data:
            pickle.dump(assignment, file)
        file.close()
