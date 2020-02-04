class Calculator:
    def __init__(self):
        self.result = 0

    def sum(self, num):
        self.result += num
        return self.result

    def sub(self, num):
        self.result -= num
        return self.result

    def mul(self, num):
        self.result *= num
        return self.result

    def div(self, num):
        self.result /= num
        return self.result


cal = Calculator()
print(cal.sum(3))
print(cal.sub(2))
print(cal.mul(9))
print(cal.sub(3))
