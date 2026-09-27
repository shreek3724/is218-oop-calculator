from calculator.cli import run

# new CLI test code
# a test conversation provides input and checks what the app prints

def session(monkeypatch, capsys, answers):
    # iter is a cursor; next takes one response for each input prompt.
    responses = iter(answers)

    def scripted_input(prompt):
        return next(responses)

    # pytest supplies these fixtures and restores input after the test.
    monkeypatch.setattr("builtins.input", scripted_input)
    run()
    return capsys.readouterr().out


def test_arithmetic_session(monkeypatch, capsys):
    output = session(monkeypatch, capsys,
                     ["add", "10", "5", "subtract", "20", "7", "exit"])
    assert "Result: 15" in output
    assert "Result: 13" in output
    assert output.endswith("Goodbye!\n")


def test_history_and_removal(monkeypatch, capsys):
    output = session(monkeypatch, capsys,
                     ["add", "10", "5", "subtract", "20", "7",
                      "history", "remove", "1", "history", "exit"])
    assert "1. Add: 10, 5 = 15" in output
    assert "2. Subtract: 20, 7 = 13" in output
    assert "Removed: Add: 10, 5 = 15" in output
    assert output.endswith("1. Subtract: 20, 7 = 13\nGoodbye!\n")


def test_empty_history(monkeypatch, capsys):
    output = session(monkeypatch, capsys, ["history", "remove", "exit"])
    assert output.count("No calculations in history.") == 2


def test_help_and_unknown_command(monkeypatch, capsys):
    output = session(monkeypatch, capsys, [" HELP ", "pizza", " EXIT "])
    assert "Commands:" in output
    assert "Unknown command." in output
    assert output.endswith("Goodbye!\n")


def test_invalid_first_number_recovers(monkeypatch, capsys):
    output = session(monkeypatch, capsys,
                     ["add", "hello", "history", "add", "2", "3", "exit"])
    assert "Invalid number or result." in output
    assert "No calculations in history." in output
    assert "Result: 5" in output


def test_invalid_second_number_recovers(monkeypatch, capsys):
    output = session(monkeypatch, capsys,
                     ["subtract", "10", "hello", "history", "subtract", "8", "3", "exit"])
    assert "Invalid number or result." in output
    assert "No calculations in history." in output
    assert "Result: 5" in output

# appended CLI tests from checkpoint 5B
def test_invalid_removal_number_preserves_history(monkeypatch, capsys):
    # Familiar loops exercise several boundary inputs without new test syntax.
    for invalid_number in ["0", "-1", "99"]:
        output = session(monkeypatch, capsys,
                         ["add", "1", "2", "remove", invalid_number, "history", "exit"])
        assert "Calculation does not exist." in output, invalid_number
        assert output.count("1. Add: 1, 2 = 3") == 2, invalid_number


def test_invalid_removal_text_preserves_history(monkeypatch, capsys):
    for invalid_text in ["hello", "1.5"]:
        output = session(monkeypatch, capsys,
                         ["add", "1", "2", "remove", invalid_text, "history", "exit"])
        assert "Please enter a whole calculation number." in output, invalid_text
        assert output.count("1. Add: 1, 2 = 3") == 2, invalid_text

# old cli test code below:

'''
def session(monkeypatch, capsys, answers):
    # iter is a cursor; next takes one response for each input prompt
    responses = iter(answers)

    def scripted_input(prompt):
        return next(responses)

    #pytest supplies these fictures and restores input after the test
    monkeypatch.setattr("builtins.input", scripted_input)
    run()
    return capsys.readouterr().out

def test_arithmetic_session(monkeypatch, capsys):
    output = session(monkeypatch, capsys,
                     ["add", "10", "5", "subtract", "20", "7", "exit"])
    assert "Result: 15" in output
    assert "Result: 13" in output
    assert output.endswith("Goodbye!\n")

def test_history_and_removal(monkeypatch, capsys):
    output = session(monkeypatch, capsys,
                     ["add", "10", "5", "subtract", "20", "7", "history", "remove", "1", "history", "exit"])
    assert "1. Add: 10, 5 = 15" in output
    assert "2. Subtract: 20, 7 = 13" in output
    assert "Removed: Add: 10, 5 = 15" in output
    assert output.endswith("1. Subtract: 20, 7 = 13\nGoodbye!\n")

def test_empty_history(monkeypatch, capsys):
    output = session(monkeypatch, capsys, ["history", "remove", "exit"])
    assert output.count("No calculations in history.") == 2

def test_help_and_unknown_command(monkeypatch, capsys):
    output = session(monkeypatch, capsys, ["HELP", "pizza", "EXIT"])
    assert "Commands:" in output
    assert "Unknown command." in output
    assert output.endswith("Goodbye!\n")

def test_independent_scripted_session(monkeypatch, capsys):
    # independent test requirement
    # tests mixed-case padded command with novel operands !
    output = session(monkeypatch, capsys, ["  aDd   ", "100", "25", "exit"])
    assert "Result: 125" in output
    assert output.endswith("Goodbye!\n")
'''