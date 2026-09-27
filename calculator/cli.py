from calculator.calculation import Add, Subtract, Calculation
from calculator.history import History

# new CLI code from checkpoint 5A

HELP = """Commands:
  add       Add two numbers
  subtract  Subtract the second number from the first
  history   Show this session's calculations
  remove    Remove a calculation by its displayed number
  help      Show available commands
  exit      Exit the calculator"""

def describe(calculation: Calculation) -> str:
    """Format an object through its common interface."""
    # :g formats numbers compactly. The class name is only a display label.
    return (
        f"{type(calculation).__name__}: "
        f"{calculation.a:g}, {calculation.b:g} = {calculation.get_result():g}"
    )

def show_history(history: History) -> None:
    calculations = history.get_history()
    if not calculations:
        print("No calculations in history.")
        return
    print("Calculation History\n")
    # enumerate gives us a display number alongside each calculation object.
    for number, calculation in enumerate(calculations, start=1):
        print(f"{number}. {describe(calculation)}")

def run() -> None:
    history = History()
    operations = {"add": Add, "subtract": Subtract}
    print('OOP Calculator\n\nType "help" for commands.')
    while True:
        # READ: the terminal gives us text; normalize commands for comparison.
        command = input("> ").strip().lower()
        if command == "exit":
            break
        if command in operations:
            # EVALUATE: invalid text is handled before history is changed.
            try:
                a = float(input("First number: "))
                b = float(input("Second number: "))
                operation_class = operations[command]
                calculation = operation_class(a, b)
            except ValueError:
                print("Invalid number or result. Please use finite numbers.")
                continue
            history.add(calculation)
            # PRINT: arithmetic remains the object's responsibility.
            print(f"Result: {calculation.get_result():g}")
        elif command == "history":
            show_history(history)
        elif command == "remove":
            show_history(history)
            if history.get_history():
                number = int(input("Enter calculation number to remove: "))
                # People count from 1; Python indexes start at 0.
                removed = history.remove(number - 1)
                print(f"Removed: {describe(removed)}")
        elif command == "help":
            print(HELP)
        else:
            print('Unknown command.\nType "help" for available commands.')
        # LOOP: reaching the end starts another iteration at the input prompt.
    print("Goodbye!")

'''
# CLI code from checkpoint 4B

HELP = """Commands:
  add       Add two numbers
  subtract  Subtract the second number from the first
  history   Show this session's calculations
  remove    Remove a calculation by its displayed number
  help      Show available commands
  exit      Exit the calculator"""

def describe(calculation: Calculation) -> str:
    # format an object through its common interface
    # :g formats numbers compactly. the class name is only a display label !
    return (
        f"{type(calculation).__name__}: "
        f"{calculation.a:g}, {calculation.b:g} = {calculation.get_result():g}"
    )

def show_history(history: History) -> None:
    calculations = history.get_history()
    if not calculations:
        print("No calculations in history.")
        return
    print("Calculation History!\n")
    # enumerate gives us a display number alongside each calculation object
    for number, calculation in enumerate(calculations, start=1):
        print(f"{number}. {describe(calculation)}")

def run() -> None:
    history = History()
    operations = {"add": Add, "subtract": Subtract}
    print('OOP Calculator\n\nType "help" for commands')
    while True:
        # the terminal gives us text; normalize commands for comparison!
        command = input("> ").strip().lower()
        if command == "exit":
            break
        if command in operations:
            # this stage assumes the user supplies valid numbers
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            operation_class = operations[command]
            calculation = operation_class(a, b)
            history.add(calculation)
            # print: arithmetric remains the object's respoonsibility
            print(f"Result: {calculation.get_result():g}")
        elif command == "history":
            show_history(history)
        elif command == "remove":
            show_history(history)
            if history.get_history():
                number = int(input("Enter the number of the calculation to remove: "))
                # people count from 1; python indexes start at 0
                removed = history.remove(number - 1)
                print(f"Removed: {describe(removed)}")
        elif command == "help":
            print(HELP)
        else:
            print("Unknown command.\nType 'help' for available commands.")
    print("Goodbye!")
'''
    
# old code for CLI from checkpoint 4A
'''
# checkpoint 4A: a small conversation before adding history commands

HELP = "Commands: add, subtract, help, exit"

def run():
    operations = {"add": Add, "subtract": Subtract}
    print('OOP Calculator\n\nType "help" for commands')

    while True:
        command = input("> ").strip().lower()
        if command == "exit":
            break
        if command in operations:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            operation_class = operations[command]
            calculation = operation_class(a,b)
            print(f"Result: {calculation.get_result():g}")
        elif command == "help":
            print(HELP)
        else:
            print("Unknown command.\nType 'help' for available commands.")
    print("Goodbye!")
'''