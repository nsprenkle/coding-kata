def calc_path_coordinates(legs):
    """ determine a coordinate set for a path """
    coordinate_set = set()

    x = 0
    y = 0

    for leg in legs:
        # first char is direction, the remainder are magnitude
        direction = leg[0].upper()
        magnitude = int(leg[1:])

        if direction == 'R':
            for step in range(0, magnitude):
                x += 1
                coordinate_set.add((x, y))
        elif direction == 'L':
            for step in range(0, magnitude):
                x -= 1
                coordinate_set.add((x, y))
        elif direction == 'U':
            for step in range(0, magnitude):
                y += 1
                coordinate_set.add((x, y))
        elif direction == 'D':
            for step in range(0, magnitude):
                y -= 1
                coordinate_set.add((x, y))
        else:
            raise Exception('bad direction')

    return coordinate_set


def main(path1=None, path2=None, file=None):
    # read from file
    if file is not None:
        path1, path2 = read_file(file)

    # get path coordinates
    coordinates1 = calc_path_coordinates(path1)
    coordinates2 = calc_path_coordinates(path2)

    # find intersection points
    intersections = coordinates1.intersection(coordinates2)

    manhattan_distances = []

    # find Manhattan distances
    for intersection in intersections:
        manhattan_distances.append(abs(intersection[0]) + abs(intersection[1]))

    # return minimum manhattan distance
    return min(manhattan_distances)


def read_file(file):
    """read comma separated paths from a file, one per line, return paths as a tuple of arrays"""
    fileHandler = open(file)
    path1 = fileHandler.readline().strip().split(',')
    path2 = fileHandler.readline().strip().split(',')
    fileHandler.close()

    return (path1, path2)


if __name__ == "__main__":
    file = 'input.txt'
    print('Minimum distance {}'.format(main(file=file)))
