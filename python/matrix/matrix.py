class Matrix(object):
    def __init__(self, matrix_string):
        lines = matrix_string.split('\n')
        self.matrix = []
        for line in lines:
            self.matrix.append(line.split(' '))
        for r in range(0, len(self.matrix)):
            for c in range(0, len(self.matrix[r])):
                self.matrix[r][c] = int(self.matrix[r][c])

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        output = []
        for line in self.matrix:
            output.append(line[index-1])
        return output
