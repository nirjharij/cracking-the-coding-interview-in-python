from binary_tree import BinarySearchTree


def weave(prefix, subtree_left, subtree_right, results):
    # print(subtree_left, subtree_right)
    if not len(subtree_left) or not len(subtree_right):
        results.append(prefix + subtree_left + subtree_right)
        return results

    left_subtree_item = subtree_left.pop(0)
    prefix.append(left_subtree_item)
    # print("left subtree")
    # print(subtree_left)
    weave(prefix, subtree_left, subtree_right, results)
    left_item = prefix.pop()
    subtree_left.insert(0, left_item)

    right_subtree_item = subtree_right.pop(0)
    prefix.append(right_subtree_item)
    # print("subtree right")
    # print(subtree_right)
    weave(prefix, subtree_left, subtree_right, results)
    right_item = prefix.pop()
    subtree_right.insert(0, right_item)

    return results


def traverse(root):
    results = []
    if root is None:
        return results
    prefix = [root.data]

    left_seq = traverse(root.left_child)
    right_seq = traverse(root.right_child)

    results = weave(prefix, left_seq, right_seq, results)

    return results


if __name__ == "__main__":
    bst_obj = BinarySearchTree()
    bst_obj.insert(20)
    bst_obj.insert(8)
    bst_obj.insert(22)
    bst_obj.insert(4)
    bst_obj.insert(12)
    bst_obj.insert(10)
    bst_obj.insert(14)
    # bst_obj.insert(2)
    # bst_obj.insert(1)
    # bst_obj.insert(3)
    res = traverse(bst_obj.root)
    print(res)
