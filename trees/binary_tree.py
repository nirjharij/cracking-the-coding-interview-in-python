from collections import defaultdict


class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.parent = None
        self.size = 1


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.count = 0
        self.bottom_view_dict = defaultdict(list)

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

    def pre_order(self, root):
        """
        ROOT -- LEFT -- RIGHT
        :return:
        """
        if root is None:
            return
        stack = [root]
        while stack:
            item = stack.pop()
            print(item.data)
            if item.right_child:
                stack.append(item.right_child)
            if item.left_child:
                stack.append(item.left_child)

    def post_order(self, root):
        stack = []
        while True:
            while root:
                if root.right_child is not None:
                    stack.append(root.right_child)
                stack.append(root)
                root = root.left_child


            root = stack.pop()

            if not stack:
                print(root.data)
                break

            if root.right_child is not None and stack[-1] == root.right_child:
                stack.pop()
                stack.append(root)
                root = root.right_child
            else:
                print(root.data)
                root = None

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

    def generate_random_node(self):
        pass

    def count_nodes(self, node):
        if node is None:
            return
        self.count_nodes(node.left_child)
        self.count += 1
        self.count_nodes(node.right_child)

    def mirror(self, root):
        if root is None:
            return

        self.mirror(root.left_child)
        self.mirror(root.right_child)

        root.right_child, root.left_child = root.left_child, root.right_child

    def inorder_iterative(self, root):
        stack = []
        current = root

        while True:
            if current is not None:
                stack.append(current)
                current = current.left_child
            elif stack:
                current = stack.pop()
                print(current.data)
                current = current.right_child
            else:
                break

    def print_boundary(self, root):
        if root:
            print(root.data)
            self.print_left_boundary(root.left_child)

            self.print_leaves(root.left_child)
            self.print_leaves(root.right_child)

            self.print_right_boundary(root.right_child)

    def print_left_boundary(self, root):
        if root:
            if root.left_child:
                print(root.data)
                self.print_left_boundary(root.left_child)
            elif root.right_child:
                print(root.data)
                self.print_left_boundary(root.right_child)

    def print_right_boundary(self, root):
        if root:
            if root.right_child:
                self.print_right_boundary(root.right_child)
                print(root.data)
            elif root.left_child:
                self.print_right_boundary(root.left_child)
                print(root.data)

    def print_leaves(self, root):
        if root:
            self.print_leaves(root.left_child)

            if root.left_child is None and root.right_child is None:
                print(root.data)

            self.print_leaves(root.right_child)

    def left_view(self, root, level, max_level):
        if root is None:
            return
        if max_level < level:
            print(root.data)
            max_level = level

        self.left_view(root.left_child, level+1, max_level)
        self.left_view(root.right_child, level+1, max_level)

    def bottom_view(self, root, hd=0):
        if root is None:
            return
        self.bottom_view_dict[hd].append(root.data)
        self.bottom_view(root.left_child, hd - 1)
        self.bottom_view(root.right_child, hd + 1)

    def spiral_traversal(self, root, ltr=True):
        queue = [root]
        while queue:
            item = queue.pop(0)
            print(item.data)
            if not queue:
                ltr = not ltr
            if ltr:
                if item.left_child:
                    queue.append(item.left_child)
                if item.right_child:
                    queue.append(item.right_child)
            else:
                if item.right_child:
                    queue.append(item.right_child)
                if item.left_child:
                    queue.append(item.left_child)

    def level_order_traversal(self, root):
        queue = [root]
        while queue:
            item = queue.pop(0)
            print(item.data)
            if item.left_child:
                queue.append(item.left_child)
            if item.right_child:
                queue.append(item.right_child)

    def print_nodes_k_distance_from_root(self, root, k):
        if root is None:
            return
        if k == 0:
            print(root.data)
        else:
            self.print_nodes_k_distance_from_root(root.left_child, k - 1)
            self.print_nodes_k_distance_from_root(root.right_child, k - 1)

    def print_all_nodes_at_k_distance_of_node(self, node, target, k):
        if node is None:
            return -1
        if node.data == target:
            self.print_nodes_k_distance_from_root(node, k)
            return 0

        left_distance = self.print_all_nodes_at_k_distance_of_node(node.left_child, target, k)

        if left_distance != -1:
            if left_distance + 1 == k:
                print(node.data)
            else:
                self.print_nodes_k_distance_from_root(node.right_child, k-2-left_distance)
            return left_distance + 1

        right_distance = self.print_all_nodes_at_k_distance_of_node(node.right_child, target, k)

        if right_distance != -1:
            if right_distance + 1 == k:
                print(node.data)
            else:
                self.print_nodes_k_distance_from_root(node.left_child, k - 2 - right_distance)
            return right_distance + 1


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
    # successor = bst_obj.in_order_successor(bst_obj.root.left_child.right_child.left_child)
    # if successor:
    #     print(successor.data)
    # bst_obj.count_nodes(bst_obj.root)
    # print(bst_obj.count)
    # bst_obj.in_order(bst_obj.root)
    # bst_obj.mirror(bst_obj.root)
    # print("***********")
    # bst_obj.in_order(bst_obj.root)
    # bst_obj.pre_order(bst_obj.root)
    # bst_obj.post_order(bst_obj.root)
    # bst_obj.bottom_view(bst_obj.root)
    # print(bst_obj.bottom_view_dict)
    # bst_obj.level_order_traversal(bst_obj.root)
    bst_obj.spiral_traversal(bst_obj.root)
