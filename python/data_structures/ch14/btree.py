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
        stack = Stack()
        it = iter(sexpr)

        # 현재 문제는 right를 이상한애 한다 / left는 잘 한다
        root = None
        while stack.is_empty() or it:
            try:
                token = next(it)
            except StopIteration:
                break

            if token != ")":
                if token == "(" and not stack.is_empty():
                    root = stack.peek()
                if token == "#":
                    stack.push(TreeNode(None))
                else:
                    stack.push(TreeNode(token))
                continue

            prev = None

            while stack.peek().elem != "(":
                node = stack.peek()
                stack.pop()
                checker = 0
                if root == node:
                    a = stack.peek()
                    stack.pop()
                    if not stack.is_empty():
                        b = stack.peek()
                        stack.pop()
                        root = stack.peek()
                        stack.push(b)
                        stack.push(a)
                    else:
                        stack.push(a)
                        checker += 1

                if checker == 0:
                    if root.right_child is None:
                        root.right_child = node
                    else:
                        root.left_child = node

                prev = node

            stack.pop()

            if stack.is_empty():
                root = prev
                continue

            root = stack.peek()

            root.left_child = prev

            stack.pop()
            stack.push(root)

        if not stack.is_empty():
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