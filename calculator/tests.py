# calculator/tests.py

import unittest
from pkg.calculator import Calculator
from pkg.render import format_json_output, _clean_result
import json
import math


class TestBasicArithmetic(unittest.TestCase):
    """Tests for the four fundamental arithmetic operations."""

    def setUp(self):
        self.calc = Calculator()

    def test_addition(self):
        self.assertEqual(self.calc.evaluate("3 + 5"), 8)

    def test_subtraction(self):
        self.assertEqual(self.calc.evaluate("10 - 4"), 6)

    def test_multiplication(self):
        self.assertEqual(self.calc.evaluate("3 * 4"), 12)

    def test_division(self):
        self.assertEqual(self.calc.evaluate("10 / 2"), 5)

    def test_addition_with_floats(self):
        self.assertAlmostEqual(self.calc.evaluate("1.5 + 2.5"), 4.0)

    def test_subtraction_with_floats(self):
        self.assertAlmostEqual(self.calc.evaluate("5.5 - 2.2"), 3.3)

    def test_negative_result(self):
        self.assertEqual(self.calc.evaluate("3 - 10"), -7)


class TestAdvancedOperators(unittest.TestCase):
    """Tests for extended operators: exponentiation and modulo."""

    def setUp(self):
        self.calc = Calculator()

    def test_exponentiation(self):
        self.assertEqual(self.calc.evaluate("2 ** 8"), 256)

    def test_exponentiation_with_zero(self):
        self.assertEqual(self.calc.evaluate("5 ** 0"), 1)

    def test_modulo(self):
        self.assertEqual(self.calc.evaluate("10 % 3"), 1)

    def test_modulo_exact(self):
        self.assertEqual(self.calc.evaluate("9 % 3"), 0)


class TestUnaryFunctions(unittest.TestCase):
    """Tests for built-in unary math functions."""

    def setUp(self):
        self.calc = Calculator()

    def test_sqrt(self):
        self.assertAlmostEqual(self.calc.evaluate("sqrt 16"), 4.0)

    def test_sqrt_non_perfect(self):
        self.assertAlmostEqual(self.calc.evaluate("sqrt 2"), math.sqrt(2))

    def test_abs_negative(self):
        self.assertEqual(self.calc.evaluate("abs -9"), 9)

    def test_abs_positive(self):
        self.assertEqual(self.calc.evaluate("abs 7"), 7)

    def test_floor(self):
        self.assertEqual(self.calc.evaluate("floor 3.9"), 3)

    def test_ceil(self):
        self.assertEqual(self.calc.evaluate("ceil 3.1"), 4)

    def test_sqrt_negative_raises(self):
        with self.assertRaises(ValueError):
            self.calc.evaluate("sqrt -4")


class TestOperatorPrecedence(unittest.TestCase):
    """Tests ensuring operator precedence is correctly applied."""

    def setUp(self):
        self.calc = Calculator()

    def test_multiplication_before_addition(self):
        self.assertEqual(self.calc.evaluate("3 * 4 + 5"), 17)

    def test_division_before_subtraction(self):
        self.assertEqual(self.calc.evaluate("10 - 8 / 2"), 6)

    def test_complex_expression(self):
        self.assertEqual(self.calc.evaluate("2 * 3 - 8 / 2 + 5"), 7)

    def test_exponentiation_precedence(self):
        # 2 ** 3 = 8, then 8 * 2 = 16
        self.assertEqual(self.calc.evaluate("2 ** 3 * 2"), 16)

    def test_mixed_all_operators(self):
        # Precedence: ** (3) > *, % (2) > + (1)
        # Step-by-step: 2 ** 2 = 4 → 4 * 10 = 40 → 40 % 3 = 1 → 5 + 1 = 6
        self.assertEqual(self.calc.evaluate("5 + 2 ** 2 * 10 % 3"), 6)


class TestEdgeCases(unittest.TestCase):
    """Tests for boundary conditions and edge cases."""

    def setUp(self):
        self.calc = Calculator()

    def test_empty_expression(self):
        self.assertIsNone(self.calc.evaluate(""))

    def test_whitespace_only_expression(self):
        self.assertIsNone(self.calc.evaluate("   "))

    def test_single_number(self):
        self.assertEqual(self.calc.evaluate("42"), 42)

    def test_single_float(self):
        self.assertAlmostEqual(self.calc.evaluate("3.14"), 3.14)

    def test_large_numbers(self):
        self.assertEqual(self.calc.evaluate("1000000 * 1000000"), 1_000_000_000_000)


class TestErrorHandling(unittest.TestCase):
    """Tests that confirm proper errors are raised for invalid input."""

    def setUp(self):
        self.calc = Calculator()

    def test_invalid_operator(self):
        with self.assertRaises(ValueError):
            self.calc.evaluate("$ 3 5")

    def test_invalid_token(self):
        with self.assertRaises(ValueError):
            self.calc.evaluate("3 + abc")

    def test_not_enough_operands(self):
        with self.assertRaises(ValueError):
            self.calc.evaluate("+ 3")

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.evaluate("10 / 0")

    def test_modulo_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.evaluate("10 % 0")


class TestRender(unittest.TestCase):
    """Tests for the JSON output rendering module."""

    def test_integer_result_displayed_as_int(self):
        output = json.loads(format_json_output("3 + 5", 8.0))
        self.assertEqual(output["result"], 8)
        self.assertIsInstance(output["result"], int)

    def test_float_result_preserved(self):
        output = json.loads(format_json_output("1 / 3", 1 / 3))
        self.assertAlmostEqual(output["result"], 1 / 3)

    def test_expression_preserved(self):
        output = json.loads(format_json_output("3 + 5", 8.0))
        self.assertEqual(output["expression"], "3 + 5")

    def test_metadata_included(self):
        output = json.loads(
            format_json_output("3 + 5", 8.0, include_metadata=True)
        )
        self.assertIn("result_type", output)
        self.assertIn("expression_length", output)
        self.assertEqual(output["result_type"], "int")
        self.assertEqual(output["expression_length"], len("3 + 5"))

    def test_metadata_excluded_by_default(self):
        output = json.loads(format_json_output("3 + 5", 8.0))
        self.assertNotIn("result_type", output)
        self.assertNotIn("expression_length", output)

    def test_custom_indent(self):
        output = format_json_output("1 + 1", 2.0, indent=4)
        self.assertIn("    ", output)

    def test_clean_result_whole_float(self):
        self.assertIsInstance(_clean_result(4.0), int)

    def test_clean_result_fractional_float(self):
        self.assertIsInstance(_clean_result(4.5), float)


if __name__ == "__main__":
    unittest.main(verbosity=2)
