from linked_list_operations import LinkedList


def deletenode(node):
    if node is None or node.next is None:
        return
    node.data = node.next.data
    node.next = node.next.next


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
    print("Before Deletion")
    llist.traverse()
    deletenode(llist.head.next.next)
    print("\nAfter Deletion")
    llist.traverse()


