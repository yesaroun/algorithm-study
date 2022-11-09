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

            while stack_proc.peek().elem != "(":
                node = stack_proc.peek()
                stack_proc.pop()
                # print(node)
                node = node if node.elem != "#" else None
                stack_subtree.push(node)

            stack_proc.pop()    # remove "("
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

        root = self.root
        while root is not None and elem != root.elem:
            root = root.left_child if elem < root.elem else root.right_child

        return root

if __name__ == "__main__":
    sexpr = "( 30 ( 5 ( 2 # ) 40 ) )".split()
    sexpr = [int(i) if i.isnumeric() else i for i in sexpr]
    root = BTreeBuilder.build(sexpr)
    tree = BSTree(root)

    found = tree.search(5)
    print(found)
    found = tree.search(2)
    print(found)
    found = tree.search(40)
    print(found)
    found = tree.search(30)
    print(found)
    found = tree.search(35)
    print(found)