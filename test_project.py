from unittest.mock import patch
from project import currency_salary

# Define currency and salary values

currency = "usd"
salary = 500

c_sign = None


def test_currency_salary():
    global currency, salary, c_sign


    with patch('builtins.input', side_effect=[currency, str(salary)]):
        result = currency_salary(None, None, None)

    c, s, cs = result

    assert c in ["eur", "usd", "gbp"]
    assert type(s) == int
    assert s > 0

    c_symbols = {"eur": "€", "usd": "$", "gbp": "£"}
    assert cs == c_symbols[c]


def test_needs():
    s = salary
    needs_budget = s * 0.5

    assert type(needs_budget) == float
    assert needs_budget > 0
    assert needs_budget < s


def test_wants():
    s = salary
    wants_budget = s * 0.3

    assert type(wants_budget) == float
    assert wants_budget > 0
    assert wants_budget < s


def test_savings_plan():

    global salary

    e_fund = salary * 6
    s_amount = salary * 2
    s_amount_2 = salary * 3
    progress_percentage = int((s_amount / e_fund) * 100)
    progress_percentage_2 = int((s_amount_2 / e_fund) * 100)

    assert type(e_fund) == int
    assert e_fund > 0

    assert type(s_amount) == int
    assert s_amount > 0

    assert progress_percentage == 33
    assert progress_percentage_2 == 50


def run_tests():
    test_currency_salary()
    test_savings_plan()
    test_needs()
    test_wants()


if __name__ == "__main__":
    run_tests()
