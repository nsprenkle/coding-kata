"""
Given two lists containing objects like the following:
Coin = {
    'type': 'quarter' or 'nickel',
    'year': 4 digit number
}

Write a method are_quarters_equivalent(coin_list_a, coin_list_b) verifying that both lists contain
the exact same quarters, in the same order, ignoring nickels.
"""


def next_quarter_in_list(list, start_index):
    """ Get the a tuple of next quarter in the list and index or None """
    for i in range(start_index, len(list)):
        if list[i]["type"] == "quarter":
            return list[i], i

    return None, None


def are_quarters_equivalent(coin_list_a, coin_list_b):
    coin_index_a = 0
    coin_index_b = 0

    while coin_index_a is not None and coin_index_b is not None:

        # Find next quarter location in each list
        coin_a, coin_index_a = next_quarter_in_list(coin_list_a, coin_index_a)
        coin_b, coin_index_b = next_quarter_in_list(coin_list_b, coin_index_b)

        # If both are None, we've reached the end of the list
        if coin_a is None and coin_b is None:
            return True

        # If both lists have a next quarter, compare them and iterate
        elif coin_a is not None and coin_b is not None:
            if coin_a["year"] == coin_b["year"]:
                coin_index_a += 1
                coin_index_b += 1
                continue
            else:
                return False

        # A mismatch means the lists have different numbers of quarters...
        # and are therefore not equivalent
        else:
            return False

    # Ensure we made a single compare or
    return True
