class Matrix:

    def __init__(self, rows, columns) -> object:
        (self.rows, self.columns) = (rows, columns)
        self.values = [[0 for i in range(self.columns)] for i in range(self.rows)]

    @classmethod
    def create_from_array(cls, data):
        cls = Matrix(len(data), len(data[0]))
        cls.values = [[data[row][col] for col in range(cls.columns)] for row in range(cls.rows)]
        return cls

    @classmethod
    def create_void(cls):
        cls = Matrix(0, 0)
        return cls

    def dim(self):
        return self.rows, self.columns

    def display(self, before="", after=""):
        print(before)
        if self.is_void():
            print([None])
        else:
            for i in range(self.rows):
                print(self.values[i])
        print(after)

    def edit(self, row, column, value):
        old = self.values[row - 1][column - 1]
        self.values[row - 1][column - 1] = value
        return old

    def is_void(self):
        if self.rows == 0 or self.columns == 0:
            return True
        else:
            return False

    def linear_matrix(self):
        for row in range(A.rows):
            for column in range(self.columns):
                self.values[row][column] = row * self.columns + column

    def add(self, other_matrix):
        if self.dim() == other_matrix.dim():
            result = Matrix(self.rows, self.columns)
            for row in range(self.rows):
                for col in range(self.columns):
                    result.values[row][col] = self.values[row][col] + other_matrix.values[row][col]
            return result
        else:
            return Matrix.create_void()

    def multiply(self, other_matrix):
        A = self
        B = other_matrix

        if A.columns == B.rows:
            multiplied = Matrix(A.rows, B.columns)
            for row in range(multiplied.rows):
                for col in range(multiplied.columns):
                    r = 0
                    for k in range(A.columns):
                        r += A.values[row][k] * B.values[k][col]
                    multiplied.values[row][col] = r
            return multiplied
        else:
            return Matrix.create_void()


V = Matrix.create_void()
V.display()

A = Matrix(4, 4)
B = Matrix(6, 4)
A.linear_matrix()
B.linear_matrix()
'''
print("__________________")
C = A.multiply(B)
print("__________________")

C.display("C = ")

D = matrix.create_from_array([[-2, 0, 5, -6, 8, 2, 2.5, 8],
                              [3, -1, 4, -3, -1, 0, 2, 7],
                              [1, 1, 3, 5, -6, 7, 2, 0],
                              [1, 2, 5, -1, 7, -0, -7, 1],
                              [8, -6, 4, 1, -3, 4, 0, 1],
                              [8, -6, 4, 1, -3, 4, 0, 1],
                              [8, -6, 4, 1, -3, 4, 0, 1],
                              [8, -6, 4, 1, -3, 4, 0, 1]])
A.multiply(D).display("E = ")
A2 = A.multiply(A)
A2.display("A2 =")'''
