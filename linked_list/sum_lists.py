from linked_list_operations import LinkedList


def sum_reversed_num_list(l1, l2):
    final_list = LinkedList()
    if l1 is None and l2 is None:
        return
    if l1 and l2 is None:
        return l1
    if l2 and l1 is None:
        return l2
    carry = 0
    while l1 or l2:
        if l1 and l2:
            sum = l1.data + l2.data
            if carry:
                sum = sum + carry
            val = sum % 10
            final_list.push(val)
            if sum >= 10:
                carry = 1
            else:
                carry = 0
            l1 = l1.next
            l2 = l2.next
        elif l1 and not l2:
            sum = l1.data
            if carry:
                sum = carry + sum
            val = sum % 10
            final_list.push(val)
            if sum >= 10:
                carry = 1
            else:
                carry = 0
            l1 = l1.next
        elif l2 and not l1:
            sum = l2.data
            if carry:
                sum = carry + sum
            val = sum % 10
            final_list.push(val)
            if sum >= 10:
                carry = 1
            else:
                carry = 0
            l2 = l2.next
    if carry:
        final_list.push(carry)
    final_list.reverse()
    final_list.traverse()


if __name__ == "__main__":
    llist1 = LinkedList()
    llist1.push(1)
    llist1.push(9)
    llist1.push(8)
    llist1.push(2)
    llist2 = LinkedList()
    llist2.push(4)
    llist2.push(3)
    llist2.push(2)
    sum_reversed_num_list(llist1.head, llist2.head)
