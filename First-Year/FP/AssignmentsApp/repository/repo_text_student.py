from src.repository.repo_mem_student import InMemoryRepoStudent
from src.domain.student import Student
from faker import Faker
import copy
import random
import os

class TextFileRepoStudent(InMemoryRepoStudent):
    def __init__(self, text_file):
        super().__init__()
        self._text_file = text_file
        self._data = self.load_from_file(self._text_file)

        if len(self._data) > 0:
            pass
        else:
            # 20 random generated entities at startup
            fake = Faker()
            for i in range(20):
                student = Student(i, fake.name(), random.randint(1, 10))
                self._data.append(student)
            self.save_to_file(self._text_file)

    def add_student(self, student: Student):
        """
        Adds the given student to the list of students by calling the add function of parent class.
        Then saves the modifications to the text file
        :param student: the student to be added
        :return: none - the function modifies the current students list
        """
        super().add_student(student)
        self.save_to_file(self._text_file)

    def remove_student(self, student: Student):
        """
        Removes the given student from the list of students by calling the remove function of parent class.
        Then saves the modifications to the text file
        :param student: the student to be removed
        :return: none - the function modifies the current students list
        """
        super().remove_student(student)
        self.save_to_file(self._text_file)

    def update_student(self, student: Student):
        """
        Updates the given student from the list of students by calling the update function of parent class.
        Then saves the modifications to the text file
        :param student: the student to be modified
        :return: none - the function modifies the current students list
        """
        super().update_student(student)
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
                    temp_data.append(Student(int(line[0]), line[1], int(line[2])))
                file.close()
            #self._data = temp_data.copy()
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
            for student in self._data:
                file.write(str(student.id) + "," + str(student.name)
                           + "," + str(student.group) + "\n")
            file.close()
        except IOError as e:
            print("Error: " + str(e))
