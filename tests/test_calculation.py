import pytest
from calculator.calculation import Calculation, Add, Subtract

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

def test_subtract_execute_positive():
    calc = Subtract(10.0, 5.0)
    assert calc.get_result() == 5.0

def test_subtract_execute_negative():
    calc = Subtract(5.0, 10.0)
    assert calc.get_result() == -5.0

# adding the abstraction and polymorphism tests from the root test file
# also adding independent test

def test_calculation_is_abstract():
    # verifies that the calculation cannot be instatiated directly
    with pytest.raises(TypeError):
        Calculation(10.0, 5.0)

def test_polymorphism():
    # verifies uniform method invocation in a loop across subclasses
    calculations = [Add(10, 5), Subtract(20, 7)]
    results = []
    for calculation in calculations:
        results.append(calculation.get_result())
    assert results == [15, 13]

def test_independent_polymorphic_loop():
    # arrange 3 calcs, including a subtaction with a negative result
    calculations = [
        Add(15.0, 5.0),
        Subtract(4.0, 9.0),
        Add(3.5, 2.5)
    ]
    # act: ordinary loop collecting results without type checking
    results = []
    for calc in calculations:
        results.append(calc.get_result())
    # assert: verifuy the complete expected list
    assert results == [20.0, -5.0, 6.0]

# new appended tests as part of 5C

def test_decimal_addition():
    assert Add(0.1, 0.2).get_result() == pytest.approx(0.3)


def test_decimal_subtraction():
    assert Subtract(1.5, 0.25).get_result() == 1.25


def test_subtract_two_negative_operands():
    assert Subtract(-10, -5).get_result() == -5


def test_subtract_zero_operands():
    assert Subtract(0, 0).get_result() == 0