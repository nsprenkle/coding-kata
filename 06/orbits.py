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


def main():
    orbits = injest('input.txt')
    tree = build_tree(orbits)

    checksum = count_orbits(tree, "COM")
    print('Checksum: {}'.format(checksum))


if __name__ == "__main__":
    main()
