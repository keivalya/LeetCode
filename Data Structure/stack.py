# Stacks

class Node:
    """
    Node class used in the linked list-based stack implementation.
    Each node contains a value and a reference to the next node.
    """
    def __init__(self, value):
        """
        Initialize a new node with the given value.
        """
        self.value = value
        self.next = None


class Stack:
    """
    Stack data structure implemented using a singly linked list.
    Supports typical stack operations: push, pop, peek, and print.
    """
    def __init__(self):
        """
        Initialize an empty stack with top, bottom, and length attributes.
        """
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        """
        Return the top node of the stack without removing it.
        """
        return self.top

    def push(self, value):
        """
        Push a new value onto the top of the stack.
        """
        new_node = Node(value)
        if self.length == 0:
            self.top, self.bottom = new_node, new_node
        else:
            temp = self.top
            self.top = new_node
            self.top.next = temp
        self.length += 1
        return self

    def pop(self):
        """
        Remove and return the top element from the stack.
        If the stack is empty, print a message and return None.
        """
        if self.length == 0:
            print("The stack is empty!")
            return None

        if self.top == self.bottom:
            self.bottom = None

        self.top = self.top.next
        self.length -= 1

        return self

    def print_stack(self):
        """
        Print all elements in the stack from top to bottom.
        """
        current = self.top
        while current:
            print(current.value, end=" -> ")
            current = current.next


class Stack:
    """
    Stack data structure implemented using a dynamic Python list (array).
    This version is simpler and uses built-in list operations.
    """
    def __init__(self):
        """
        Initialize an empty stack using a list.
        """
        self.arr = []

    def peek(self):
        """
        Return the top value of the stack without removing it.
        If the stack is empty, print a message.
        """
        if len(self.arr) != 0:
            return self.arr[-1]
        else:
            print("Stack is empty")

    def push(self, value):
        """
        Push a new value onto the top of the stack.
        """
        return self.arr.append(value)

    def pop(self):
        """
        Remove and return the top value of the stack.
        """
        return self.arr.pop()

    def __str__(self):
        """
        Return a string representation of the stack contents.
        """
        return f"{self.arr}"


# Example usage:
myStack = Stack()
myStack.peek()
myStack.push('amazon')
myStack.push('google')
myStack.push('boston dynamics')
myStack.push('microsoft')
myStack.push('meta')
myStack.pop()
myStack.pop()

print(myStack)
