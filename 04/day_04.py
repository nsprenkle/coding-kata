# Password checker for several criteria
def matches_password_criteria(password):
    password = str(password)

    # two adjacent digits are the same
    adjacent_digits = False
    numbers_increasing = True

    prev_digit = None

    for digit in password:
        # password must contain an adjacent repeated digit
        if digit == prev_digit:
            adjacent_digits = True

        # numbers must only increase from left to right
        if digit < prev_digit:
            return False

        prev_digit = digit

    return adjacent_digits & numbers_increasing


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
