from textwrap import wrap

student_list = [
    'Alice',
    'Bob',
    'Charlie',
    'David',
    'Eve',
    'Fred',
    'Ginny',
    'Harriet',
    'Ileana',
    'Joseph',
    'Kincaid',
    'Larry'
]

plant_list = [
    'Grass',
    'Clover',
    'Radishes',
    'Violets'
]

class Garden(object):
    def __init__(self, diagram, students = student_list):
        self.plant_pots = wrap(diagram.replace("\n", ""), 2)
        self.student_list = sorted(students)
        self.plant_dictionary = {}
        for i in plant_list:
            self.plant_dictionary[i[0]] = i

    def plants(self, student):
        top_row = self.student_list.index(student)
        bottom_row = int(top_row + len(self.plant_pots) / 2)
        accumulator = []
        for plant in self.plant_pots[top_row] + self.plant_pots[bottom_row]:
            accumulator.append(self.plant_dictionary[plant])
        return accumulator
