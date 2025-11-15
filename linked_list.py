class Node:
    """
    A Node class to store integer data and a reference to the next node.
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    A singly linked list that holds Node objects and performs operations using recursion.
    """

    def __init__(self):

        self.head = None

    def insert_at_front(self, data):
        """
        TODO:
        - Create a new Node with 'data'.
        - Insert it at the front of the list (head).
        - Update 'head' to the new node.
        """
        pass

    def insert_at_end(self, data):
        """
        (Optional) TODO:
        - Create a new Node with 'data'.
        - Traverse to the end of the list.
        - Set the last node's 'next' reference to the new node.
        """
        pass

    def recursive_sum(self):
        """
        TODO:
        - Use recursion to sum all node data in the list.
        - Consider a helper function that:
          1. Checks if the current node is None, and returns 0 if so.
          2. Otherwise, returns node.data + recursive call on node.next.
        - Return the total sum.
        """
        pass

    def recursive_reverse(self):
        """
        TODO:
        - Reverse the list in-place using recursion.
        - Possible approach:
          1. Use a helper function that accepts 'prev' and 'current'.
          2. Base case: if current is None, return 'prev' (new head).
          3. Otherwise, swap pointers and recurse.
        - Update 'head' to the returned new head.
        """
        pass

    def recursive_search(self, target):
        """
        TODO:
        - Return True if 'target' is found, otherwise False, using recursion.
        - Consider a helper function that:
          1. Returns False if the current node is None.
          2. Returns True if current node's data == target.
          3. Otherwise, recurse on the next node.
        """
        pass

    def display(self):
        """
        TODO:
        - Print the contents of the list for debugging.
        - Traverse from 'head' and collect each node's data.
        - Format output as 'val -> val -> val -> None' or similar.
        """
        pass
