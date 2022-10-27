class BTree:
    def __init__(self, root):
        self.root = root

    def traverse_levelorder(self):
        # using recursive
        raise NotImplemented

    def traverse_levelorder_iterative(self):
        # using iterative
        raise NotImplemented

if __name__ == "__main__":
    sexpr = "( + ( * ( * ( / ( A B ) C ) D ) E ) )".split()
    root = BTreeBuilder.build(sexpr)
    tree = BTree(root)
    actions = tree.traverse_levelorder()
    print(actions)

    actions = tree.traverse_levelorder_iterative()
    print(actions)