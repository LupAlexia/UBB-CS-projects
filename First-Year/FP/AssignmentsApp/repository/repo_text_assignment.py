from datetime import datetime

from src.repository.repo_mem_assignment import InMemoryRepoAssignment
from src.domain.assignment import Assignment
from faker import Faker
import copy
import random
import pickle
import os

class TextFileRepoAssignment(InMemoryRepoAssignment):
    def __init__(self, text_file):
        super().__init__()
        self._text_file = text_file
        self._data = self.load_from_file(self._text_file)

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
            self.save_to_file(self._text_file)

    def add_assignment(self, assignment: Assignment):
        """
        Adds the given assignment to the list of assignments by calling the add function of parent class.
        Then saves the modifications to the text file
        :param assignment: the assignment to be added
        :return: none - the function modifies the current assignments list
        """
        super().add_assignment(assignment)
        self.save_to_file(self._text_file)

    def remove_assignment(self, assignment:Assignment):
        """
        Removes the given assignment to the list of assignments by calling the remove function of parent class.
        Then saves the modifications to the text file
        :param assignment: the assignment to be removed
        :return: none - the function modifies the current assignments list
        """
        super().remove_assignment(assignment)
        self.save_to_file(self._text_file)

    def update_assignment(self, assignment:Assignment):
        """
        Updates the given assignment to the list of assignments by calling the update function of parent class.
        Then saves the modifications to the text file
        :param assignment: the assignment to be modified
        :return: none - the function modifies the current assignments list
        """
        super().update_assignment(assignment)
        self.save_to_file(self._text_file)


    @staticmethod
    def load_from_file(textfile):
        """
        Loads the list from a text file
        :param textfile:
        :return:
        """
        try:
            if not os.path.exists(textfile):
                return []  # Return an empty list if the file doesn't exist

            with open(textfile, "r") as file:
                temp_data = []
                for line in file:
                    line = line.strip()
                    line = line.split(",")
                    temp_data.append(Assignment(int(line[0]), line[1], line[2]))
                file.close()
            return temp_data
        except IOError:
            pass

    def save_to_file(self, textfile):
        """
        Saves the list to a text file
        :param textfile:
        :return:
        """
        try:
            file = open(textfile, "w")
            for assignment in self._data:
                file.write(str(assignment.id) + "," + str(assignment.descript)
                           + "," + str(assignment.deadline) + "\n")
            file.close()
        except IOError as e:
            print("Error: " + str(e))
