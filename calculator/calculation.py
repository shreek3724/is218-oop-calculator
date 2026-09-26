class Add:
    '''represents addition calculation with two numbers'''

    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def get_result(self) -> float:
        """executes the addition operation"""
        return self.a + self.b #returns the result