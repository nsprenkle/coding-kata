# Password checker for several criteria
def matches_password_criteria(password):
    password = str(password)

    # two adjacent digits are the same
    adjacent_pair = False
    numbers_increasing = True

    prev_digit = None
    number_count = 0

    for digit in password:
        # password must contain an adjacent pair of digits
        if digit == prev_digit:
            if number_count == 0:
                number_count = 2
            else:
                number_count += 1
        else:
            if number_count == 2:
                adjacent_pair = True
            number_count = 0

        # numbers must only increase from left to right
        if digit < prev_digit:
            print('Password not strictly increasing, {}'.format(password))
            return False

        prev_digit = digit

    print('Password {} a pair {}'.format(
        'contains' if adjacent_pair else 'does not contain', password))
    adjacent_pair = adjacent_pair or number_count == 2

    return adjacent_pair and numbers_increasing


def main(min, max):
    """ run password check criteria for numbers in range """
    matches = 0

    for password in range(min, max):
        if matches_password_criteria(password):
            matches += 1

    print('Matches: {}'.format(matches))

    return matches


if __name__ == "__main__":
    main(123257, 647015)
