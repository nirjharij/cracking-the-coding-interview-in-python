from binary_tree import BinarySearchTree


def check_balanced(tree):
    if not tree:
        return 0
    left_tree_depth = check_balanced(tree.left_child)
    if left_tree_depth == -1:
        return -1
    right_tree_depth = check_balanced(tree.right_child)
    if right_tree_depth == -1:
        return -1
    if abs(left_tree_depth - right_tree_depth) > 1:
        return -1
    else:
        return max(left_tree_depth, right_tree_depth) + 1


if __name__ == "__main__":
    bst_obj = BinarySearchTree()
    bst_obj.insert(20)
    bst_obj.insert(30)
    bst_obj.insert(10)
    bst_obj.insert(15)
    bst_obj.insert(12)
    bst_obj.insert(6)
    bst_obj.insert(2)
    bst_obj.insert(40)
    bst_obj.insert(50)
    bst_obj.insert(28)
    bst_obj.insert(25)
    # bst_obj.in_order(bst_obj.root)
    tree_height = check_balanced(bst_obj.root)
    if tree_height == -1:
        print("Not balanced")
    else:
        print("Balanced")
