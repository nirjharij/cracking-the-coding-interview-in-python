# Definition for singly-linked list.
from linked_list_operations import LinkedList


class Solution:
    def mergeKLists(self, lists):
        result = None
        for i in range(len(lists)):
            result = self.sorted_merge(result, lists[i])
        temp = result
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

    def sorted_merge(self, list1, list2):
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
        return final_list.head


if __name__ == "__main__":
    llist1 = LinkedList()
    llist1.push(5)
    llist1.push(4)
    llist1.push(1)
    llist2 = LinkedList()
    llist2.push(4)
    llist2.push(3)
    llist2.push(1)
    llist3 = LinkedList()
    llist3.push(6)
    llist3.push(2)
    s = Solution()
    resp = s.mergeKLists([llist1.head, llist2.head, llist3.head])
