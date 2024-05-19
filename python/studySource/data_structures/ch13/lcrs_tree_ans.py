from stacks import Stack

class Tree:
    def __init__(self):
        self.root = None

    def build(self, sexpr):
        stack = Stack()
        it = iter(sexpr)

        root = None
        # stack이 empty이거나 it가 있는 동안 반복
        while stack.is_empty() or it:
            try:
                token = next(it)
            except StopIteration:
                break

            # ) 가 아니면 TreeNode 객체로 stack에 저장해라
            if token != ")":
                stack.push(self.TreeNode(token))
                continue

            prev = None
            # ( 가 아니면 stack에 있는걸 빼서
            # 뺀거의 형제 노드를 prev로 정하고
            # 뺀 걸 prev에 저장한다
            # 그리고 이걸 반복한다
            while stack.peek().elem != "(":
                node = stack.peek()
                stack.pop()
                node.right_sibling = prev
                prev = node

            stack.pop()
            # "(" pop

            # 이 경우는 root인 경우 while문 나가기
            if stack.is_empty():
                root = prev
                continue

            root = stack.peek()
            # ( 앞에 있는 문자를 root에 저장 및 left_child 저장
            root.left_child = prev
            stack.pop()
            stack.push(root)
            # stack에 root 저장하고 뒤에 반복

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
