"""
Tests for coin
"""

from coin import are_quarters_equivalent


def coin(type, year):
    return {"type": type, "year": year}


def test_empty_lists_are_equivalent():
    assert are_quarters_equivalent([], []) == True


def test_only_quarters_are_equivalent():
    assert (
        are_quarters_equivalent(
            [coin("quarter", 2019), coin("quarter", 2020)],
            [coin("quarter", 2019), coin("quarter", 2020)],
        )
        == True
    )


def test_different_order_is_unequal():
    assert (
        are_quarters_equivalent(
            [coin("quarter", 2020), coin("quarter", 2019)],
            [coin("quarter", 2019), coin("quarter", 2020)],
        )
        == False
    )


def test_only_nickels_are_equivalent():
    assert (
        are_quarters_equivalent(
            [{"type": "nickel", "year": 2019}], [{"type": "nickel", "year": 2019}]
        )
        == True
    )


def test_quarters_with_nickels_are_equivalent():
    assert (
        are_quarters_equivalent(
            [{"type": "nickel", "year": 2019}, {"type": "quarter", "year": 2020}],
            [
                {"type": "quarter", "year": 2020},
                {"type": "nickel", "year": 2020},
                {"type": "nickel", "year": 3000},
            ],
        )
        == True
    )


def test_empty_and_nickels_are_equivalent():
    assert are_quarters_equivalent([{"type": "nickel", "year": 2019}], []) == True
