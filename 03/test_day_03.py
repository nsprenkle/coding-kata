from day_03 import main, calc_path_coordinates


def test_all():
    # tests ([path1], [path2], expected_distance)
    test1 = (['R8', 'U5', 'L5', 'D3'], ['U7', 'R6', 'D4', 'L4'], 30)
    test2 = (['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'],
             ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83'], 610)
    test3 = (['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51'],
             ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7'], 410)

    tests = [test1, test2, test3]

    for test in tests:
        assert main(path1=test[0], path2=test[1]) == test[2]


def test_calc_path_coordinates():
    assert calc_path_coordinates(['R2']) == [(1, 0), (2, 0)]
    assert calc_path_coordinates(['R2', 'U2']) == [
        (1, 0), (2, 0), (2, 1), (2, 2)]
    assert calc_path_coordinates(['R1', 'L2', 'U1', 'D2']) == [
        (1, 0), (0, 0), (-1, 0), (-1, 1), (-1, 0), (-1, -1)]
