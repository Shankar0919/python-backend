from validators.boolean_validator import is_boolean
from validators.date_validator import is_valid_date
from validators.time_validator import is_valid_time
from validators.currency_validator import is_valid_currency


def test_boolean_validator():
    assert is_boolean("true")
    assert is_boolean("false")
    assert not is_boolean("maybe")


def test_date_validator():
    assert is_valid_date("2020-01-01")
    assert not is_valid_date("01-01-2020")


def test_time_validator():
    assert is_valid_time("12:30:45")
    assert not is_valid_time("99:99:99")


def test_currency_validator():
    assert is_valid_currency("100")
    assert is_valid_currency("100.50")
    assert not is_valid_currency("abc")
