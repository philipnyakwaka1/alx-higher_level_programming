#!/usr/bin/python3
"""Class Node"""

class Node:
    def __init__(self, data, next_node=None):
        """initialize"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """get data"""
        return self.__data
    
    @data.setter
    def data(self, value):
        """set data"""
        if type(value) != int:
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """get next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self,value):
        """set next_node"""
        if value is not None and not isinstance(value, Node):
            raise TypeError('next_node must be a Node object')
        self.__next_node = value

class SinglyLinkedList:
    """class SinglyLinkedList"""
    def __init__(self):
        self.__head = None
    
    def __str__(self):
        """print singly linked list"""
        result = []
        current = self.__head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        """insert new node"""
        node = Node(value)
        if self.__head is None or node.data < self.__head.data:
            node.next_node = self.__head
            self.__head = node
        elif self.__head.next_node is None and node.data >= self.__head.data:
            self.__head.next_node = node
        else:
            current = self.__head
            while current.next_node:
                if node.data >= current.data and node.data < current.next_node.data:
                    node.next_node = current.next_node
                    current.next_node = node
                    break
                current = current.next_node
            if current and current.next_node is None:
                current.next_node = node