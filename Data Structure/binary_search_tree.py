# Binary Search Tree (BST)

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BinarySearchTree:
    """
    A Binary Search Tree (BST) implementation supporting insert, & lookup.
    """
    def __init__(self):
        self.root = None

    def insert(self, value):
        """
        Insert a new value into the BST.
        Maintains the BST property: left < root < right.
        """
        new_node = Node(value)
        if not self.root:
            self.root = new_node
        else:
            curr = self.root
            while True:
                if value < curr.value:
                    if not curr.left:
                        curr.left = new_node
                        return self
                    curr = curr.left
                else:
                    if not curr.right:
                        curr.right = new_node
                        return self
                    curr = curr.right

    def lookup(self, value):
        """
        Search for a value in the BST.
        Returns True if found, otherwise False.
        """
        if not self.root:
            return None
        else:
            curr = self.root
            while curr:
                if value < curr.value:
                    curr = curr.left
                elif value > curr.value:
                    curr = curr.right
                else:
                    return True
        return False

    def remove(self, value):
        """
        Remove a node with the specified value from the BST.
        (Implementation not provided.)
        """
        pass

    def print_tree(self, node=None, prefix="", is_left=True):
        """
        Recursively print the BST structure in a visually readable format.
        """
        if node is None:
            node = self.root
        if node.right:
            self.print_tree(node.right,
                            prefix + ("│   " if is_left else "    "), False)

        print(prefix + ("└── " if is_left else "┌── ") + str(node.value))

        if node.left:
            self.print_tree(node.left,
                            prefix + ("    " if is_left else "│   "), True)


# Example usage
tree = BinarySearchTree()

# insert
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
tree.print_tree()

# lookup (exists/not)
print(tree.lookup(5))   # False
print(tree.lookup(20))  # True
