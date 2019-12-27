import amps


def test_amps():
    intcode = [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0]
    phase_sequence = [4, 3, 2, 1, 0]

    assert amps.run(intcode, phase_sequence) == 43210

    intcode = [3, 23, 3, 24, 1002, 24, 10, 24, 1002, 23, -1,
               23, 101, 5, 23, 23, 1, 24, 23, 23, 4, 23, 99, 0, 0]
    phase_sequence = [0, 1, 2, 3, 4]

    assert amps.run(intcode, phase_sequence) == 54321

    intcode = [3, 31, 3, 32, 1002, 32, 10, 32, 1001, 31, -2, 31, 1007, 31, 0,
               33, 1002, 33, 7, 33, 1, 33, 31, 31, 1, 32, 31, 31, 4, 31, 99, 0, 0, 0]
    phase_sequence = [1, 0, 4, 3, 2]

    assert amps.run(intcode, phase_sequence) == 65210


def test_find_max_signal():
    intcode = [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0]

    (max_val, sequence) = amps.find_max_signal(intcode)
    assert max_val == 43210
    assert sequence == [4, 3, 2, 1, 0]

    intcode = [3, 23, 3, 24, 1002, 24, 10, 24, 1002, 23, -1,
               23, 101, 5, 23, 23, 1, 24, 23, 23, 4, 23, 99, 0, 0]

    (max_val, sequence) = amps.find_max_signal(intcode)
    assert max_val == 54321
    assert sequence == [0, 1, 2, 3, 4]

    intcode = [3, 31, 3, 32, 1002, 32, 10, 32, 1001, 31, -2, 31, 1007, 31, 0,
               33, 1002, 33, 7, 33, 1, 33, 31, 31, 1, 32, 31, 31, 4, 31, 99, 0, 0, 0]

    (max_val, sequence) = amps.find_max_signal(intcode)
    assert max_val == 65210
    assert sequence == [1, 0, 4, 3, 2]
