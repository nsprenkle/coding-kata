def calc_path_coordinates(legs):
    """ determine a coordinate set for a path """
    path_coordinates = []

    x = 0
    y = 0

    for leg in legs:
        # first char is direction, the remainder are magnitude
        direction = leg[0].upper()
        magnitude = int(leg[1:])

        for _ in range(0, magnitude):
            if direction == 'R':
                x += 1
            elif direction == 'L':
                x -= 1
            elif direction == 'U':
                y += 1
            elif direction == 'D':
                y -= 1
            else:
                raise Exception('bad direction')

            path_coordinates.append((x, y))

    return path_coordinates


def main(path1=None, path2=None, file=None):
    # read from file
    if file is not None:
        path1, path2 = read_file(file)

    # get path coordinates
    coordinates1 = calc_path_coordinates(path1)
    coordinates2 = calc_path_coordinates(path2)

    # find intersection points
    intersections = list(filter(lambda x: x in coordinates1, coordinates2))

    path_distances = []

    # find path distances to intersection points
    for intersection in intersections:
        path_distances.append(coordinates1.index(
            intersection) + coordinates2.index(intersection))

    # return minimum steps + 2 offset, one for each wire
    return min(path_distances) + 2


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
