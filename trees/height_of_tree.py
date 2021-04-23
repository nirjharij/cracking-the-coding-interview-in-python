from binary_tree import BinarySearchTree


def height(tree):
    if not tree:
        return 0
    left_tree_depth = height(tree.left_child)
    right_tree_depth = height(tree.right_child)

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
    # bst_obj.in_order(bst_obj.root)
    tree_height = height(bst_obj.root)
    print(tree_height)
