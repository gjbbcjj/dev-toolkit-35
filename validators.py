import re

def validate_integer(value):
    """Validate if the input is a valid integer."""
    try:
        int_value = int(value)
        return int_value
    except ValueError:
        raise ValueError(f'Invalid integer value: {value}')


def validate_email(value):
    """Validate if the input is a valid email address."""
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, value):
        raise ValueError(f'Invalid email address: {value}')
    return value


def validate_positive_float(value):
    """Validate if the input is a valid positive float."""
    try:
        float_value = float(value)
        if float_value < 0:
            raise ValueError(f'Value must be positive: {value}')
        return float_value
    except ValueError:
        raise ValueError(f'Invalid positive float value: {value}')