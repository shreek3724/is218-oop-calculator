Replaced README content with stage 6 requirements

# Object-Oriented Command-Line Calculator

This project is a calculator with add, subtract, history, remove, help, and exit functions created by using object oriented programming concepts. This includes encapsulation, inheritance, abstraction, and polymorphism, completed with CLI interface, and 100% test coverage, with all tests passing, and continuous integration (CI)

## Required Features & Supported Commands
Section is formatted as feature/command name --> description

add --> adds two numbers together
subtract --> subtracts two numbers, the second from the first
history --> displays all valid past calculations
remove --> removes the calculation of user-inputted index from the history
help --> shows all valid and available commands with descriptions
exit --> closes the calculator 

## Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git](https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git)
   cd YOUR-REPOSITORY
   ```

2. **Create and activate virtual environment, install dependencies**
```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
```

3. **Start the application**
```bash
    python -m calculator
```

4. **Run tests and check coverage**
```bash
    python -m pytest
 ```

## Reflect and Transfer 

1. **Where would Multiply belong? Include changes to registration, help, and tests; explain why History needs no multiplication logic.**
To include multiply, you would first create a "Multiply" class that inherits from Calculation in calculation/calculation.py, and implement get_result() as self.a*self.b
You would then go to calculator.cli.py, and register "multiply" in the operations dictionary
You would also update the HELP command to include multiply.
And lastly you would add its applicable unit tests to tests/test_calculation.py and tests/test_cli.py
History would not need to be changed because it stores and retries the generic Calculation objects, disregarding the specific subclass of the object, meaning adding new operations does not necessitate an update to the History module.

2. **What contract could email and text-message notification objects share through send()?**
A potential contract email and text-message notification objects could share through send() would be a an abtract Notification class, including send(self, message: str).

3. **What design knowledge transfers to another language, and what syntax or runtime rules would you still need to learn?**
Some transferable concepts to other languages include abstract data types, polymorphism, encapsulation, single responsibility principle, and open/closed responsibility principle.
In terms of language-specific rules, memory management rules, static and dynamic syntax, as well as access modifiers may need to be learned.