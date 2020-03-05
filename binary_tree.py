class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if not self.root:
            self.root = new_node
        else:
            temp = self.root
            prev_node = temp
            while temp is not None:
                prev_node = temp
                if new_node.data < temp.data:
                    temp = temp.left_child
                else:
                    temp = temp.right_child
            if data < prev_node.data:
                prev_node.left_child = new_node
            elif data > prev_node.data:
                prev_node.right_child = new_node

    def in_order(self, node):
        """
        LEFT -- ROOT -- RIGHT
        :return:
        """
        if node is not None:
            self.in_order(node.left_child)
            print(node.data)
            self.in_order(node.right_child)

    def pre_order(self):
        """
        ROOT -- LEFT -- RIGHT
        :return:
        """
        pass

    def post_order(self):
        pass


if __name__ == "__main__":
    bst_obj = BinarySearchTree()
    bst_obj.insert(20)
    bst_obj.insert(30)
    bst_obj.insert(10)
    bst_obj.insert(15)
    bst_obj.insert(12)
    bst_obj.insert(6)
    bst_obj.insert(2)
    bst_obj.in_order(bst_obj.root)
