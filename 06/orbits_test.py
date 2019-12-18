from anytree import Node

import orbits


def test_injest():
    orbital_pairs = orbits.injest('input_test.txt')

    assert orbital_pairs is not None
    assert len(orbital_pairs) is 11
    assert orbital_pairs[0] == ('COM', 'B')


def test_bulid_tree():
    orbital_pairs = orbits.injest('input_test.txt')

    orbital_tree = orbits.build_tree(orbital_pairs)

    assert len(orbital_tree) is 8


def test_count_orbits():
    orbital_pairs = orbits.injest('input_test.txt')
    orbital_tree = orbits.build_tree(orbital_pairs)

    assert orbits.count_orbits(orbital_tree, 'COM') == 42


def test_path_to():
    orbital_pairs = orbits.injest('input_test_2.txt')
    orbital_tree = orbits.build_tree(orbital_pairs)

    print(orbital_tree)
    assert orbits.path_to(orbital_tree, 'COM', 'YOU') == [
        'B', 'C', 'D', 'E', 'J', 'K']
    assert orbits.path_to(orbital_tree, 'COM', 'SAN') == ['B', 'C', 'D', 'I']


def test_orbital_transfers():
    orbital_pairs = orbits.injest('input_test_2.txt')
    orbital_tree = orbits.build_tree(orbital_pairs)

    print(orbital_tree)

    assert orbits.orbital_transfers(orbital_tree, 'YOU', 'SAN') == 4
