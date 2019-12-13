import day_04


def test_matches_password_criteria():
    assert day_04.matches_password_criteria(112233)
    assert not day_04.matches_password_criteria(123444)
    assert day_04.matches_password_criteria(111122)
    assert not day_04.matches_password_criteria(223450)
    assert not day_04.matches_password_criteria(123456)
