class School(object):
    def __init__(self):
        self.student_info = []

    def add_student(self, name, grade):
        student = Student(name, grade)
        self.student_info.append(student)

    def roster(self):
        return [student.name for student in self._list_by_name_and_grade()]

    def grade(self, grade_number):
        return [student.name for student in self._limit_by_grade(grade_number)]

    def _list_by_name_and_grade(self):
        return sorted(self.student_info, key=lambda x: (x.grade, x.name))

    def _limit_by_grade(self, grade_number):
        return list(filter(lambda x: x.grade == grade_number, self._list_by_name_and_grade()))

class Student():
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
