from calculator.calculation import Add

def test_add_instance_creation():
    # verifies that an add instance correctly stores attributes
    calc = Add(2.0,3.0)
    assert calc.a == 2.0
    assert calc.b == 3.0

def test_add_execute_positive():
    # verifies addition with pos numbers
    calc = Add(5.0, 5.0)
    assert calc.get_result() == 10.0

def test_add_execute_negative():
    # verifies addition with neg numbers
    calc = Add(-2.0, -4.0)
    assert calc.get_result() == -6.0

def test_add_execute_floats():
    # verifies addition with pos float values
    calc = Add(1.5, 2.5)
    assert calc.get_result() == 4.0

'''tests instance attributes
execution results
negative numbers
and floating point values'''

def test_add_independent_state_immutability():
    # arrange the operands
    a = 12.0
    b = -4.0
    calc = Add(a, b)

    # act
    result = calc.get_result()

    # assert correct answer
    assert result == 8.0

    # assrt asking for answer did not change either of the operands
    assert calc.a == 12.0
    assert calc.b == -4.0