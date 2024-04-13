class CheckNum:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def checkMax(self):
        if self.num1 > self.num2:
            print(1)
        else:
            print(2)
m = CheckNum(2,4)
m.checkMax()