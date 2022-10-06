class STUDENT:
    __MAX_GRADE = 100

    name: str
    surname: str
    record_book_id: int
    __grades: list

    def __init__(self,
                 name: str,
                 surname: str,
                 record_book_id: int = 0):
        if name is None or name == '':
            raise AttributeError('Name can\'t be empty')
        self.name = name
        if surname is None or surname == '':
            raise AttributeError('Surname can\'t be empty')
        self.surname = surname
        self.record_book_id = record_book_id
        self.__grades = list()

    def add_grades(self, *grades: int):
        for grade in grades:
            if grade < 0 or grade > self.__MAX_GRADE:
                raise ValueError(f'Grade {grade} is out of range')
            self.__grades.append(grade)
        return self

    def avg_grade(self):
        return sum(self.__grades) / len(self.__grades)


class GROUP:
    __STUDENTS_MAX = 20

    name: str
    students: list

    def __init__(self, name):
        self.name = name
        self.students = list()

    def add_students(self, *students: STUDENT):
        if len(self.students) + len(students) > self.__STUDENTS_MAX:
            raise IndexError(f'Unable to store more than \
            {self.__STUDENTS_MAX} students in a group')
        for student in students:
            self.__add_student(student)

    def top_five(self):
        students_dict = {student: student.avg_grade() for student in self.students}
        return sorted(students_dict, key=students_dict.get, reverse=True)[:5]

    def __add_student(self, new_student: STUDENT):
        for student in self.students:
            if new_student.name == student.name and \
                    new_student.surname == student.surname:
                raise ValueError(f'Student {student.name} {student.surname} \
                already exists')
        self.students.append(new_student)
