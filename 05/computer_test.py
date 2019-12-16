import computer


def test_run_program():
    assert computer.run([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
    assert computer.run([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
    assert computer.run([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]
    assert computer.run([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [
        30, 1, 1, 4, 2, 5, 6, 0, 99]

    # day 05
    assert computer.run([1002, 4, 3, 4, 33]) == [1002, 4, 3, 4, 99]
    assert computer.run([1101, 100, -1, 4, 0]) == [1101, 100, -1, 4, 99]
