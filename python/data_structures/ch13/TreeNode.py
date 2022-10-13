class TreeNode:
    def __init__(self, elem):
        self.elem = elem
        self.left_child = None
        self.right_sibling = None

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.elem}"