class LinkedList:

    def __init__(self, value):
        self.head = {
            "value": value,
            "next": None,
        }
        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_node = {"value": value, "next": None}
        self.tail["next"] = new_node
        self.tail = new_node
        self.length += 1
        return self


my_linkedlist = LinkedList(10)
my_linkedlist.append(5)
my_linkedlist.append(16)

print(my_linkedlist.head)
