class Calculator:

    def __init__(self) -> None:
        self.__memory = 0
    
    @property
    def memory(self):
        return self.__memory

    def memory_reset(self):
        self.__memory = 0

    def add(self, a: int, b: int = None) -> int:
        if b == None:
            result = self.__memory + a
            self.__memory = result
            return result
        else:
            result = a + b
            self.__memory = result
            return result

    def subtract(self, a: int, b: int = None) -> int:
        if b == None:
            result = self.__memory - a
            self.__memory = result
            return result
        else:
            result = a - b
            self.__memory = result
            return result

    def multiplicate(self, a: int, b: int = None) -> int:
        if b == None:
            result = self.__memory * a
            self.__memory = result
            return result
        else:
            result = a * b
            self.__memory = result
            return result

    def divide(self, a: int, b: int = None) -> float:
        if b == None:
            result = self.__memory / a
            self.__memory = result
            return result
        else:
            result = a / b
            self.__memory = result
            return result

    def root(self, root: int, num: int = None) -> float:
        if num == None:
            result = self.__memory ** (1 / root)
            self.__memory = result
        else:
            result = num ** (1 / root)
            self.__memory = result
            return result



cal = Calculator()

print("Result:", cal.subtract(10, 7))
print("Memory:", cal.memory)
cal.memory_reset()
print("Memory:", cal.memory)
print("Result:", cal.multiplicate(3, 5))
print("Memory:", cal.memory)
cal.memory_reset()
print("Memory:", cal.memory)
#print("Result:", cal.divide(10, 4))
#print("Result:", cal.root(3, 8))
#print("Memory:", cal.memory)