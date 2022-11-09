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

class BTree:
    def __init__(self):
        self.root = None

    def build(self, sexpr):
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

            # print("stack_subtree : ", stack_subtree)

            stack_proc.pop()    # remove "("
            # print("stack_proc : ", stack_proc)
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

        if not stack_proc.is_empty():
            raise Exception("expression is wrong.")

        self.root = root

if __name__ == "__main__":
    sexpr = "( 30 ( 5 ( 2 # ) 40 ( # 80 ) ) )".split()
    tree = BTree()
    tree.build(sexpr)

    print(tree.root)
    print(tree.root.left_child)
    print(tree.root.left_child.left_child)
    print(tree.root.left_child.right_child)
    print(tree.root.right_child)
    print(tree.root.right_child.left_child)
    print(tree.root.right_child.right_child)

"""
30 
5
2 
None 
40 
None 
80
"""