from faker.providers.bank.es_MX import is_valid_clabe

from src.exceptions.incorrect_input import IncorrectInputException
from src.exceptions.duplicate_objects import DuplicateObjectException
from src.exceptions.no_more_undo_redo import NoMoreUndoException, NoMoreRedoException
from src.exceptions.obj_not_found import ObjectNotFoundException
from src.domain.student import Student
from datetime import datetime


class ConsoleUI:
    def __init__(self, student_services, assignment_services, grade_services, undo_services):
        self._student_services = student_services
        self._assignment_services = assignment_services
        self._grade_services = grade_services
        self._undo_services = undo_services

    def print_menu(self):
        print("This is the menu. The following functionalities are provided:\n"
              "1 - Manage the students and assignments.\n"
              "2 - Give assignments to a student or a group of students\n"
              "3 - Grade student for a given assignment.\n"
              "4 - Create statistics\n"
              "5 - Undo LPO\n"
              "6 - Redo LPO\n")

    def print_manage_menu(self, obj):
        print("The following functionalities are provided regarding the management of students and assignments:\n"
              f"1 - Add {obj}.\n"
              f"2 - Remove {obj}.\n"
              f"3 - Update {obj}.\n"
              f"4 - Display the list of {obj}.\n")

    def validate_input_student(self, id, name, group): #
        try:
            errors = ""
            if not id.isdigit():
                errors += 'id must be positive integer number! '
            if name == "":
                errors += 'student name cannot be empty! '
            if not group.isdigit():
                errors += 'group must be positive integer number!'

            if errors != '':
                raise IncorrectInputException(errors)
        except IncorrectInputException as e:
            print(e)
            return False
        return True

    def is_valid_date(self, date_str, date_format="%Y-%m-%d"):
        try:
            datetime.strptime(date_str, date_format) # parse the string using the provided date format
            return True
        except ValueError:
            return False

    def validate_input_assignment(self, id, descript, deadline):
        try:
            errors = ""
            if not id.isdigit():
                errors += 'id must be positive integer number! '
            if descript == "":
                errors += 'description cannot be empty! '
            if not self.is_valid_date(deadline):
                errors += 'deadline must be a valid date!'

            if errors != '':
                raise IncorrectInputException(errors)
        except IncorrectInputException as e:
            print(e)
            return False
        return True

    def validate_input_grade(self, grade):
        try:
            errors = ""
            if not grade.isdigit():
                errors += 'grade must be positive integer number! '
            if not (0 < int(grade) <= 10):
                errors += 'grade must be between 1 and 10 '

            if errors != '':
                raise IncorrectInputException(errors)
        except IncorrectInputException as e:
            print(e)
            return False
        return True

    def execute_command(self):
        print("Your choice: ")
        choice1 = int(input("> "))

        if choice1 == 1:
            obj = input("Please introduce the objects you want to manage(students or assignments): ")

            if obj == 'students':
                self.print_manage_menu(obj)
                print("Your choice: ")
                choice2 = int(input("> "))

                if choice2 == 1:
                    id = input('id student: ')
                    name = input('name student: ')
                    group = input('group student: ')
                    if self.validate_input_student(id, name, group):
                        id = int(id); group = int(group)
                        try:
                            self._student_services.add_student(id, name, group)
                            print('The student was added!')
                        except DuplicateObjectException as e:
                            print(e)
                elif choice2 == 2:
                    id = input('id student: ')
                    if not id.isdigit():
                        print("id must be positive integer number!")
                    else:
                        id = int(id)
                        try:
                            self._student_services.remove_student(id)
                            print('The student was removed!')
                            print('The assignments of the student were removed!')
                        except ObjectNotFoundException as e:
                            print(e)
                elif choice2 == 3:
                    id = input('id student: ')
                    name = input('name student: ')
                    group = input('group student: ')
                    if self.validate_input_student(id, name, group):
                        id = int(id); group = int(group)
                        try:
                            self._student_services.update_student(id, name, group)
                            print('The student was updated!')
                        except ObjectNotFoundException as e:
                            print(e)
                elif choice2 == 4:
                    self.print_students()

            elif obj == 'assignments':
                self.print_manage_menu(obj)
                print("Your choice: ")
                choice2 = int(input("> "))

                if choice2 == 1:
                    id = input('id assignment: ')
                    descript = input('description assignment: ')
                    deadline = input('deadline assignment(YYYY-MM-DD): ')
                    if self.validate_input_assignment(id, descript, deadline):
                        id = int(id)
                        try:
                            self._assignment_services.add_assignment(id, descript, deadline)
                            print('The assignment was added!')
                        except DuplicateObjectException as e:
                            print(e)
                elif choice2 == 2:
                    id = input('id assignment: ')
                    if not id.isdigit():
                        print("id must be positive integer number!")
                    else:
                        id = int(id)
                        try:
                            self._assignment_services.remove_assignment(id)
                            print('The assignment was removed!')
                            print('All grades for this assignment were removed!')
                        except ObjectNotFoundException as e:
                            print(e)
                elif choice2 == 3:
                    id = input('id assignment: ')
                    descript = input('description assignment: ')
                    deadline = input('deadline assignment(YYYY-MM-DD): ')
                    if self.validate_input_assignment(id, descript, deadline):
                        id = int(id)
                        try:
                            self._assignment_services.update_assignment(id, descript, deadline)
                            print('The assignment was updated!')
                        except ObjectNotFoundException as e:
                            print(e)
                elif choice2 == 4:
                    self.print_assignments()


            else:
                print('You must introduce key words students or assignments!')

        elif choice1 == 2:
            print("Who do you want to give assignments to:\n"
                  "1 - One student.\n"
                  "2 - A group of students.\n")
            choice2 = int(input("> "))

            assignment_id = input("id assignment: ")
            if not assignment_id.isdigit():
                print("IDs must be positive integer numbers!")
            else:
                assignment_id = int(assignment_id)
            try:
                self._assignment_services.check_assignment_exists(assignment_id)
            except ObjectNotFoundException as e:
                print(e)

            if choice2 == 1:
                student_id = input("id student: ")
                if not student_id.isdigit():
                    print("IDs must be positive integer numbers!")
                else:
                    student_id = int(student_id)
                    try:
                        self._student_services.check_student_exists(student_id)
                    except ObjectNotFoundException as e:
                        print(e)
                    try:
                        self._grade_services.add_grade(assignment_id, student_id, 0)
                        print('The assignment was given to the student!')
                        self.print_grades(self._grade_services.print_list())
                    except DuplicateObjectException as e:
                        print(e)
            else:
                group = input("the group: ")
                if not group.isdigit():
                    print("The group must be a positive integer number!")
                else:
                    group = int(group)
                    students_ids = self._student_services.find_students_ids_by_group(group)
                    if students_ids is not None:
                        exists = False
                        for student_id in students_ids:
                            try:
                                self._grade_services.add_grade(assignment_id, student_id, 0)
                                exists = True
                            except DuplicateObjectException as e:
                                print(e)
                        if exists is True:
                            print('The assignment was given to the students of the group that were not previously given it!')
                            self.print_grades(self._grade_services.print_list())
                        else:
                            print('\nAll students of the group were already given the assignment!\n')
                    else:
                        print('This group does not exist!')



        elif choice1 == 3:
            student_id = input("For which student we do the grading: ")
            if not student_id.isdigit():
                print("IDs must be positive integer numbers!")
            else:
                student_id = int(student_id)
                try:
                    self._student_services.check_student_exists(student_id)
                except ObjectNotFoundException as e:
                    print(e)

                print(f"The list of ungraded assignments of student {student_id}:\n ")
                ungraded_id_assignments_list = self._grade_services.print_list_by_ungraded(student_id)
                ungraded_assignments_list = self.compute_ungraded_assignments_list(ungraded_id_assignments_list)
                self.print_ungraded_assignments(ungraded_assignments_list)
                print()

                assignment_id = input("Choose an assignment id from the list of ungraded assignments: ")
                if not assignment_id.isdigit():
                    print("IDs must be positive integer numbers!")
                else:
                    assignment_id = int(assignment_id)
                    try:
                        if not assignment_id in ungraded_id_assignments_list:
                            raise IncorrectInputException('you must choose an assignment from the list above!')
                        grade = input("grade = ")
                        if self.validate_input_grade(grade):
                            grade = int(grade)
                            self._grade_services.update_grade(assignment_id, student_id, grade)
                            print('The grade was given to the student!')
                            self.print_grades(self._grade_services.print_list())
                    except IncorrectInputException as e:
                        print(e)

        elif choice1 == 4:
            print("What do you want to know?\n"
                  "1. All students who received a given assignment, ordered descending by grade.\n"
                  "2. All students who are late in handing in at least one assignment.\n"
                  "3. Students with the best school situation, sorted in descending order of the average grade.\n")
            choice2 = int(input("> "))
            if choice2 == 1:
                assignment_id = input("assignment id: ")
                if not assignment_id.isdigit():
                    print("IDs must be positive integer numbers!")
                else:
                    assignment_id = int(assignment_id)
                    grades = self._grade_services.filter_by_assignment(assignment_id)
                    self.print_students_with_assignment(grades)
            elif choice2 == 2:
                result = self._grade_services.find_late_students()

                for data in result:
                    # Assignment late to be handed in if ungraded and deadline before current date
                    late_assignments = []
                    for assignment_id in data.ungraded_assignments:
                        assignment = self._assignment_services.find_assignment_by_id(assignment_id)
                        deadline_as_date = datetime.strptime(assignment.deadline, "%Y-%m-%d")
                        if deadline_as_date < datetime.now():
                            late_assignments.append(assignment_id)

                    if len(late_assignments) > 0:
                        student = self._student_services.find_student_by_id(data.student_id)
                        print(str(student) + " is late in handing in assignments: " + str(late_assignments))

            elif choice2 == 3:
                result = self._grade_services.sort_desc_by_average()
                for data in result:
                    student = self._student_services.find_student_by_id(data.student_id)
                    print(str(student) + " with average: " + str(data.average_grade))
        elif choice1 == 5:
            try:
                self._undo_services.undo()
                print("The LPO was undone!")
            except NoMoreUndoException as ex:
                print(ex)
        elif choice1 == 6:
            try:
                self._undo_services.redo()
                print("The LPO was redone!")
            except NoMoreRedoException as ex:
                print(ex)
        elif choice1 == 7:
            self.print_grades(self._grade_services.print_list())
        else:
            print("\nError: Invalid operation!\n")


    def print_students(self):
        for student in self._student_services.print_list():
            print(str(student))

        if len(self._student_services.print_list()) == 0:
            print("The list is empty.\n")

    def print_students_with_assignment(self, grades):
        for grade in grades:
            student_id = grade.student
            print(self._student_services.find_student_by_id(student_id), end = " ")
            grade_value = grade.value
            print(f"with grade {grade_value}")

        if len(self._student_services.print_list()) == 0:
            print("The list is empty.\n")

    def print_assignments(self):
        for assignment in self._assignment_services.print_list():
            print(str(assignment))

        if len(self._assignment_services.print_list()) == 0:
            print("The list is empty.\n")

    def print_grades(self, glist):
        for grade in glist:
            print(str(grade))

        if len(glist) == 0:
            print("The list is empty.\n")

    def compute_ungraded_assignments_list(self, id_list):
        ungraded_assignments = []
        for assignment_id in id_list:
            assignment = self._assignment_services.find_assignment_by_id(assignment_id)
            ungraded_assignments.append(assignment)
        return ungraded_assignments

    def print_ungraded_assignments(self, alist):
        for assignment in alist:
            print(str(assignment))

        if len(alist) == 0:
            print("The list is empty.\n")

    def start(self):
        while True:
            self.print_menu()
            self.execute_command()
