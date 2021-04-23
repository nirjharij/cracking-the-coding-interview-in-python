# Approach 1: Reverse the linked list and compare the first half of original list with reversed list.
# If it matches then it is a palindrome otherwise not

# Approach 2: Push first half elements of linked list to a stack if we know the size.
# If we do not know the size use fast and slow pointers to insert first half of linked list to stack
# and then pop out elements from stack and compare with second half of linked list
# to check whether the string is palindrome or not

# Approach 3:
from linked_list_operations import LinkedList


def check_palindrome(head, list_length):
    if head is None or list_length <= 0:
        return head, True
    elif list_length == 1:
        return head.next, True

    node, palindrome_flag = check_palindrome(head.next, list_length - 2)

    if not node or not palindrome_flag:
        return node, False

    if head.data != node.data:
        return node.next, False
    else:
        return node.next, True


if __name__ == '__main__':
    llist = LinkedList()
    llist.push(1)
    llist.push(2)
    llist.push(0)
    llist.push(2)
    llist.push(1)
    # llist.push(3)
    res, flag = check_palindrome(llist.head, 5)
    if flag:
       print("Is palindrome")
    else:
        print("Not palindrome")
