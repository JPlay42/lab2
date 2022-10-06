import unittest

from ex5 import STUDENT, GROUP


class TestEx5(unittest.TestCase):
    def test_empty_name_surname_exceptions(self):
        with self.assertRaises(AttributeError):
            STUDENT(None, 'Surname')
        with self.assertRaises(AttributeError):
            STUDENT('Name', None)

    def test_max_group_capacity(self):
        group = GROUP('TV-12')
        for i in range(20):
            group.add_students(STUDENT(str(i), str(i)))
        with self.assertRaises(IndexError):
            group.add_students(STUDENT('Vasya', 'Pumpkin'))

    def test_student_grade_validation(self):
        student = STUDENT('Vasya', 'Pumpkin')
        with self.assertRaises(ValueError):
            student.add_grades(-1)
        with self.assertRaises(ValueError):
            student.add_grades(101)
        student.add_grades(0)
        student.add_grades(100)

    def test_average_grade(self):
        student = STUDENT('Vasya', 'Pumpkin')
        student.add_grades(0, 50, 90, 100)
        self.assertEqual(60, student.avg_grade())

    def test_top_five(self):
        students = (
            STUDENT('a', 'a', 0).add_grades(60, 70, 80),  # 70
            STUDENT('b', 'b', 1).add_grades(70, 80),  # 75
            STUDENT('c', 'c', 2).add_grades(100, 99),  # 99.5
            STUDENT('d', 'd', 3).add_grades(80),  # 80
            STUDENT('e', 'e', 4).add_grades(60, 68),  # 64
            STUDENT('f', 'f', 5).add_grades(50, 70),  # 60
            STUDENT('g', 'g', 6).add_grades(82, 88)  # 85
        )
        group = GROUP('TV-12')
        group.add_students(*students)
        top_five = group.top_five()
        self.assertEqual(5, len(top_five))
        self.assertEqual(2, top_five[0].record_book_id)
        self.assertEqual(6, top_five[1].record_book_id)
        self.assertEqual(3, top_five[2].record_book_id)
        self.assertEqual(1, top_five[3].record_book_id)
        self.assertEqual(0, top_five[4].record_book_id)


if __name__ == '__main__':
    unittest.main()
