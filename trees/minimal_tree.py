# Given sorted array create a bst with minimal height


from binary_tree import BinarySearchTree


bst_obj = BinarySearchTree()


def minimal_tree(array):
    start = 0
    end = len(array) - 1
    mid = int((start+end)/2)

    left_array = array[start:mid]
    right_array = array[mid+1:end+1]

    if start > end:
        return

    if left_array == right_array:
        # print("Found 1")
        return array[mid]

    bst_obj.insert(array[mid])
    print("Root")
    print(array[mid])
    left_child = minimal_tree(left_array)
    right_child = minimal_tree(right_array)
    print("Left and Right children")
    print(left_child, right_child)
    if left_child:
        bst_obj.insert(left_child)
    if right_child:
        bst_obj.insert(right_child)


minimal_tree([1, 2, 3, 4, 5, 6, 7, 8, 9])
bst_obj.in_order(bst_obj.root)
