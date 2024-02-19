# test.py
import unittest
from main import StudentsInMLOps

class TestStudentsInMLOps(unittest.TestCase):

    def setUp(self):
        self.mlops_class = StudentsInMLOps()

    def test_enroll_students(self):
        self.mlops_class.enrollStudents(5)
        self.assertEqual(self.mlops_class.getTotalStrength(), 5)

    def test_drop_students(self):
        self.mlops_class.enrollStudents(10)
        self.mlops_class.dropStudents(3)
        self.assertEqual(self.mlops_class.getTotalStrength(), 7)

    def test_drop_students_below_zero(self):
        self.mlops_class.enrollStudents(5)
        self.mlops_class.dropStudents(10)
        self.assertEqual(self.mlops_class.getTotalStrength(), 0)

    def test_get_class_name(self):
        self.assertEqual(self.mlops_class.getClassName(), "MLOps")

if __name__ == '__main__':
    unittest.main()
