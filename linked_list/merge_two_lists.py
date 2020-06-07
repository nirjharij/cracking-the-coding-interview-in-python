from linked_list_operations import LinkedList


def sorted_merge(list1, list2):
    if list1 is None:
        return list2
    elif list2 is None:
        return list1

    final_list = LinkedList()
    while list1 or list2:
        if list1 and list2 is None:
            final_list.insertatend(list1.data)
            list1 = list1.next
            continue

        if list2 and list1 is None:
            final_list.insertatend(list2.data)
            list2 = list2.next
            continue

        if list1.data < list2.data:
            final_list.insertatend(list1.data)
            list1 = list1.next
        elif list1.data > list2.data:
            final_list.insertatend(list2.data)
            list2 = list2.next
        elif list1.data == list2.data:
            final_list.insertatend(list1.data)
            final_list.insertatend(list2.data)
            list1 = list1.next
            list2 = list2.next
    return final_list


if __name__ == "__main__":
    llist1 = LinkedList()
    llist1.push(10)
    llist1.push(9)
    llist1.push(8)
    llist1.push(7)
    llist1.push(6)
    llist1.push(5)
    llist2 = LinkedList()
    llist2.push(4)
    llist2.push(3)
    llist2.push(2)
    llist2.push(2)
    llist2.push(1)
    llist2.push(0)
    final_list = sorted_merge(llist1.head, llist2.head)
    final_list.traverse()
