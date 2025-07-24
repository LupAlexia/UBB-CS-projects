import random
from src.domain.grade import Grade
from src.repository.repo_mem_assignment import InMemoryRepoAssignment
from src.repository.repo_mem_grade import InMemoryRepoGrade
import os
import pickle
import copy
from src.repository.repo_mem_student import InMemoryRepoStudent


class TextFileRepoGrade(InMemoryRepoGrade):
    def __init__(self, text_file):
        super().__init__()
        self._text_file = text_file
        self._data = self.load_from_file(self._text_file)

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
            self.save_to_file(self._text_file)

    def add_grade(self, grade: Grade):
        """
        Adds the given grade to the list of grades and updates the history list by calling the add function of parent class.
        Then saves the modifications to the binary file "binary.pkl"
        :param grade: the student to be added
        :return: none - the function modifies the current students list
        """
        super().add_grade(grade)
        self.save_to_file(self._text_file)

    def remove_grade(self, grade:Grade):
        super().remove_grade(grade)
        self.save_to_file(self._text_file)

    def update_grade(self, grade: Grade):
        super().update_grade(grade)
        self.save_to_file(self._text_file)

    @staticmethod
    def load_from_file(textfile):
        """
        Loads the list from a binary file
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
                    temp_data.append(Grade(int(line[0]), int(line[1]), int(line[2])))
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
            for grade in self._data:
                file.write(str(grade.student) + "," + str(grade.assignment)
                           + "," + str(grade.value) + "\n")
            file.close()
        except IOError as e:
            print("Error: " + str(e))

