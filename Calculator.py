class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def addition(self):
        return self.x + self.y

    def subtraction(self):
        return self.x - self.y

    def multiplication(self):
        return self.x * self.y

    def division(self):
        return self.x / self.y


n1 = Calculator(7, 5)
n1.addition()
print(n1.addition())
n1.subtraction()
print(n1.subtraction())
n1.multiplication()
print(n1.multiplication())
n1.division()
print(n1.division())

