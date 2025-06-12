# Queues

class Node:
    """
    Node class for use in the queue.
    Each node holds a value and a reference to the next node.
    """

    def __init__(self, value):
        """
        Initialize a new node with the given value.
        """
        self.value = value
        self.next = None


class Queue:
    """
    Queue data structure implemented using a singly linked list.
    Follows the FIFO (First-In-First-Out) principle.
    """

    def __init__(self):
        """
        Initialize an empty queue with first, last pointers and a length counter.
        """
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        """
        Return the node at the front of the queue without removing it.
        """
        return self.first

    def enqueue(self, value):
        """
        Add a new node with the given value to the end of the queue.
        """
        new_node = Node(value)
        if self.length == 0:
            self.first, self.last = new_node, new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return self

    def dequeue(self):
        """
        Remove and return the node at the front of the queue.
        If the queue is empty, return None.
        """
        if self.length == 0:
            return None
        if self.first == self.last:
            self.last = None
        self.first = self.first.next
        self.length -= 1
        return self

    def print_queue(self):
        """
        Print all elements in the queue from front to rear.
        """
        current = self.first
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")


# Example usage
myQueue = Queue()

# enqueue
myQueue.enqueue('nike')
myQueue.enqueue('adidas')
myQueue.enqueue('puma')
myQueue.enqueue('new balance')

# dequeue
myQueue.dequeue()
myQueue.dequeue()

# peek
myQueue.peek()

# print entire queue
myQueue.print_queue()
