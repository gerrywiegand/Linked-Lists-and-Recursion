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

        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def recursive_sum(self):
        def helper(node):
            if node is None:
                return 0
            return node.data + helper(node.next)

        return helper(self.head)

    def recursive_reverse(self):
        def helper(prev, current):
            if current is None:
                return prev
            next_node = current.next
            current.next = prev
            return helper(current, next_node)

        self.head = helper(None, self.head)

    def recursive_search(self, target):

        def helper(node, target):
            if node is None or not target:
                return False
            if node.data == target:
                return True
            return helper(node.next, target)

        return helper(self.head, target)

    def display(self):
        current = self.head
        output = []
        while current.next:
            output.append(f"{current.data} ->")
            current = current.next
        output.append(str(current.data))
        print(output)
        """
        TODO:
        - Print the contents of the list for debugging.
        - Traverse from 'head' and collect each node's data.
        - Format output as 'val -> val -> val -> None' or similar.
        """
        pass


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_front(5)
    print("Sum of elements:", ll.recursive_sum())  # Output: 35
    ll.display()  # Expected Output: 5 -> 10 -> 20 -> None
    print("Search for 10:", ll.recursive_search(10))  # Output: True
    print("Search for 15:", ll.recursive_search(15))  # Output: False
    ll.recursive_reverse()
    ll.display()  # Expected Output: 20 -> 10 -> 5 -> None
