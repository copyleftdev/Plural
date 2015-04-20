

def is_leap(year):
    return is_typical_leap_year(year) and not is_atypical_common_year(year)

def is_atypical_common_year(year):
    return year % 100 == 0 and not year % 400 == 0

def is_typical_leap_year(year):
    return year % 4 == 0


def test_normal_leap_year():
    assert is_leap(1996)

def test_normal_common_year():
    assert not is_leap(2001)

def test_atypical_common_year():
    assert not is_leap(1900)

def test_atypical_leap_year():
    assert is_leap(2000)
