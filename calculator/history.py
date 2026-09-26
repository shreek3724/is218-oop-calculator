from calculator.calculation import Calculation

# this is a history management module for calculator operations

class History: 
    def __init__(self) -> None:
        self._calculations: list[Calculation] = []

    def add(self, calculation: Calculation) -> None:
        #adds a calculation to history after verifying its type
        if not isinstance(calculation, Calculation):
            raise TypeError("Only Calculation instances can be added to history")
        self._calculations.append(calculation)

    def get_history(self) -> list[Calculation]:
        # returns a shallow copy of the calculations history list
        return self._calculations.copy()

    def remove(self, index: int) -> Calculation:
        # removes and returns a calculation at index
        # rejects negative indexes
        if index < 0 or index >= len(self._calculations):
            raise IndexError("Index out of range!")
        return self._calculations.pop(index)