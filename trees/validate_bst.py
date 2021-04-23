from binary_tree import BinarySearchTree


def check_bst(root, min, max):
    if not root:
        return True

    if (min and root.data <= min) or (max and root.data >= max):
        return False

    if not check_bst(root.left_child, min, root.data) or not check_bst(root.right_child, root.data, max):
        return False

    return True


if __name__ == "__main__":
    bst_obj = BinarySearchTree()
    bst_obj.level_order_insert(20)
    bst_obj.level_order_insert(30)
    bst_obj.level_order_insert(10)
    bst_obj.level_order_insert(15)
    bst_obj.level_order_insert(12)
    bst_obj.level_order_insert(6)
    # bst_obj.insert(2)
    # bst_obj.insert(40)
    # bst_obj.insert(50)
    # bst_obj.insert(28)
    # bst_obj.insert(25)
    bst_obj.in_order(bst_obj.root)
    is_bst = check_bst(bst_obj.root, None, None)
    if is_bst:
        print("Is a BST")
    else:
        print("Is not a BST")
