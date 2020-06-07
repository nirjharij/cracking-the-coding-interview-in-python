class StackNode:
    def __init__(self, start_index, next_index, max_index):
        self.start_index = start_index
        self.next_index = next_index
        self.max_index = max_index

    def is_full(self, arr):
        if arr[self.max_index] == None:
            return False
        else:
            return True

    def is_empty(self, arr):
        if arr[self.start_index] == None:
            return True
        else:
            return False


class ThreeStacks:
    def __init__(self, array_size):
        self.arr = [None] * array_size

        division = array_size//3
        first_stack_range = (0, division-1)
        second_stack_range = (0+division, (2*division)-1)
        third_stack_range = (0+2*division, 3*division)

        self.stack1 = StackNode(start_index=first_stack_range[0], next_index=first_stack_range[0], max_index=first_stack_range[1])
        self.stack2 = StackNode(start_index=second_stack_range[0], next_index=second_stack_range[0], max_index=second_stack_range[1])
        self.stack3 = StackNode(start_index=third_stack_range[0], next_index=third_stack_range[0], max_index=third_stack_range[1])

    def push(self, stack, data):
        if not stack.is_full(self.arr):
            next_index = stack.next_index
            self.arr[next_index] = data

    def pop(self, stack):
        if not stack.is_empty(self.arr):
            item = self.arr[stack.next_index]
            self.arr[stack.next_index] = None
            return item


if __name__ == "__main__":
    ts = ThreeStacks(10)
    ts.push(ts.stack1, 13)
    ts.push(ts.stack2, 12)
    ts.push(ts.stack2, 11)
    item = ts.pop(ts.stack1)
    print(item)
