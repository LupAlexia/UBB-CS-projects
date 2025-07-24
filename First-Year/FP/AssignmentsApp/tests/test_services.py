import unittest

from src.domain.assignment import Assignment
from src.domain.student import Student
from src.repository.repo_binary_assignment import BinaryFileRepoAssignment
from src.repository.repo_binary_student import BinaryFileRepoStudent
from src.repository.repo_mem_assignment import InMemoryRepoAssignment
from src.repository.repo_mem_student import InMemoryRepoStudent
from src.repository.repo_text_assignment import TextFileRepoAssignment
from src.repository.repo_text_student import TextFileRepoStudent
from src.services.services_assignment import ServicesAssignment
from src.services.services_student import ServicesStudent


class TestStudentsService(unittest.TestCase):
    def setUp(self):
        self._reset_file('test_students.txt')
        self._reset_file('test_students.pickle')

        mr = InMemoryRepoStudent(); tr = TextFileRepoStudent('test_students.txt'); br = BinaryFileRepoStudent('test_students.pickle')
        self.memory_service = ServicesStudent(mr)
        self.text_service = ServicesStudent(tr)
        self.binary_service = ServicesStudent(br)

    @staticmethod
    def _reset_file(file_path):
        with open(file_path, 'w') as file:
            file.truncate(0)

    def test_add_student(self):
        lenm = len(self.memory_service.print_list())
        lenb = len(self.binary_service.print_list())
        lent = len(self.text_service.print_list())

        self.memory_service.add_student(24, 'Aurel Popa', 10)
        self.text_service.add_student(24, 'Aurel Popa', 10)
        self.binary_service.add_student(24, 'Aurel Popa', 10)

        self.assertEqual(len(self.memory_service.print_list()), lenm + 1)
        self.assertEqual(len(self.binary_service.print_list()), lenb + 1)
        self.assertEqual(len(self.text_service.print_list()), lent + 1)


    def test_remove_student(self):
        self.memory_service.add_student(24, 'Aurel Popa', 10)
        self.text_service.add_student(24, 'Aurel Popa', 10)
        self.binary_service.add_student(24, 'Aurel Popa', 10)

        lenm = len(self.memory_service.print_list())
        lenb = len(self.binary_service.print_list())
        lent = len(self.text_service.print_list())

        self.memory_service.remove_student(24)
        self.text_service.remove_student(24)
        self.binary_service.remove_student(24)

        self.assertEqual(len(self.memory_service.print_list()), lenm - 1)
        self.assertEqual(len(self.binary_service.print_list()), lenb - 1)
        self.assertEqual(len(self.text_service.print_list()), lent - 1)

    def test_update_student(self):
        self.memory_service.add_student(24, 'Aurel Popa', 10)
        self.text_service.add_student(24, 'Aurel Popa', 10)
        self.binary_service.add_student(24, 'Aurel Popa', 10)

        student = Student(24, 'Aura Popa', 10)
        self.memory_service.update_student(24, 'Aura Popa', 10)
        self.text_service.update_student(24, 'Aura Popa', 10)
        self.binary_service.update_student(24, 'Aura Popa', 10)

        self.assertEqual(self.memory_service.find_student_by_id(24).name, student.name)
        self.assertEqual(self.text_service.find_student_by_id(24).name, student.name)
        self.assertEqual(self.binary_service.find_student_by_id(24).name, student.name)

        self.assertEqual(self.memory_service.find_student_by_id(24).group, student.group)
        self.assertEqual(self.text_service.find_student_by_id(24).group, student.group)
        self.assertEqual(self.binary_service.find_student_by_id(24).group, student.group)

class TestAssignmentsService(unittest.TestCase):
    def setUp(self):
        self._reset_file('test_assignments.txt')
        self._reset_file('test_assignments.pickle')

        mr = InMemoryRepoAssignment(); tr = TextFileRepoAssignment('test_assignments.txt'); br = BinaryFileRepoAssignment('test_assignments.pickle')
        self.memory_service = ServicesAssignment(mr)
        self.text_service = ServicesAssignment(tr)
        self.binary_service = ServicesAssignment(br)

    @staticmethod
    def _reset_file(file_path):
        with open(file_path, 'w') as file:
            file.truncate(0)

    def test_add_assignment(self):
        lenm = len(self.memory_service.print_list())
        lenb = len(self.binary_service.print_list())
        lent = len(self.text_service.print_list())

        self.memory_service.add_assignment(24, 'Global warming', '2024-12-08')
        self.text_service.add_assignment(24, 'Global warming', '2024-12-08')
        self.binary_service.add_assignment(24, 'Global warming', '2024-12-08')

        self.assertEqual(len(self.memory_service.print_list()), lenm + 1)
        self.assertEqual(len(self.binary_service.print_list()), lenb + 1)
        self.assertEqual(len(self.text_service.print_list()), lent + 1)


    def test_remove_assignment(self):
        self.memory_service.add_assignment(24, 'Global warming', '2024-12-08')
        self.text_service.add_assignment(24, 'Global warming', '2024-12-08')
        self.binary_service.add_assignment(24, 'Global warming', '2024-12-08')

        lenm = len(self.memory_service.print_list())
        lenb = len(self.binary_service.print_list())
        lent = len(self.text_service.print_list())

        self.memory_service.remove_assignment(24)
        self.text_service.remove_assignment(24)
        self.binary_service.remove_assignment(24)

        self.assertEqual(len(self.memory_service.print_list()), lenm - 1)
        self.assertEqual(len(self.binary_service.print_list()), lenb - 1)
        self.assertEqual(len(self.text_service.print_list()), lent - 1)

    def test_update_assignment(self):
        self.memory_service.add_assignment(24, 'Global warming', '2024-12-08')
        self.text_service.add_assignment(24, 'Global warming', '2024-12-08')
        self.binary_service.add_assignment(24, 'Global warming', '2024-12-08')

        assignment = Assignment(24, 'Global politics', '2024-12-08')
        self.memory_service.update_assignment(24, 'Global politics', '2024-12-08')
        self.text_service.update_assignment(24, 'Global politics', '2024-12-08')
        self.binary_service.update_assignment(24, 'Global politics', '2024-12-08')

        self.assertEqual(self.memory_service.find_assignment_by_id(24).descript, assignment.descript)
        self.assertEqual(self.text_service.find_assignment_by_id(24).descript, assignment.descript)
        self.assertEqual(self.binary_service.find_assignment_by_id(24).descript, assignment.descript)

        self.assertEqual(self.memory_service.find_assignment_by_id(24).deadline, assignment.deadline)
        self.assertEqual(self.text_service.find_assignment_by_id(24).deadline, assignment.deadline)
        self.assertEqual(self.binary_service.find_assignment_by_id(24).deadline, assignment.deadline)