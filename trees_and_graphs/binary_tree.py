class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.parent = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def level_order_insert(self, data):
        queue = []
        new_node = Node(data)
        if self.root:
            queue.append(self.root)
            while queue:
                temp = queue.pop(0)
                if not temp.left_child:
                    temp.left_child = new_node
                    break
                else:
                    queue.append(temp.left_child)
                if not temp.right_child:
                    temp.right_child = new_node
                    break
                else:
                    queue.append(temp.right_child)
        else:
            self.root = new_node

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
                    new_node.parent = prev_node
                    temp = temp.left_child
                else:
                    new_node.parent = prev_node
                    temp = temp.right_child
            if data < prev_node.data:
                new_node.parent = prev_node
                prev_node.left_child = new_node
            elif data > prev_node.data:
                new_node.parent = prev_node
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

    def in_order_successor(self, node):
        if node.right_child:
            successor = self.find_min(node.right_child)
            return successor

        parent = node.parent
        while parent:
            if node != parent.right_child:
                break
            node = parent
            parent = node.parent
        return parent

    def find_min(self, node):
        min = node.data
        while node.left_child:
            min = node.left_child.data
            node = node.left_child
        return min


if __name__ == "__main__":
    bst_obj = BinarySearchTree()
    bst_obj.insert(20)
    bst_obj.insert(8)
    bst_obj.insert(22)
    bst_obj.insert(4)
    bst_obj.insert(12)
    bst_obj.insert(10)
    bst_obj.insert(14)
    # bst_obj.in_order(bst_obj.root)
    successor = bst_obj.in_order_successor(bst_obj.root.left_child.right_child.left_child)
    if successor:
        print(successor.data)
