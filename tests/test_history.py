import pytest
from calculator.calculation import Add, Subtract
from calculator.history import History

# tests for the history collection class

def test_history_starts_empty():
    history = History()
    assert len(history.get_history()) == 0

def test_add_to_history():
    history = History()
    history.add(Add(10,5))
    history.add(Subtract(20,7))
    assert len(history.get_history()) == 2

def test_add_invalid_type_raises_type_error():
    history = History()
    with pytest.raises(TypeError):
        history.add("not a calculation!")

def test_get_history_returns_copy():
    history = History()
    history.add(Add(10,5))
    snapshot = history.get_history()
    snapshot.clear()
    assert len(history.get_history()) == 1

def test_shallow_copy_mutates_underlying_object():
    history = History()
    history.add(Add(10,5))
    snapshot = history.get_history()
    snapshot[0].a = 99
    assert history.get_history()[0].get_result() == 104

def test_remove_valid_index():
    history = History()
    history.add(Add(10,5))
    history.add(Subtract(20,7))
    removed = history.remove(0)
    assert removed.get_result() == 15
    assert len(history.get_history()) == 1

def test_remove_negative_index_raises_index_error():
    history = History()
    history.add(Add(10,5))
    with pytest.raises(IndexError):
        history.remove(-1)
    assert len(history.get_history()) == 1

def test_remove_from_empty_history():
    # the independent test task
    # verifies that remove(0) on empty history raises an IndexError and leave history empty
    history = History()
    with pytest.raises(IndexError):
        history.remove(0)
    assert len(history.get_history()) == 0

# new appended tests as part of 5C

def test_remove_middle_entry_keeps_neighbors():
    history = History()
    first = Add(1, 2)
    middle = Subtract(5, 1)
    last = Add(10, 20)
    for calculation in [first, middle, last]:
        history.add(calculation)
    assert history.remove(1) is middle
    assert history.get_history() == [first, last]


def test_empty_history_rejects_removal():
    history = History()
    with pytest.raises(IndexError):
        history.remove(0)
    assert history.get_history() == []


def test_remove_last_entry_keeps_previous_order():
    history = History()
    first = Add(1, 2)
    middle = Subtract(5, 1)
    last = Add(10, 20)
    for calculation in [first, middle, last]:
        history.add(calculation)
    assert history.remove(2) is last
    assert history.get_history() == [first, middle]