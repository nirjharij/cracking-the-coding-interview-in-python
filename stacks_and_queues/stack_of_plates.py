class StackPlates:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack = [[]]
        self.top = None
        self.stack_index = 0
        self.sub_stack_top = [None]

    def push(self, data):
        if len(self.stack[self.stack_index]) == self.max_size:
            self.stack_index = self.stack_index + 1
            self.stack.append([data])
            self.top = self.stack[self.stack_index][0]
            self.sub_stack_top.append(None)
            self.sub_stack_top[self.stack_index] = self.top
        else:
            self.stack[self.stack_index].append(data)
            stack_size = len(self.stack[self.stack_index]) - 1
            self.top = self.stack[self.stack_index][stack_size]
            self.sub_stack_top[self.stack_index] = self.top

    def pop(self):
        if self.top:
            stack_size = len(self.stack[self.stack_index]) - 1
            item = self.stack[self.stack_index][stack_size]
            self.stack[self.stack_index].pop(stack_size)
            if stack_size > 0:
                self.top = self.stack[self.stack_index][stack_size-1]
                self.sub_stack_top[self.stack_index] = self.top
            elif stack_size == 0:
                self.stack.pop(self.stack_index)
                self.sub_stack_top[self.stack_index] = None
                self.stack_index = self.stack_index - 1
                self.top = self.stack[self.stack_index][self.max_size - 1]
            return item
        else:
            print("Stack is Empty")
            return None

    def pop_at_index(self, index):
        if index == self.stack_index:
            item = self.pop()
            return item
        else:
            item = self.stack[index][self.max_size - 1]
            for i in range(index+1, self.stack_index+1):
                if i == self.stack_index:
                    item_popped = self.pop()
                else:
                    item_popped = self.stack[i][self.max_size - 1]
                self.stack[i-1][self.max_size - 1] = item_popped
            return item


if __name__ == "__main__":
    stacks = StackPlates(2)
    stacks.push(1)
    stacks.push(2)
    stacks.push(3)
    stacks.push(4)
    stacks.push(5)
    # print(stacks.stack)
    # item = stacks.pop()
    # # print(item)
    # item = stacks.pop()
    # # print(item)
    # stacks.push(item)
    stacks.push(6)
    print(stacks.stack)
    item = stacks.pop_at_index(0)
    print(item)
    item = stacks.pop_at_index(0)
    print(item)
    print(stacks.stack)
