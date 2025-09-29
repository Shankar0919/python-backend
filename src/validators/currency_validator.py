import re


def is_valid_currency(value: str) -> bool:
    return bool(re.match(r'^[0-9]+(\.[0-9]{1,2})?$', str(value)))
