from BSTree import BSTree
from Node import Node


class SpTree(BSTree):
    def __init__(self):
        super().__init__()
        self.header = Node(None)

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
            return

        self.splay(val)

        if self.root.val == val:
            return

        n = Node(val)
        if val < self.root.val:
            n.left = self.root.left
            n.right = self.root
            self.root.left = None
        else:
            n.right = self.root.right
            n.left = self.root
            self.root.right = None
        self.root = n

    def remove(self, val):
        if self.root is None:
            return

        self.splay(val)

        if self.root.val != val:
            return

        if self.root.left is None:
            self.root = self.root.right
        else:
            right_subtree = self.root.right
            self.root = self.root.left
            self.splay(val)
            self.root.right = right_subtree

    def splay(self, val):
        if self.root is None:
            return

        l = r = self.header
        t = self.root
        self.header.left = self.header.right = None

        while True:
            if val < t.val:
                if t.left is None:
                    break
                if val < t.left.val:
                    y = t.left
                    t.left = y.right
                    y.right = t
                    t = y
                    if t.left is None:
                        break
                r.left = t
                r = t
                t = t.left
            elif val > t.val:
                if t.right is None:
                    break
                if val > t.right.val:
                    y = t.right
                    t.right = y.left
                    y.left = t
                    t = y
                    if t.right is None:
                        break
                l.right = t
                l = t
                t = t.right
            else:
                break

        l.right = t.left
        r.left = t.right
        t.left = self.header.right
        t.right = self.header.left
        self.root = t
