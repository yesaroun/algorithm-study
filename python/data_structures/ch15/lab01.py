from stacks import Stack

class TreeNode:
    def __init__(self, elem):
        self.elem = elem

        self.left_child = None
        self.right_child = None

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.elem}"

class BTreeBuilder:
    # 이거하면 self쓰면 안된다
    @staticmethod
    def build(sexpr):
        stack = Stack()
        root = None


        return root

class BTree:
    def __init__(self, root):
        self.root = root

    def traverse_inorder(self):
        ret = []
        # using recursive ...

        def inorder_recursive(root):
            if root is None:
                return

            inorder_recursive(root.left_child)
            ret.append(root)
            inorder_recursive(root.right_child)

        inorder_recursive(self.root)
        return ret

        return ret

if __name__ == "__main__":
    sexpr = "( + ( * ( * ( / ( A B ) C ) D ) E ) )".split()
    root = BTreeBuilder.build(sexpr)
    tree = BTree(root)
    actions = tree.traverse_inorder()

    print(actions)