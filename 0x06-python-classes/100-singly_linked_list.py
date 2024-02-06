#!/usr/bin/python3
"""Module to define Node and SinglyLinkedList classes."""


class Node:
    """Class that defines a node
    Attributes:
        __size(int): the zise of the side of the square
    """
    def __init__(self, data, next_node=None):
        """Initialize a new Square
        Args:
            data (int): node's data
            next_node (Node): next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter for the data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter for the data"""
        self.__data = value
        if not isinstance(self.__data, int):
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """getter for the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter for the next node"""
        self.__next_node = value
        if not (isinstance(value, Node) or value is None):
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """Representation of a singly linked list"""
    def __init__(self):
        """initialize a singlylinkedlist"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert the node into the correct position
        depending on its data value.

            Args:
                value (Node): the node to be inserted.

            """
        new_node = Node(value)
        if not self.__head or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            curr = self.__head
            while curr.next_node and curr.next_node.data < value:
                curr = curr.next_node
            new_node.next_node = curr.next_node
            curr.next_node = new_node

    def __str__(self):
        """printing for singlylist representation"""
        vals = []
        curr = self.__head
        while curr is not None:
            vals.append(str(curr.data))
            curr = curr.next_node
        return ('\n'.join(vals))
