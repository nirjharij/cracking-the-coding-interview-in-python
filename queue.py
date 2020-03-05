class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def add(self, item):
        new_node = Node(item)
        if self.last is not None:
            self.last.next = new_node
        self.last = new_node
        if self.first is None:
            self.first = self.last

    def remove(self):
        if self.first is None:
            print("Queue is empty")
            return
        item = self.first.data
        self.first = self.first.next
        if self.first is None:
            self.last = None
        return item
