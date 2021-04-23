import sys


class MinHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize+1)
        self.Heap[0] = -1 * sys.maxsize
        self.FRONT = 1

    def parent(self, pos):
        return pos//2

    def left_child(self, pos):
        return 2 * pos

    def right_child(self, pos):
        return (2 * pos) + 1

    def swap(self, c_pos, p_pos):
        self.Heap[c_pos], self.Heap[p_pos] = self.Heap[p_pos], self.Heap[c_pos]

    def insert(self, item):
        if self.size > self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = item
        current_pos = self.size
        while self.Heap[current_pos] < self.Heap[self.parent(current_pos)]:
            self.swap(current_pos, self.parent(current_pos))
            current_pos = self.parent(current_pos)

    def min_heapify(self, pos):
        if not self.isLeaf(pos):
            if self.Heap[pos] > self.Heap[self.left_child(pos)] or self.Heap[pos] > self.Heap[self.right_child(pos)]:
                if self.Heap[self.left_child(pos)] < self.Heap[self.right_child(pos)]:
                    self.swap(pos, self.left_child(pos))
                    self.min_heapify(self.left_child(pos))
                else:
                    self.swap(pos, self.right_child(pos))
                    self.min_heapify(self.right_child(pos))

    def isLeaf(self, pos):
        if pos >= (self.size // 2) and pos <= self.size:
            return True
        return False

    def minHeap(self):
        for pos in range(self.size // 2, 0, -1):
            self.min_heapify(pos)

    def Print(self):
        for i in range(1, (self.size//2)+1):
            print("PARENT : " + str(self.Heap[i]) + " LEFT CHILD : " + str(self.Heap[(2*i)]) + " RIGHT CHILD : " +
                  str(self.Heap[(2*i)+1]))

    def remove(self):
        item = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.min_heapify(self.FRONT)
        return item


if __name__ == '__main__':
    min_heap = MinHeap(15)
    min_heap.insert(5)
    min_heap.insert(3)
    min_heap.insert(17)
    min_heap.insert(10)
    min_heap.insert(84)
    min_heap.insert(19)
    min_heap.insert(6)
    min_heap.insert(22)
    min_heap.insert(9)
    min_heap.insert(2)
    min_heap.minHeap()
    min_heap.Print()
    print("The Min val is " + str(min_heap.remove()))
