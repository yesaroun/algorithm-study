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

class TreeNode:
    def __init__(self, elem):
        self.elem = elem
        self.value = None  # boolean value
        self.left_child = self.right_child = None

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.elem}“

    def calculate_propositional(self, *param):
        ret = None

        def calculate_recursive(root):
            raise NotImplemented

        calculate_recursive(self.root)
        return ret


class PropositionalTree:
    pass
    # 이거 btree처럼 만들어야 할듯


if __name__ == "__main__":
    sexpr = "( OR ( OR ( AND ( 0 NOT ( # 1 ) ) AND ( NOT ( # 0 ) 2 ) ) NOT ( # 2 ) ) )".split()
    root = BTreeBuilder.build(sexpr)
    tree = PropositionalTree(root)

    prop = tree.calculate_propositional(False, True, False)
    print(prop.value)