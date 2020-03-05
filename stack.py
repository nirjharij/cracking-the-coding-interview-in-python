class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, item):
        new_node = StackNode(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            print("Stack is empty")
            return
        item = self.top.data
        self.top = self.top.next
        return item

    def peek(self):
        if self.top is None:
            print("Stack is empty")
            return
        return self.top.data

    def is_empty(self):
        return self.top is None
