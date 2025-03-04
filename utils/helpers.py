# utils/helpers.py
# This module contains utility functions for the system. Why Use helpers.py?
# Reduces Redundancy → Instead of rewriting validation logic in multiple places, we reuse helper functions.
# Improves Readability → Code is cleaner, easier to understand, and maintain.
# Enhances Maintainability → If validation rules change, we only update them in one place (helpers.py). 

def validate_positive_number(value, value_name="Value"):
    """
    Ensures a given number is positive.
    :param value: The number to validate.
    :param value_name: The name of the value for error messages.
    :return: The validated positive number.
    """
    if value <= 0:
        raise ValueError(f"❌ {value_name} must be greater than zero.")
    return value

def validate_non_negative_number(value, value_name="Value"):
    """
    Ensures a given number is non-negative.
    :param value: The number to validate.
    :param value_name: The name of the value for error messages.
    :return: The validated non-negative number.
    """
    if value < 0:
        raise ValueError(f"❌ {value_name} cannot be negative.")
    return value
