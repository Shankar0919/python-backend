def is_boolean(value: str) -> bool:
    return str(value).lower() in ["true", "false", "1", "0"]
