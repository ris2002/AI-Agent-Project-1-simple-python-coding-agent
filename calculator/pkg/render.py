# calculator/pkg/render.py

import json
from typing import Optional


def _clean_result(result: float) -> int | float:
    """
    Convert a whole-number float to an int for cleaner display.

    Args:
        result: The numeric result of an expression.

    Returns:
        An int if result is a whole number, otherwise the original float.
    """
    if isinstance(result, float) and result.is_integer():
        return int(result)
    return result


def format_json_output(
    expression: str,
    result: float,
    indent: int = 2,
    include_metadata: bool = False,
) -> str:
    """
    Format a calculator result as a pretty-printed JSON string.

    Args:
        expression:       The original expression string provided by the user.
        result:           The computed numeric result.
        indent:           Number of spaces used for JSON indentation (default: 2).
        include_metadata: When True, adds extra fields such as result type
                          and expression length to the output.

    Returns:
        A formatted JSON string ready to be printed or logged.

    Example:
        >>> format_json_output("3 + 5", 8.0)
        '{\\n  "expression": "3 + 5",\\n  "result": 8\\n}'
    """
    cleaned = _clean_result(result)

    output_data: dict = {
        "expression": expression,
        "result": cleaned,
    }

    if include_metadata:
        output_data["result_type"] = type(cleaned).__name__
        output_data["expression_length"] = len(expression)

    return json.dumps(output_data, indent=indent)
