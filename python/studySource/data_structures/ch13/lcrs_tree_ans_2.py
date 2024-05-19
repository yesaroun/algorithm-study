from stacks import Stack

class Tree:
    def __init__(self):
        self.root = None

    def build(self, sexpr):
        stack = Stack()
        it = iter(sexpr)

        root = None
        while stack.is_empty() or it:
            try:
                token = next(it)
            except StopIteration:
                break

            if token != ")":
                stack.push(self.TreeNode(token))
                continue

            prev = None
            while stack.peek().elem != "(":
                node = stack.peek()
                stack.pop()
                node.right_sibling = prev
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

    class TreeNode:
        def __init__(self, elem):
            self.elem = elem
            self.left_child = None
            self.right_sibling = None

        def __repr__(self):
            return str(self)

        def __str__(self):
            return f"{self.elem}"


if __name__ == "__main__":
    sexpr = "( A ( B ( E ( K L ) F ) C ( G ) D ( H ( M ) I J ) ) )"
    sexpr = sexpr.split()

    tree = Tree()
    tree.build(sexpr)
    root = tree.root
    print(root)
    b = root.left_child
    print(b)
    e = b.left_child
    print(e)
    k = e.left_child
    print(k)
    l = k.right_sibling
    print(l)
    f = e.right_sibling
    print(f)
    c = b.right_sibling
    print(c)
    d = c.right_sibling
    print(d)
    g = c.left_child
    print(g)
    h = d.left_child
    print(h)
    i = h.right_sibling
    print(i)
    j = i.right_sibling
    print(j)