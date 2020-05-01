"""
Test methods for deep copy
"""
import pytest

from deep_copy import Node


def assert_node_equal(n1, n2):
    """ Recurse through a tree and assert values are equal """
    # Assert that values are equal
    assert n1.value == n2.value

    # Assert that pointers are not equal
    assert n1 != n2

    # If either has a first child, both should have a first child
    if n1.first_child is not None or n2.first_child is not None:
        assert n1.first_child is not None and n2.first_child is not None
        assert assert_node_equal(n1.first_child, n2.first_child) is True

    # If either has a second child, both should have a second child
    if n1.second_child is not None or n2.second_child is not None:
        assert n1.second_child is not None and n2.second_child is not None
        assert assert_node_equal(n1.second_child, n2.second_child) is True

    return True


def test_shallow_copy():
    """Prove that just making a shallow reference fails deep copy """
    n1 = Node(value=1)
    n2 = n1
    with pytest.raises(AssertionError):
        assert_node_equal(n1, n2)


def test_deep_copy_no_children():
    """ Deep copy should with a single node"""
    n1 = Node(value=1)
    c1 = n1.deepCopy()
    assert_node_equal(n1, c1)


def test_deep_copy():
    """ Test deep copy on a more complicated tree """
    # Make a tree of mismatched leaf lengths
    root = Node(value=1)
    n1 = Node(value=2)
    n2 = Node(value=3)
    n1_1 = Node(value=4)

    # Link Nodes
    n1.first_child = n1_1
    root.first_child = n1
    root.second_child = n2

    # Copy the root
    root_copy = root.deepCopy()

    assert_node_equal(root, root_copy)
