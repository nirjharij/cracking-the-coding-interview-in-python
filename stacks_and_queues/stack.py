class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.min_stack_top = None

    def push(self, item):
        new_node = StackNode(item)
        new_node.next = self.top
        self.top = new_node

        min_node = StackNode(item)
        min_node.next = self.min_stack_top
        if self.min_stack_top is None:
            self.min_stack_top = min_node
        else:
            if item < self.min_stack_top.data:
                self.min_stack_top = min_node

    def pop(self):
        if self.top is None:
            print("Stack is empty")
            return
        item = self.top.data
        self.top = self.top.next
        if item == self.min_stack_top.data:
            self.min_stack_top = self.min_stack_top.next
        return item

    def peek(self):
        if self.top is None:
            print("Stack is empty")
            return
        return self.top.data

    def is_empty(self):
        return self.top is None

    def get_min(self):
        if self.min_stack_top:
            item = self.min_stack_top.data
            self.min_stack_top = self.min_stack_top.next
            return item
        else:
            return ""


if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(12)
    stack.push(8)
    stack.push(40)
    min = stack.get_min()
    print(min)
    item = stack.pop()
    item2 = stack.pop()
    print(item, item2)
    stack_min = stack.get_min()
    print(stack_min)
