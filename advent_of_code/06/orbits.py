import anytree


def injest(file):
    """ read input as an array of tuples """
    file_handler = open(file)

    raw_orbits = file_handler.readlines()
    orbits = []

    for orbit in raw_orbits:
        (a, b) = orbit.strip().split(')')
        orbits.append((a, b))

    return orbits


def build_tree(orbits):
    """ build a dictionary representing orbits """
    orbital_tree = {}

    for orbit in orbits:
        # create the dict entry if it doesn't exist
        if orbit[0] not in orbital_tree:
            orbital_tree[orbit[0]] = []

        # append to the list of orbiting bodies
        orbital_tree[orbit[0]].append(orbit[1])

    return orbital_tree


def count_orbits(tree, node, depth=0):
    """ count direct and inderect orbits from tree traversal """

    orbit_count = depth

    # exit if an end orbit is found
    if node not in tree:
        return orbit_count

    for orbit in tree[node]:
        orbit_count += count_orbits(tree, orbit, depth + 1)

    return orbit_count


def path_to(orbital_tree, node, destination, current_path=[]):

    # if we've reached our destination, return the path, less the destination node
    if node == destination:
        current_path.pop()
        print('Path found to {}: {}'.format(destination, current_path))
        return current_path

    # traverse the orbital tree
    if node in orbital_tree:

        for orbit in orbital_tree[node]:
            path = path_to(orbital_tree, orbit,
                           destination, current_path + [orbit])

            if path:
                return path


def orbital_transfers(orbital_tree, start, destination, com='COM'):
    path_1 = path_to(orbital_tree, com, start)
    path_2 = path_to(orbital_tree, com, destination)

    # find orbits unique to a/b
    transfers = set(path_1) ^ set(path_2)

    return len(transfers)


def main():
    orbits = injest('input.txt')
    tree = build_tree(orbits)

    # Part 01
    # checksum = count_orbits(tree, "COM")
    # print('Checksum: {}'.format(checksum))

    # Part 02
    print('Transfers: {}'.format(orbital_transfers(tree, 'YOU', 'SAN')))


if __name__ == "__main__":
    main()
