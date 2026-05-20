# calculator/main.py

import sys
from pkg.calculator import Calculator
from pkg.render import format_json_output

USAGE = """
Calculator App
==============
Usage:   python main.py "<expression>"

Operators  : +  -  *  /  %  **
Functions  : sqrt  abs  floor  ceil

Examples:
  python main.py "3 + 5"
  python main.py "10 / 2 - 3"
  python main.py "2 ** 8"
  python main.py "sqrt 144"
  python main.py "15 % 4"
"""


def main() -> None:
    """
    Entry point for the calculator CLI application.

    Reads an expression from command-line arguments, evaluates it,
    and prints the result as formatted JSON.
    """
    calculator = Calculator()

    if len(sys.argv) <= 1:
        print(USAGE)
        return

    expression = " ".join(sys.argv[1:])

    try:
        result = calculator.evaluate(expression)
        if result is None:
            print("Error: Expression is empty or contains only whitespace.")
            sys.exit(1)

        print(format_json_output(expression, result))

    except ZeroDivisionError as e:
        print(f"Math Error: {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"Input Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
