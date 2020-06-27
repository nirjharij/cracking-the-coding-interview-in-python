from linked_list_operations import LinkedList


def detect_loop(llist):
    found = False
    if llist is None:
        return None
    slow_ptr = llist
    fast_ptr = llist
    while fast_ptr.next and fast_ptr:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
        if slow_ptr is fast_ptr:
            found = True
            break
    if found:
        slow_ptr = llist
        while slow_ptr != fast_ptr:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next
        return fast_ptr
    else:
        return None


if __name__ == "__main__":
    llist = LinkedList()
    llist.insertatend(4)
    llist.insertatend(7)
    llist.insertatend(1)
    llist.insertatend(2)
    llist.insertatend(3)
    llist.tail.next = llist.head.next.next
    node = detect_loop(llist.head)
    if node:
        print("Loop present")
        print(node.data)
    else:
        print("Loop not present")
