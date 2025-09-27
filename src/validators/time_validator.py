from datetime import datetime

def is_valid_time(value: str) -> bool:
    try:
        datetime.strptime(value, "%H:%M:%S")
        return True
    except Exception:
        return False
