from binary_tree import BinarySearchTree


def check_subtree(t1, t2):
    # import pdb; pdb.set_trace()
    if t1 is None and t2 is None:
        return True
    elif t1 is None or t2 is None:
        return False
    elif t1.data != t2.data:
        return False
    else:
        left_subtree = check_subtree(t1.left_child, t2.left_child)
        right_subtree = check_subtree(t1.right_child, t2.right_child)
        if left_subtree and right_subtree:
            return True
        else:
            return False


def traverse(t1, t2):
    if t2 is None:
        return True

    if t1 is None:
        return

    if t1.data == t2.data:
        is_subtree = check_subtree(t1, t2)
        if is_subtree:
            return True
    left_subtree = traverse(t1.left_child, t2)
    right_subtree = traverse(t1.right_child, t2)
    if left_subtree or right_subtree:
        return True


if __name__ == "__main__":
    tree1 = BinarySearchTree()
    tree1.insert(10)
    tree1.insert(8)
    tree1.insert(12)
    tree1.insert(11)
    tree1.insert(15)
    tree1.insert(4)

    tree2 = BinarySearchTree()
    tree2.insert(12)
    tree2.insert(11)
    tree2.insert(13)

    res = traverse(tree1.root, tree2.root)
    if res:
        print("Subtree present")
    else:
        print("Subtree not present")
