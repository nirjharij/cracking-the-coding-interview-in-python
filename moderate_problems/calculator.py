class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, item):
        new_node = StackNode(item)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.top is None:
            print("Stack is empty")
            return
        item = self.top.data
        self.top = self.top.next
        self.size -= 1
        return item

    def peek(self):
        if self.top is None:
            print("Stack is empty")
            return
        return self.top.data

    def is_empty(self):
        return self.top is None


class Calculator:
    def __init__(self):
        self.num_stack = Stack()
        self.op_stack = Stack()
        self.priority = {'+': 1, '-': 1, '/': 2, '*': 2, '': 0}

    def compute(self, expr):
        i = 0
        while i < len(expr):
            num = self.get_num(expr, i)
            i += len(num)
            self.num_stack.push(int(''.join(num)))
            if i >= len(expr):
                break
            op = expr[i]
            self.collapse_top(op)
            self.op_stack.push(op)
            i += 1
        self.collapse_top('')
        if self.num_stack.size == 1 and self.op_stack.size == 0:
            return self.num_stack.pop()
        return 0

    def get_num(self, expr, i):
        num = []
        while i < len(expr):
            if expr[i].isdigit():
                num.append(expr[i])
            else:
                break
            i += 1
        return num

    def get_operator(self, expr):
        pass

    def collapse_top(self, op):
        while self.num_stack.size >= 2 and self.op_stack.size >= 1:
            if self.priority[op] <= self.priority[self.op_stack.peek()]:
                second = self.num_stack.pop()
                first = self.num_stack.pop()
                operator = self.op_stack.pop()
                collapsed = self.apply_op(first, operator, second)
                self.num_stack.push(collapsed)
            else:
                break

    def apply_op(self, first, op, second):
        if op == '+':
            return first + second
        elif op == '-':
            return first - second
        elif op == '*':
            return first * second
        elif op == '/':
            return round(first / second, 1)
        else:
            return second


c = Calculator()
print(c.compute('2-6-7*8/2+5'))
