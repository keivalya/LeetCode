class DoublyLinkedList:
    def __init__(self, value):
        """
        Initialize the doubly linked list with a single node.
        Sets both head and tail to the initial node and length to 1.
        """
        self.head = {"value": value, "next": None, "prev": None}
        self.tail = self.head
        self.length = 1

    def append(self, value):
        """
        Add a new node with the given value to the end of the list.
        Updates the tail and maintains bidirectional links.
        """
        new_node = {"value": value, "next": None, "prev": None}
        new_node["prev"] = self.tail
        self.tail["next"] = new_node
        self.tail = new_node
        self.length += 1
        return self

    def prepend(self, value):
        """
        Add a new node with the given value to the beginning of the list.
        Updates the head and maintains bidirectional links.
        """
        new_node = {"value": value, "next": None, "prev": None}
        new_node["next"] = self.head
        self.head["prev"] = new_node
        self.head = new_node
        self.length += 1
        return self

    def insert(self, idx, value):
        """
        Insert a new node with the given value at the specified index.
        Adjusts the surrounding nodes' next and prev pointers accordingly.
        """
        new_node = {"value": value, "next": None, "prev": None}
        leader = self.traverse_to_idx(idx - 1)
        follower = leader["next"]
        leader["next"] = new_node
        new_node["prev"] = leader
        new_node["next"] = follower
        follower["prev"] = new_node
        self.length += 1
        return self

    def remove(self, idx):
        """
        Remove the node at the specified index.
        Bypasses the node by linking its previous and next nodes together.
        """
        leader = self.traverse_to_idx(idx - 1)
        follower = leader["next"]["next"]
        leader["next"] = follower
        follower["prev"] = leader
        self.length -= 1
        return self

    def traverse_to_idx(self, idx):
        """
        Return the node located at the specified index by traversing from head.
        """
        counter = 0
        curr = self.head
        while counter != idx:
            curr = curr["next"]
            counter += 1
        return curr

    def print_forward(self):
        """
        Print the values in the list from head to tail.
        """
        curr = self.head
        while curr:
            print(curr["value"], end=" -> ")
            curr = curr["next"]
        print("None")

    def print_backward(self):
        """
        Print the values in the list from tail to head.
        """
        curr = self.tail
        while curr:
            print(curr["value"], end=" <- ")
            curr = curr["prev"]
        print("None")


my_linkedlist = DoublyLinkedList(10)

# append
my_linkedlist.append(5)
my_linkedlist.append(16)

# prepend
my_linkedlist.prepend(0)

# insert
my_linkedlist.insert(2, 55)

# remove
my_linkedlist.remove(3)

# print forward
my_linkedlist.print_forward()


# ------------------------------------------
# Documentation: What is a Doubly Linked List?
#
# A Doubly Linked List (DLL) is a linear data structure made up of nodes.
# Each node contains:
#   - value: The data it holds.
#   - next: A pointer to the next node.
#   - prev: A pointer to the previous node.
#
# Benefits of DLL:
#   - Traversal in both directions (forward and backward).
#   - Efficient insertion and removal from both ends.
#
# In this implementation, each node is represented as a dictionary
# for simplicity instead of a dedicated Node class.
# ------------------------------------------
