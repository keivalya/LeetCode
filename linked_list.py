class LinkedList:

    def __init__(self, value):
        """
        Initialize the linked list with the first node containing the given value.
        Sets both head and tail to this initial node and initializes the length to 1.
        """
        self.head = {
            "value": value,
            "next": None,
        }
        self.tail = self.head
        self.length = 1

    def append(self, value):
        """
        Add a new node with the specified value to the end of the linked list.
        Updates the tail and increments the length.
        """
        new_node = {"value": value, "next": None}
        self.tail["next"] = new_node
        self.tail = new_node
        self.length += 1
        return self

    def prepend(self, value):
        """
        Add a new node with the specified value to the beginning of the linked list.
        Updates the head and increments the length.
        """
        new_node = {"value": value, "next": None}
        new_node["next"] = self.head
        self.head = new_node
        self.length += 1
        return self

    def insert(self, idx, value):
        """
        Insert a new node with the given value at the specified index.
        If the index is greater than or equal to the list length, the new node is appended.
        """
        if idx >= self.length:
            return self.append(value)
        new_node = {"value": value, "next": None}
        leader = self.traverse_to_idx(idx - 1)
        follower = leader["next"]
        leader["next"] = new_node
        new_node["next"] = follower
        self.length += 1
        return self

    def traverse_to_idx(self, idx):
        """
        Traverse the list to return the node at the specified index.
        """
        counter = 0
        curr = self.head
        while counter != idx:
            curr = curr["next"]
            counter += 1
        return curr

    def _printList(self):
        """
        Traverse the linked list and return a list containing all node values in order.
        """
        array = []
        curr = self.head
        while curr is not None:
            array.append(curr["value"])
            curr = curr["next"]
        return array


my_linkedlist = LinkedList(10)

# append
my_linkedlist.append(5)
my_linkedlist.append(16)

# prepend
my_linkedlist.prepend(1)

# insert
my_linkedlist.insert(200, 99)
my_linkedlist.insert(2, 11)

# print(my_linkedlist.head)
print(my_linkedlist._printList())
