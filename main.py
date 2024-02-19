# main.py

class StudentsInMLOps:
    def __init__(self):
        self.total_strength = 0
        self.class_name = "MLOps"

    def enrollStudents(self, count):
        self.total_strength += count

    def dropStudents(self, count):
        self.total_strength -= count
        if self.total_strength < 0:
            self.total_strength = 0

    def getTotalStrength(self):
        return self.total_strength

    def getClassName(self):
        return self.class_name


if __name__ == "__main__":
    # Example usage
    mlops_class = StudentsInMLOps()
    mlops_class.enrollStudents(10)
    print(f"Total Strength: {mlops_class.getTotalStrength()}")
    print(f"Class Name: {mlops_class.getClassName()}")
    mlops_class.dropStudents(5)
    print(f"Total Strength after dropping 5 students: {mlops_class.getTotalStrength()}")
