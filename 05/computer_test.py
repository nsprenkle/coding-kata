import computer


def test_memory():
    # day 02
    mem = [1, 0, 0, 0, 99]
    computer.run(mem)
    assert mem == [2, 0, 0, 0, 99]

    mem = [2, 3, 0, 3, 99]
    computer.run(mem)
    assert mem == [2, 3, 0, 6, 99]

    mem = [2, 4, 4, 5, 99, 0]
    computer.run(mem)
    assert mem == [2, 4, 4, 5, 99, 9801]

    mem = [1, 1, 1, 4, 99, 5, 6, 0, 99]
    computer.run(mem)
    assert mem == [30, 1, 1, 4, 2, 5, 6, 0, 99]

    # day 05
    mem = [1002, 4, 3, 4, 33]
    computer.run(mem)
    assert mem == [1002, 4, 3, 4, 99]

    mem = [1101, 100, -1, 4, 0]
    computer.run(mem)
    assert mem == [1101, 100, -1, 4, 99]


def test_output():
    # day 05

    # test input == 8 (position mode)
    assert computer.run([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], input=8) == 1
    assert computer.run([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], input=0) == 0

    # test input == 8 (immediate mode)
    assert computer.run([3, 3, 1108, -1, 8, 3, 4, 3, 99], input=8) == 1
    assert computer.run([3, 3, 1108, -1, 8, 3, 4, 3, 99], input=0) == 0

    # test input < 8 (position mode)
    assert computer.run([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], input=7) == 1
    assert computer.run([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], input=9) == 0

    # test input < 8 (immediate mode)
    assert computer.run([3, 3, 1107, -1, 8, 3, 4, 3, 99], input=7) == 1
    assert computer.run([3, 3, 1107, -1, 8, 3, 4, 3, 99], input=9) == 0

    # test input != 0 (jumps & position mode)
    assert computer.run([3, 12, 6, 12, 15, 1, 13, 14, 13,
                         4, 13, 99, -1, 0, 1, 9], input=1337) == 1
    assert computer.run([3, 12, 6, 12, 15, 1, 13, 14, 13,
                         4, 13, 99, -1, 0, 1, 9], input=0) == 0

    # test input != 0 (jumps & immediate mode)
    assert computer.run([3, 3, 1105, -1, 9, 1101, 0, 0,
                         12, 4, 12, 99, 1], input=1337) == 1
    assert computer.run([3, 3, 1105, -1, 9, 1101, 0, 0,
                         12, 4, 12, 99, 1], input=0) == 0

    # a lengthy example... 999 if input < 8, 1000 if input == 8, 1001 if input > 8
    assert computer.run([3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
                         1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
                         999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99
                         ], input=7) == 999

    assert computer.run([3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
                         1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
                         999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99
                         ], input=8) == 1000

    assert computer.run([3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
                         1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
                         999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99
                         ], input=9) == 1001
