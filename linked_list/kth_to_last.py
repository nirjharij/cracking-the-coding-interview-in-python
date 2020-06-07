from linked_list_operations import LinkedList


def kth_from_last(llist, k):
    if llist is None:
        return 1, False

    ret, found = kth_from_last(llist.next, k)
    # print(ret)
    if ret == k and not found:
        return llist.data, True
    if not found:
        return ret + 1, False
    else:
        return ret, True


def two_pointer(llist, k):
    ptr1 = llist
    ptr2 = llist
    for i in range(k-1):
        ptr2 = ptr2.next

    while ptr2.next != None:
        ptr1 = ptr1.next
        ptr2 = ptr2.next

    return ptr1.data


if __name__ == "__main__":
    llist = LinkedList()
    llist.push(4)
    llist.push(7)
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.push(5)
    llist.push(6)
    llist.push(8)
    llist.traverse()
    result = kth_from_last(llist.head, 3)
    print("\n")
    print("Kth FROM LAST By recursion:")
    print(result[0])
    result = two_pointer(llist.head, 3)
    print("Kth from Last By Two pointer:")
    print(result)
