from src.repository.repo_mem_student import InMemoryRepoStudent
from src.domain.student import Student
from faker import Faker
import copy
import random
import pickle
import os

class BinaryFileRepoStudent(InMemoryRepoStudent):
    def __init__(self, bin_file):
        super().__init__()
        self._bin_file = bin_file
        self._data = self.load_from_file(self._bin_file)

        if len(self._data) > 0:
            pass
        else:
            # 20 random generated entities at startup
            fake = Faker()
            for i in range(20):
                student = Student(i, fake.name(), random.randint(1, 10))
                self._data.append(student)
            self.save_to_file(bin_file)

    def add_student(self, student: Student):
        """
        Adds the given student to the list of students by calling the add function of parent class.
        Then saves the modifications to the binary file
        :param student: the student to be added
        :return: none - the function modifies the current students list
        """
        super().add_student(student)
        self.save_to_file(self._bin_file)

    def remove_student(self, student:Student):
        """
        Removes the given student from the list of students by calling the remove function of parent class.
        Then saves the modifications to the binary file
        :param student: the student to be removed
        :return: none - the function modifies the current students list
        """
        super().remove_student(student)
        self.save_to_file(self._bin_file)

    def update_student(self, student:Student):
        """
        Updates the given student from the list of students by calling the update function of parent class.
        Then saves the modifications to the binary file
        :param student: the student to be modified
        :return: none - the function modifies the current students list
        """
        super().update_student(student)
        self.save_to_file(self._bin_file)

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
                    student = pickle.load(file)
                    temp_data.append(student)
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
        for student in self._data:
            pickle.dump(student, file)
        file.close()
