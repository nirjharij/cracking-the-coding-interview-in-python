class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.children = None
        self.parent = None
        self.size = 0


class Tree:
    def __init__(self):
        self.root = None

    def get_count(self, root):
        if root is None:
            return 0
        left_count = self.get_count(root.left)
        right_count = self.get_count(root.right)
        return left_count + right_count + 1

    def get_children_count(self, root):
        if root is None:
            return
        root.children = self.get_count(self.root)
        self.get_children_count(root.left)
        self.get_children_count(root.right)

    def get_random_node(self):
        pass
