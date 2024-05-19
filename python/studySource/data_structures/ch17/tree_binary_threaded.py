from stacks import Stack

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
                stack_proc.push(TreeNodeThreaded(expr))
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

class TreeNodeThreaded:
    def __init__(self, elem=None):
        self.elem = elem
        self.left_child = self.right_child = None
        self.left_thread = self.right_thread = False

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.elem}"

class ThreadedBinaryTree:
    """Threaded Binary Tree"""

    def __init__(self, root=None):
        self.root = root
        self.head = TreeNodeThreaded()
        self.head.left_thread = True
        self.head.right_thread = False
        self.head.left_child = self.head
        self.head.right_child = self.head

        self.__build()

    def __build(self):
        """using inorder traversal"""
        root = self.root
        stack = Stack()
        actions = []

        # using inorder traversal
        # 쓰레드를 연결해야 한다 / inorder해서 리스트를 만들어 놓고 하나씩 하면서 연결해도 괜찮다




    def find_successor(self, root):
        """원하는 노드의 successor를 찾아준다."""
        node = None

        node = root
        while node and node.left_child:
            node = node.left_child

        return node

    def traverse_inorder(self):
        """head 노드부터 시작하여 이진 스레드 트리를 중회 순행하며 출력"""
        root = self.find_successor(self.head)
        ret = []

        while root is not None and root is not self.head:
            ret.append(root)
            root = self.find_successor(root)

        return ret

    def traverse_postorder(self):
        raise NotImplemented

if __name__ == "__main__":
    sexpr = "( A ( B ( D ( H I ) E ) C ( F G ) ) )".split()
    root_ = BTreeBuilder.build(sexpr)
    tree = ThreadedBinaryTree(root_)

    root = tree.root
    e = root.left_child.right_child
    print(f"{e.left_child} <{e}> {e.right_child}")

    f = root.right_child.left_child
    print(f"{f.left_child} <{f}> {f.right_child}")

    g = root.right_child.right_child
    print(f"{g.left_child} <{g}> {g.right_child}")

    h = root.left_child.left_child.left_child
    print(f"{h.left_child} <{h}> {h.right_child}")

    i = root.left_child.left_child.right_child
    print(f"{i.left_child} <{i}> {i.right_child}")

    print()
    actions = tree.traverse_inorder()
    print(actions)