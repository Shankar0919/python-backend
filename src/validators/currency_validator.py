import re
def is_valid_currency(value: str) -> bool:
    return bool(re.match(r"^\d+(\.\d{1,2})?$", value))
