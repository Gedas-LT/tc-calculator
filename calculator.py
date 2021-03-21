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
        try:
            if b == None:
                result = self.__memory / a
                self.__memory = result
                return result
            else:
                result = a / b
                self.__memory = result
                return result
        except ZeroDivisionError:
            print("You cannot divide by zero!")

    def root(self, root: int, num: int = None) -> float:
        if num == None:
            result = self.__memory ** (1 / root)
            self.__memory = result
        else:
            result = num ** (1 / root)
            self.__memory = result
            return result



cal = Calculator()


cal.divide(10, 0)