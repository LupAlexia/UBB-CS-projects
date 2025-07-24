from src.repository.repo_text_student import TextFileRepoStudent
from src.repository.repo_binary_student import BinaryFileRepoStudent
from src.repository.repo_mem_student import InMemoryRepoStudent
from src.repository.repo_text_assignment import TextFileRepoAssignment
from src.repository.repo_binary_assignment import BinaryFileRepoAssignment
from src.repository.repo_mem_assignment import InMemoryRepoAssignment
from src.repository.repo_text_grade import TextFileRepoGrade
from src.repository.repo_binary_grade import BinaryFileRepoGrade
from src.repository.repo_mem_grade import InMemoryRepoGrade
from src.services.services_assignment import ServicesAssignment
from src.services.services_grade import ServicesGrade
from src.services.services_student import ServicesStudent
from src.services.sevices_undo import ServicesUndo
from src.ui.console_ui import ConsoleUI


class Settings:
    def __init__(self):
        self.__settings = {} #dictionary
        self.read_settings()

    def read_settings(self):
        lines = []
        with open('settings.properties', 'r') as f:
            lines = f.read().split('\n')  # reads all file content
            for line in lines:
                setting = line.split('=')
                self.__settings[setting[0].strip()] = setting[1].strip()

    def config(self):
        student_repo = None; assignment_repo = None; grade_repo = None
        if self.__settings['repository'] == "in-memory":
            student_repo = InMemoryRepoStudent()
            assignment_repo = InMemoryRepoAssignment()
            grade_repo = InMemoryRepoGrade()
        if self.__settings['repository'] == "text-file":
            student_repo = TextFileRepoStudent(self.__settings["students"])
            assignment_repo = TextFileRepoAssignment(self.__settings["assignments"])
            grade_repo = TextFileRepoGrade(self.__settings["grades"])
        if self.__settings['repository'] == "binary":
            student_repo = BinaryFileRepoStudent(self.__settings["students"])
            assignment_repo = BinaryFileRepoAssignment(self.__settings["assignments"])
            grade_repo = BinaryFileRepoGrade(self.__settings["grades"])

        # Dependency injection
        services_undo = ServicesUndo()
        services_grade = ServicesGrade(grade_repo, services_undo)
        services_student = ServicesStudent(student_repo, services_undo, services_grade)
        services_assignment = ServicesAssignment(assignment_repo, services_undo, services_grade)

        ui = None
        if self.__settings['ui'] == "console":
            ui = ConsoleUI(services_student, services_assignment, services_grade, services_undo)
        #if self.__settings['ui'] == 'gui':
            #ui = GraphicUi(ctrl)

        return ui
