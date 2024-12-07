#!/usr/bin/python3

"""This module defines class Node and class SinglyLinkedList"""


class Node():
    """Defines class Node"""

    def __init__(self, data, next_node=None):
        """Initializes class Node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """returns data"""

        return self.__data

    @data.setter
    def data(self, value):
        """sets the value of data"""

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """returns next_node"""

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """sets next_node"""

        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList():
    """Defines class SinglyLinkedList"""

    def __init__(self):
        """initializes the linked list"""

        self.__head = None

    def sorted_insert(self, value):
        """Inserts the node at the correct order"""

        new_node = Node(value)

        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while (current.next_node is not None and
                   current.next_node.data < value):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """string representation of the SinglyLinkedList"""

        result = []
        current = self.__head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)
