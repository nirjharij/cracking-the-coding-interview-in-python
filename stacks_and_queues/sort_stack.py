class StackNode:
    def __init__(self, data):
        self.next = None
        self.data = data


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = StackNode(data)
        if self.top:
            new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top:
            temp = self.top
            item = temp.data
            self.top = self.top.next
            return item
        else:
            print("Stack is empty")

    def peek(self):
        if self.top:
            return self.top.data

    def is_empty(self):
        if self.top:
            return False
        else:
            return True

    def sort_stack(self, ss_stack):
        # import pdb; pdb.set_trace()
        while not self.is_empty():
            temp = self.pop()
            while not ss_stack.is_empty() and ss_stack.peek() > temp:
                self.push(ss_stack.pop())
            ss_stack.push(temp)

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(8)
    s.push(5)
    s.push(11)
    ss_stack = Stack()
    s.sort_stack(ss_stack)
    ss_stack.print_stack()
