class ThreeParamAddition:
    def __init__(self, param1, param2, param3):
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3

    def __add__(self, other):
        if isinstance(other, ThreeParamAddition):
            return ThreeParamAddition(self.param1 + other.param1, self.param2 + other.param2, self.param3 + other.param3)
        else:
            raise TypeError("Unsupported operand type(s) for +: '{}' and '{}'".format(type(self), type(other)))

    def __str__(self):
        return "({}, {}, {})".format(self.param1, self.param2, self.param3)

a = ThreeParamAddition(1, 2, 3)
b = ThreeParamAddition(4, 5, 6)
c = a + b
print(c)