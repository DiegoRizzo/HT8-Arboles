from Node import Node

class BSTree:
    def __init__(self):
        self.root = None


    def insert(root, key):
        if root is None:
            return Node(key)
        if root.val == key:
            return root
        if root.val < key:
            root.right = BSTree.insert(root.right, key)
        else:
            root.left = BSTree.insert(root.left, key)
        return root

    def search(root, key):
        if root is None or root.val == key:
            return root
        
        if root.val < key:
            return BSTree.search(root.right, key)
        
        return BSTree.search(root.left, key)
    
    def get_successor(current):
        current = current.right
        while current is not None and current.left is not None:
            current = current.left
        return current
    
    def delete(root, key):
        if root is None:
            return root
        
        if root.val < key:
            root.right = BSTree.delete(root.right, key)
        elif root.val > key:
            root.left = BSTree.delete(root.left, key)
        
        else:
            if root.left is None:
                return root.right
            
            if root.right is None:
                return root.left

            successor = BSTree.get_successor(root)
            root.val = successor.val
            root.right = BSTree.delete(root.right, successor.val)
        
        return root