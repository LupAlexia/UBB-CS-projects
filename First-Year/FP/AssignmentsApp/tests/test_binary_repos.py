import unittest

from src.domain.assignment import Assignment
from src.domain.student import Student
from src.repository.repo_binary_assignment import BinaryFileRepoAssignment
from src.repository.repo_binary_student import BinaryFileRepoStudent
from src.repository.repo_mem_assignment import InMemoryRepoAssignment
from src.repository.repo_mem_student import InMemoryRepoStudent


class StudentMemoRepoTestCase(unittest.TestCase):
    def setUp(self):
        self._reset_test_file('test_students.pickle')
        self.repo = BinaryFileRepoStudent('test_students.pickle')

    @staticmethod
    def _reset_test_file(filename):
        with open(filename, 'w') as file:
            file.truncate(0)

    def test_add(self):
        """Test add method:"""
        self.repo.add_student(Student(24, 'Aurel Popa', 10))
        student = self.repo.find_student_by_id(24)
        self.assertEqual(student.name, 'Aurel Popa')
        self.assertEqual(student.group, 10)


    def test_remove(self):
        """Test remove method: """
        self.repo.add_student(Student(25, 'Aurel Popa', 10))
        student = Student(25, 'Aurel Popa', 10)
        self.repo.remove_student(student)

        self.assertEqual(self.repo.find_student(student), None, 'remove method failed')

    def test_update(self):
        """Test remove method: """
        self.repo.add_student(Student(26, 'Aurel Popa', 10))
        student = Student(26, 'Aura Popa', 10)
        self.repo.update_student(student)

        self.assertEqual(self.repo.find_student_by_id(26), student, 'update method failed')

class AssignmentMemoRepoTestCase(unittest.TestCase):
    def setUp(self):
        self._reset_test_file('test_assignments.pickle')
        self.repo = BinaryFileRepoAssignment('test_assignments.pickle')

    @staticmethod
    def _reset_test_file(filename):
        with open(filename, 'w') as file:
            file.truncate(0)


    def test_add(self):
        """Test add method:"""
        self.repo.add_assignment(Assignment(24, 'Global warming', '2024-12-08'))
        assignment = self.repo.find_assignment_by_id(24)
        self.assertEqual(assignment.descript, 'Global warming')
        self.assertEqual(assignment.deadline, '2024-12-08')


    def test_remove(self):
        """Test remove method: """
        self.repo.add_assignment(Assignment(25, 'Global warming', '2024-12-08'))
        assignment = Assignment(25, 'Global warming', '2024-12-08')
        self.repo.remove_assignment(assignment)

        self.assertEqual(self.repo.find_assignment(assignment), None, 'remove method failed')

    def test_update(self):
        """Test remove method: """
        self.repo.add_assignment(Assignment(26, 'Global warming', '2024-12-08'))
        assignment = Assignment(26, 'Global politics', '2024-10-08')
        self.repo.update_assignment(assignment)

        self.assertEqual(self.repo.find_assignment_by_id(26), assignment, 'update method failed')

if __name__ == '__main__':
    print(__name__)
    unittest.main(verbosity = 2)