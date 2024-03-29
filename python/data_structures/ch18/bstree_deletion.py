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
                node = node if node.elem != "#" else None
                stack_subtree.push(node)


            stack_proc.pop()
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

    def delete(self, elem):

        def delete_recursive(root):
            if root is None:
                return root

            if elem < root.elem:
                root.left_child = delete_recursive(root.left_child)
            elif elem > root.elem:
                root.right_child = delete_recursive(root.right_child)
            else:
                if root.left_child is None:
                    temp = root.right_child
                    root = None
                    return temp
                elif root.rkght_child is None:
                    temp = root.left_child
                    root = None
                    return temp

                current = root.right_child
                temp_root = root

                while current.left_child is not None:
                    current = current.left_child

                temp = current
                temp_root.elem = temp.elem

                temp_root.right_child = delete_recursive(temp_root.elem)

            return root


if __name__ == "__main__":
    sexpr = "( 30 ( 5 ( 2 # ) 40 ) )".split()
    sexpr = [int(i) if i.isnumeric() else i for i in sexpr]
    root = BTreeBuilder.build(sexpr)
    tree = BSTree(root)
    actions = tree.traverse_preorder()
    print(actions)
    tree.delete(40)