class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def equals(self, node):
        return self.val == node.val
