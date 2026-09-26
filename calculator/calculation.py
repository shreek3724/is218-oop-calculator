from abc import ABC, abstractmethod

class Calculation(ABC):
    # abstract base class for calculation operations

    def __init__(self, a: float, b: float) -> None:
        self.a = float(a)
        self.b = float(b)

    @ abstractmethod
    def get_result(self) -> float:
        # abstract method to get calculation result
        pass #pragma: no cover 

class Add(Calculation):
    # Concrete implementation for addition 

    def get_result(self) -> float:
        return self.a + self.b

class Subtract(Calculation):
    # Concrete implementation for subtraction 

    def get_result(self) -> float:
        return self.a - self.b

# the new version with abstract class

"""

# old version without abstract class: 

class Add:
    '''represents addition calculation with two numbers'''

    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def get_result(self) -> float:
        '''executes the addition operation'''
        return self.a + self.b #returns the result

class Subtract:
    '''respresents a subtraction calculation between two floats numbers'''

    def __init__(self, a:float, b:float):
        self.a = float(a)
        self.b = float(b)

    def get_result(self) -> float:
        '''executes the subtraction operation'''
        return self.a - self.b #returns the result
"""