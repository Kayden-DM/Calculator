## Calculator
A command-line calculator written in Python. It uses the operator module to map symbols to functions and repeatedly evaluates expressions typed in number operator number form until the user quits.

## Features
Four Operations — Supports addition, subtraction, multiplication, and division via a dictionary of operator functions.

Expression Parsing — Splits input into two numbers and an operator with expr.split().

Float Support — Converts both operands with float(), so decimals work.

Division by Zero Handling — Catches ZeroDivisionError and prints a clear message.

General Error Handling — Catches malformed input and reminds the user of the correct format.

Quit Command — Type quit to exit the loop cleanly.

Repeat Loop — Keeps accepting calculations until the user quits.

## Technologies Used
| Technology | Purpose |
|---|---|
| Python | Application logic |
| `operator` | Provides `add`, `sub`, `mul`, `truediv` functions |
| `dict` (`ops`) | Maps symbols to operator functions |
| `expr.split()` | Separates the numbers and operator |
| `float()` | Parses numeric operands |
| `try / except` | Handles division by zero and invalid input |
| `while True` loop | Keeps the calculator running |
<!-- -->
## How to Use It
Install Python 3.6 or newer from python.org and make sure it's added to your PATH.

Save the code as calculator.py.

Open a terminal in the folder containing the file.

Run python calculator.py.

Type a calculation like 5 + 3 or 10 / 4 with spaces between the parts, and type quit to exit.

## Improvements
Catch invalid operators — an unknown symbol like 5 ^ 3 raises a KeyError, which is swallowed by the general except and reported as a formatting error; checking if op not in ops first would give a clearer message.

Format the result — results print as raw floats (e.g. 0.30000000000000004); rounding with round(result, 10) or formatting with f"{result:g}" would display cleaner numbers.
