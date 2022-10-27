from stacks import Stack

class BTree:
    def __init__(self, root):
        self.root = root

    def traverse_inorder_iterative(self):
        ret = []
        root = self.root
        stack = Stack()
        ...
        return ret

if __name__ == "__main__":
    sexpr = "( + ( * ( * ( / ( A B ) C ) D ) E ) )".split()
    root = BTreeBuilder.build(sexpr)
    tree = BTree(root)
    actions = tree.traverse_inorder_iterative()

    print(actions)