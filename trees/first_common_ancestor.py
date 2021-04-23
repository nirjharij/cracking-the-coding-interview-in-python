from binary_tree import BinarySearchTree

node1_present = False
node2_present = False


def first_common_ancestor(root, node1, node2):
    if not root:
        return None
    if root.data == node1:
        global node1_present
        node1_present = True
        return root
    if root.data == node2:
        global node2_present
        node2_present = True
        return root

    left_fca = first_common_ancestor(root.left_child, node1, node2)
    right_fca = first_common_ancestor(root.right_child, node1, node2)

    if left_fca and right_fca:
        return root

    return left_fca if left_fca else right_fca


if __name__ == "__main__":
    bst_obj = BinarySearchTree()
    bst_obj.level_order_insert(20)
    bst_obj.level_order_insert(30)
    bst_obj.level_order_insert(10)
    bst_obj.level_order_insert(15)
    bst_obj.level_order_insert(12)
    bst_obj.level_order_insert(6)
    node1 = 30
    node2 = 7
    fca = first_common_ancestor(bst_obj.root, node1, node2)
    if node1_present and node2_present:
        print(f"FCA: {fca.data}")
    else:
        print("FCA: None")
