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
    @staticmethod
    def build(sexpr):
        root = None

        # 메인 프로시저를 위한 스택
        stack_proc = Stack()
        # 서브트리를 위한 스택
        stack_subtree = Stack()

        for expr in sexpr:
            if expr != ")":
                stack_proc.push(TreeNode(expr))
                continue

            # case ")"
            # ( A ( B C
            while stack_proc.peek().elem != "(":
                node = stack_proc.peek()
                stack_proc.pop()
                # print(node)
                node = node if node.elem != "#" else None
                stack_subtree.push(node)

            # print(stack_subtree)

            stack_proc.pop()    # remove "("
            # print(stack_proc)
            # stack에 마지막 하나만(root) 들어가 있는 경우 ( A )
            if stack_proc.is_empty():
                root = stack_subtree.peek()
                stack_subtree.pop()
            else:
                root = stack_proc.peek()
                stack_proc.pop()

            if stack_subtree.is_empty():
                continue

            root.left_child = stack_subtree.peek()
            stack_subtree.pop()
            root.right_child = stack_subtree.peek()
            stack_subtree.pop()
            stack_proc.push(root)

        # 기술한 sexpr 이 잘못되었을때 나오는 에러
        if not stack_proc.is_empty():
            raise Exception("expression is wrong.")

        return root

class BSTree:
    """Binary Search Tree"""

    def __init__(self, root):
        self.root = root

    def search(self, elem):
        if self.root is None:
            raise Exception("the root is none")

        def search_recursive(root):
            if root is None:
                return None

            if elem == root.elem:
                return root

            root = (
                search_recursive(root.left_child)
                if elem < root.elem
                else search_recursive(root.right_child)
            )
            return root

        return search_recursive(self.root)

    def insert(self, elem):
        """using recursive insertion"""

        def insert_recursive(root):
            if root is None:
                return TreeNode(elem)
            if elem == root.elem:
                return root
            if elem < root.elem:
                root.left_child = insert_recursive(root.left_child)
            else:
                root.right_child = insert_recursive(root.right_child)

            return root

        self.root = insert_recursive(self.root)

    def traverse_preorder(self):
        ret = []

        def preorder_recursive(root):
            if root is None:
                return

            ret.append(root)
            preorder_recursive(root.left_child)
            preorder_recursive(root.right_child)

        preorder_recursive(self.root)
        return ret


if __name__ == "__main__":
    sexpr = "( 30 ( 5 ( 2 # ) 40 ) )".split()
    sexpr = [int(i) if i.isnumeric() else i for i in sexpr]
    root = BTreeBuilder.build(sexpr)
    tree = BSTree(root)
    actions = tree.traverse_preorder()
    print(actions)

    tree.insert(40)
    actions = tree.traverse_preorder()
    print(actions)

    tree.insert(80)
    actions = tree.traverse_preorder()
    print(actions)

    found = tree.search(40)
    print(found.right_child)
    print(found.left_child)