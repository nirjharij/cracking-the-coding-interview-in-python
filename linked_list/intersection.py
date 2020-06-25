from linked_list_operations import LinkedList


def find_intersection(l1, l2, l1_len, l2_len):
    if l1_len > l2_len:
        ptr_jump = l1_len - l2_len
        for i in range(ptr_jump):
            l1.head = l1.head.next
    elif l2_len > l1_len:
        ptr_jump = l2_len - l1_len
        for i in range(ptr_jump):
            l2.head = l2.head.next
    else:
        ptr_jump = 0

    while l1.head and l2.head:
        if l1.head == l2.head:
            return True
        l1.head = l1.head.next
        l2.head = l2.head.next
    return False


if __name__ == "__main__":
    llist = LinkedList()
    llist.insertatend(4)
    llist.insertatend(7)
    llist.insertatend(1)
    llist.insertatend(2)

    llist2 = LinkedList()
    llist2.insertatend(5)
    llist2.insertatend(2)
    llist2.insertatend(1)
    llist2.insertatend(7)
    llist2.tail.next = llist.head.next.next
    llist2.tail = llist.head.next.next
    llist2.tail.next = llist.head.next.next.next
    llist2.tail = llist.head.next.next.next

    out = find_intersection(llist, llist2, 4, 6)
    if out:
        print("Intersection exists")
    else:
        print("No intersection found")
