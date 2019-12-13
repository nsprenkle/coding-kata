import day_04


def test_matches_password_criteria():
    assert day_04.matches_password_criteria(111111)
    assert not day_04.matches_password_criteria(223450)
    assert not day_04.matches_password_criteria(123456)
    assert not day_04.matches_password_criteria(123789)
