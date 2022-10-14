class STUDENT:
    __MAX_GRADE = 100

    def __init__(self,
                 name: str,
                 surname: str,
                 record_book_id: int = 0):
        self.name = name
        self.surname = surname
        self.record_book_id = record_book_id
        self.__grades = list()

    def add_grades(self, *grades: int):
        for grade in grades:
            if not isinstance(grade, int):
                raise TypeError('All grades should be int')
            if grade < 0 or grade > self.__MAX_GRADE:
                raise ValueError(f'Grade {grade} is out of range')
            self.__grades.append(grade)
        return self

    def avg_grade(self):
        return sum(self.__grades) / len(self.__grades)

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def record_book_id(self):
        return self.__record_book_id

    @name.setter
    def name(self, name: str):
        if not isinstance(name, str):
            raise TypeError('Name should be string')
        if name == '':
            raise ValueError('Name can\'t be empty')
        self.__name = name

    @surname.setter
    def surname(self, surname: str):
        if not isinstance(surname, str):
            raise TypeError('Surname should be string')
        if surname == '':
            raise ValueError('Surname can\'t be empty')
        self.__surname = surname

    @record_book_id.setter
    def record_book_id(self, record_book_id: int):
        if not isinstance(record_book_id, int):
            raise TypeError('Record_book_id should be int')
        if record_book_id < 0:
            raise ValueError('Record_book_id can\'t be negative')
        self.__record_book_id = record_book_id


class GROUP:
    __STUDENTS_MAX = 20

    def __init__(self, name):
        self.name = name
        self.__students = list()

    def add_students(self, *students: STUDENT):
        if not all(isinstance(student, STUDENT) for student in students):
            raise TypeError('Only STUDENT instances are allowed')
        if len(self.__students) + len(students) > self.__STUDENTS_MAX:
            raise IndexError('Unable to store more than '
                             f'{self.__STUDENTS_MAX} students in a group')
        for student in students:
            self.__add_student(student)

    def top_five(self):
        students_dict = {student: student.avg_grade() for student in self.students}
        return sorted(students_dict, key=students_dict.get, reverse=True)[:5]

    def __add_student(self, new_student: STUDENT):
        for student in self.students:
            if new_student.name == student.name and \
                    new_student.surname == student.surname:
                raise ValueError(f'Student {student.name} {student.surname} '
                                 'already exists')
        self.students.append(new_student)

    @property
    def name(self):
        return self.__name

    @property
    def students(self):
        return self.__students

    @name.setter
    def name(self, name: str):
        if not isinstance(name, str):
            raise TypeError('Name should be str')
        if name == '':
            raise ValueError('Name can\'t be empty')
        self.__name = name
