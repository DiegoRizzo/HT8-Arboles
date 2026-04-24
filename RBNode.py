class RBNode:
    def __init__(self, key):
        self.key = key
        self.color = 1 # 1 = Rojo, 0 = Negro
        self.left = None
        self.right = None
        self.parent = None
    
    def grandparent(self):
        if self.parent is None:
            return None
        return self.parent.parent
    
    def sibling(self):
        if self.parent is None:
            return None
        if self == self.parent.left:
            return self.parent.right
        return self.parent.left
    
    def uncle(self):
        if self.parent is None:
            return None
        return self.parent.sibling()
    