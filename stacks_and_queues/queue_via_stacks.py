import copy


class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyQueue:
    def __init__(self):
        self.stack1 = None
        self.stack2 = None

    def is_empty(self, stack):
        if stack is None:
            return True
        else:
            return False

    def push(self, data):
        if self.is_empty(self.stack1) and self.is_empty(self.stack2):
            node = StackNode(data)
            self.stack1 = node
        elif not self.is_empty(self.stack1):
            node = StackNode(data)
            node.next = self.stack1
            self.stack1 = node
        elif not self.is_empty(self.stack2):
            while self.stack2:
                if self.is_empty(self.stack1):
                    temp_node = copy.deepcopy(self.stack2)
                    temp_node.next = None
                    self.stack1 = temp_node
                else:
                    popped_node = copy.deepcopy(self.stack2)
                    popped_node.next = self.stack1
                    self.stack1 = popped_node
                self.stack2 = self.stack2.next
            node = StackNode(data)
            node.next = self.stack1
            self.stack1 = node

    def pop(self):
        if self.is_empty(self.stack1) and self.is_empty(self.stack2):
            return None
        elif not self.is_empty(self.stack2):
            popped_item = self.stack2.data
            self.stack2 = self.stack2.next
            return popped_item
        elif not self.is_empty(self.stack1):
            while self.stack1:
                if self.is_empty(self.stack2):
                    temp_node = copy.deepcopy(self.stack1)
                    temp_node.next = None
                    self.stack2 = temp_node
                else:
                    temp_node = copy.deepcopy(self.stack1)
                    temp_node.next = self.stack2
                    self.stack2 = temp_node
                self.stack1 = self.stack1.next
            popped_item = self.stack2.data
            self.stack2 = self.stack2.next
            return popped_item


if __name__ == "__main__":
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.push(4)
    queue.push(5)
    item = queue.pop()
    another = queue.pop()
    print(another)
    queue.push(6)
    new = queue.pop()
    new2 = queue.pop()
    print(new)
    print(new2)
    new3 = queue.pop()
    print(new3)
    new4 = queue.pop()
    print(new4)
