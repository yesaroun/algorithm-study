class BTree:
    def __init__(self, root):
        self.root = root
    def traverse_postorder(self):
        ret = []
        # using recursive ...
        return ret

if __name__ == "__main__":
    sexpr = "( + ( * ( * ( / ( A B ) C ) D ) E ) )".split()
    root = BTreeBuilder.build(sexpr)
    tree = BTree(root)
    actions = tree.traverse_ostorder()
    print(actions)