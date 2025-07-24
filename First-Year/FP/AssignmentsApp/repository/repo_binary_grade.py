from src.domain.grade import Grade
from src.repository.repo_mem_grade import InMemoryRepoGrade
import os
import pickle
from src.repository.repo_mem_assignment import InMemoryRepoAssignment
from src.repository.repo_mem_student import InMemoryRepoStudent
import copy
import random

class BinaryFileRepoGrade(InMemoryRepoGrade):
    def __init__(self, bin_file):
        super().__init__()
        self._bin_file = bin_file
        self._data = self.load_from_file(self._bin_file)

        if len(self._data) > 0:
            pass
        else:
            # 20 random generated entities at startup
            student_repo = InMemoryRepoStudent()
            assignment_repo = InMemoryRepoAssignment()
            for _ in range(20):
                grade = Grade(random.choice(assignment_repo.get_all_ids()), random.choice(student_repo.get_all_ids()),
                              random.randint(0, 10))
                self._data.append(grade)
            self.save_to_file(bin_file)

    def add_grade(self, grade: Grade):
        """
        Adds the given grade to the list of grades and updates the history list by calling the add function of parent class.
        Then saves the modifications to the binary file "binary.pkl"
        :param grade: the student to be added
        :return: none - the function modifies the current students list
        """
        super().add_grade(grade)
        self.save_to_file(self._bin_file)

    def remove_grade(self, grade:Grade):
        super().remove_grade(grade)
        self.save_to_file(self._bin_file)

    def update_grade(self, grade: Grade):
        super().update_grade(grade)
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
                    grade = pickle.load(file)
                    temp_data.append(grade)
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
        for grade in self._data:
            pickle.dump(grade, file)
        file.close()

