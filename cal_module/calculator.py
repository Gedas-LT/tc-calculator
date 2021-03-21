class Calculator:
    """
    A class used for basic mathematical functions.

    ...

    Attributes
    ----------
    None

    Methods
    -------
    memory():
        Returns value of memory.
    memory_reset():
        Resets value of memory.
    add(a, b=None):
        Adds two integer numbers.
    subract(a, b=None):
        Subtracts two integer numbers.
    multiplicate(a, b=None):
        Multiplicates two integer numbers.
    divide(a, b=None):
        Divides two integer numbers.
    root(root, num=None)
        Takes (num) root of number.
    """ 

    def __init__(self) -> None:
        self.__memory = 0
    
    @property
    def memory(self):
        """
        Returns value of memory.

        Parameters
        ----------
        None

        Returns
        ------
        self.__memory : int
            Current value of memory.
        """
        return self.__memory

    def memory_reset(self):
        """
        Resets value of memory to 0 (zero).

        Parameters
        ----------
        None

        Returns
        ------
        None
        """
        self.__memory = 0

    def add(self, a: int, b: int = None) -> int:
        """
        Adds two integer numbers.

        If the argument "b" isn't passed in, the value of memory is used. 

        Parameters
        ----------
        a : int
            A decimal integer.
        b : int, optional
            Another decimal integer (default is None).

        Returns
        ------
        result : int
            Sum of a and b.
        """
        if b == None:
            result = self.__memory + a
            self.__memory = result
            return result
        else:
            result = a + b
            self.__memory = result
            return result

    def subtract(self, a: int, b: int = None) -> int:
        """
        Subtracts two integer numbers.

        If the argument "b" isn't passed in, the value of memory is used.

        Parameters
        ----------
        a : int
            A decimal integer.
        b : int, optional
            Another decimal integer (default is None).

        Returns
        ------
        result : int
            Result of subtraction of a and b.
        """
        if b == None:
            result = self.__memory - a
            self.__memory = result
            return result
        else:
            result = a - b
            self.__memory = result
            return result

    def multiplicate(self, a: int, b: int = None) -> int:
        """
        Multiplicates two integer numbers.

        If the argument "b" isn't passed in, the value of memory is used.

        Parameters
        ----------
        a : int
            A decimal integer.
        b : int, optional
            Another decimal integer (default is None).

        Returns
        ------
        result : int
            Result of multiplication of a and b.
        """
        if b == None:
            result = self.__memory * a
            self.__memory = result
            return result
        else:
            result = a * b
            self.__memory = result
            return result

    def divide(self, a: int, b: int = None) -> float:
        """
        Divides two integer numbers.

        If the argument "b" isn't passed in, the value of memory is used.

        Parameters
        ----------
        a : int
            A decimal integer.
        b : int, optional
            Another decimal integer (default is None).

        Returns
        ------
        result : float
            Result of division of a and b.
        Error handling : str
            "You cannot divide by zero!" string if catches ZeroDivisionError,
            when trying to divide by zero.  
        """
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
            return "You cannot divide by zero!"

    def root(self, root: int, num: int = None) -> float:
        """
        Takes (nth) root of number.

        If the argument "num" isn't passed in, the value of memory is used.

        Parameters
        ----------
        root : int
            The number (degree) of root.
        b : int, optional
            Decimal integer (default is None).

        Returns
        ------
        result : float
            Result of (nth) root of number.
        """
        if num == None:
            result = self.__memory ** (1 / root)
            self.__memory = result
            return result
        else:
            result = num ** (1 / root)
            self.__memory = result
            return result