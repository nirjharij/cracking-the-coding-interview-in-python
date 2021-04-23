from linked_list_operations import LinkedList


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class NewLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        self.tail.next = new_node
        self.tail = new_node

    def insert_at_beg(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        new_node.next = self.head
        self.head = new_node

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next


def partition_list(llist, partition):
    new_list = NewLinkedList()
    while llist:
        if llist.data < partition:
            new_list.insert_at_beg(llist.data)
        else:
            new_list.insert_at_end(llist.data)
        llist = llist.next
    new_list.traverse()


if __name__ == "__main__":
    llist = LinkedList()
    llist.push(1)
    llist.push(2)
    llist.push(10)
    llist.push(5)
    llist.push(8)
    llist.push(5)
    llist.push(3)
    partition_list(llist.head, 5)
