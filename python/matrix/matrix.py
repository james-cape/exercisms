class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix_rows = matrix_string.split("\n")

    def row(self, index):
        row_object = self.matrix_rows[index - 1].split(" ")
        return [int(x) for x in row_object]

    def column(self, index):
        column_object = []
        for i in range(len(self.matrix_rows)):
            column_object.append(self.row(i + 1)[index - 1])
        return column_object
