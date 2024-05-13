class Square:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # b^2-4ac
    def Discr(self):
        D = self.b ** 2 - 4 * self.a * self.c
        return D

    def X(self):
        D = self.b ** 2 - 4 * self.a * self.c
        x_1 = (-self.b + (D ** 1 / 2) / 2 * self.a)
        if D > 0:
            x_2 = (-self.b - (D ** 1 / 2) / 2 * self.a)
            return x_1, x_2
        elif D == 0:
            return x_1
        else:
            print("No X")
