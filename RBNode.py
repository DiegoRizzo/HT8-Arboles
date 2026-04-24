class RBNode:
    def __init__(self, key):
        self.key = key
        self.color = 1 # 1 = Rojo, 0 = Negro
        self.left = None
        self.right = None
        self.parent = None
    