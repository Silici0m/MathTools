import math


class Polynomial:
    def __init__(self, values):

        while values[0] == 0:
            values = values[1:]
            if len(values) == 0:
                break

        self.degree = len(values) - 1
        self.coefficients = values

    def display(self, before="", after=""):
        r = before
        for i in range(len(self.coefficients)):
            exponent = len(self.coefficients) - i - 1
            if exponent > 2:
                r += str(self.coefficients[i]) + "xE" + str(len(self.coefficients) - i - 1) + " + "
            elif exponent == 2:
                r += str(self.coefficients[i]) + "x² + "
            elif exponent == 1:
                r += str(self.coefficients[i]) + "x + "
            else:
                r += str(self.coefficients[i])

        print(r + after)

    def roots(self):

        if self.degree == -1:
            return set()

        elif self.degree == 0:
            if self.coefficients[0] == 0:
                return set()
            else:
                return {math.inf}

        elif self.degree == 1:
            return (-self.coefficients[1]) / self.coefficients[0]

        elif self.degree == 2:
            a = self.coefficients[0]
            b = self.coefficients[1]
            c = self.coefficients[2]
            delta = b ** 2 - 4 * a * c
            if delta > 0:
                return {(-b - delta ** (1 / 2)) / (2 * a), (-b + delta ** (1 / 2)) / (2 * a)}
            elif delta < 0:
                return set()
            else:
                return -b / (2 * a)
        else:
            return set()
