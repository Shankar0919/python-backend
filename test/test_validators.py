from src.validators.boolean_validator import is_boolean
from src.validators.date_validator import is_valid_date
from src.validators.time_validator import is_valid_time
from src.validators.currency_validator import is_valid_currency

def test_boolean_validator():
    assert is_boolean("true")
    assert not is_boolean("maybe")

def test_date_validator():
    assert is_valid_date("2020-01-01")
    assert not is_valid_date("2020-13-40")

def test_time_validator():
    assert is_valid_time("12:30:45")
    assert not is_valid_time("25:99:00")

def test_currency_validator():
    assert is_valid_currency("12.34")
    assert not is_valid_currency("12.3456")
