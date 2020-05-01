"""
Given a structure:
    class Node
    {
        Node first_child;
        Node second_child;
        String value;
    }
write a deep-copy method.
"""


class Node(object):
    def __init__(self, first_child=None, second_child=None, value=None):
        self.first_child = first_child
        self.second_child = second_child
        self.value = value

    def deepCopy(self):
        """ Deep copies self and returns the new copy """
        new_first_child = None
        if self.first_child:
            new_first_child = self.first_child.deepCopy()

        new_second_child = None
        if self.second_child:
            new_second_child = self.second_child.deepCopy()

        new_node = Node(
            first_child=new_first_child, second_child=new_second_child, value=self.value
        )

        return new_node
