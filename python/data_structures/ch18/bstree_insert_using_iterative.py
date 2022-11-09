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

    def insert(self, elem):
        parent = None
        root = self.root

        while root is not None and elem != root.elem:
            parent = root
            root = root.left_child if elem < root.elem else root.right_child

        if root is not None:
            return

        node_new = TreeNode(elem)
        if parent is None:
            self.root = node_new
            return

        if parent.elem > node_new.elem:
            parent.left_child = node_new
        else:
            parent.right_child = node_new

        # 새로운 노드를 하나 만들어서 넣는다.
        # 내가 왼쪽에 넣을지 오른쪽일지 모르는데 그러면 parent의 키값과 비교해서 root가 더 크면
        # 루트의 좌측에 짚어넣는다. 그렇지 않으면 우측에 넣으면 된다.

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