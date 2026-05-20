# calculator/pkg/calculator.py

from typing import Optional
import math


class Calculator:
    """
    A calculator that evaluates infix mathematical expressions.

    Supports basic arithmetic operators (+, -, *, /, **, %)
    and mathematical functions (sqrt, abs, floor, ceil).

    Example:
        >>> calc = Calculator()
        >>> calc.evaluate("3 + 5")
        8.0
        >>> calc.evaluate("sqrt 16")
        4.0
    """

    OPERATORS: dict = {
        "+": (lambda a, b: a + b, 1),
        "-": (lambda a, b: a - b, 1),
        "*": (lambda a, b: a * b, 2),
        "/": (lambda a, b: a / b, 2),
        "%": (lambda a, b: a % b, 2),
        "**": (lambda a, b: a**b, 3),
    }

    UNARY_FUNCTIONS: dict = {
        "sqrt": math.sqrt,
        "abs": abs,
        "floor": math.floor,
        "ceil": math.ceil,
    }

    def evaluate(self, expression: str) -> Optional[float]:
        """
        Evaluate a mathematical expression string.

        Args:
            expression: A string representing a valid infix expression.

        Returns:
            The computed result as a float, or None for empty/blank expressions.

        Raises:
            ValueError: If the expression contains invalid tokens or is malformed.
            ZeroDivisionError: If the expression results in a division by zero.
        """
        if not expression or expression.isspace():
            return None

        tokens = expression.strip().split()
        return self._evaluate_infix(tokens)

    def _evaluate_infix(self, tokens: list[str]) -> float:
        """
        Evaluate a tokenised infix expression using the shunting-yard algorithm.

        Args:
            tokens: List of string tokens representing operands, operators, or functions.

        Returns:
            The computed result as a float.

        Raises:
            ValueError: If the expression is malformed.
            ZeroDivisionError: If division by zero is attempted.
        """
        values: list[float] = []
        operators: list[str] = []

        for token in tokens:
            if token in self.UNARY_FUNCTIONS:
                operators.append(token)

            elif token in self.OPERATORS:
                while (
                    operators
                    and operators[-1] in self.OPERATORS
                    and self.OPERATORS[operators[-1]][1] >= self.OPERATORS[token][1]
                ):
                    self._apply_operator(operators, values)
                operators.append(token)

            else:
                try:
                    values.append(float(token))
                except ValueError:
                    raise ValueError(
                        f"Invalid token '{token}'. "
                        "Expected a number, operator (+, -, *, /, **, %), "
                        "or function (sqrt, abs, floor, ceil)."
                    )

        while operators:
            self._apply_operator(operators, values)

        if len(values) != 1:
            raise ValueError(
                f"Malformed expression: expected a single result, "
                f"but got {len(values)} value(s) remaining."
            )

        return values[0]

    def _apply_operator(self, operators: list[str], values: list[float]) -> None:
        """
        Pop the top operator and apply it to the top value(s) on the value stack.

        Args:
            operators: The operator stack.
            values: The value stack.

        Raises:
            ValueError: If there are not enough operands for the operator.
            ZeroDivisionError: If division or modulo by zero is attempted.
        """
        if not operators:
            return

        operator = operators.pop()

        # Handle unary functions (single operand)
        if operator in self.UNARY_FUNCTIONS:
            if not values:
                raise ValueError(
                    f"Not enough operands for function '{operator}'."
                )
            a = values.pop()
            try:
                values.append(self.UNARY_FUNCTIONS[operator](a))
            except ValueError as e:
                raise ValueError(f"Math error in '{operator}({a})': {e}")
            return

        # Handle binary operators (two operands)
        if len(values) < 2:
            raise ValueError(
                f"Not enough operands for operator '{operator}'. "
                f"Expected 2, got {len(values)}."
            )

        b = values.pop()
        a = values.pop()

        if operator in ("/", "%") and b == 0:
            raise ZeroDivisionError(
                f"Division by zero: cannot evaluate '{a} {operator} 0'."
            )

        values.append(self.OPERATORS[operator][0](a, b))
