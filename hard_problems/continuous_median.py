from heapq import heappop, heappush, heapify


class Median:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        heapify(self.min_heap)
        heapify(self.max_heap)

    def get_median(self):
        if len(self.max_heap) == len(self.min_heap):
            max_ele = heappop(self.max_heap)
            min_ele = heappop(self.min_heap)
            return (max_ele + min_ele) // 2
        else:
            return -1 * heappop(self.max_heap)

    def add_number(self, random_number):
        if len(self.max_heap) == len(self.min_heap):
            if self.min_heap and random_number > self.min_heap[0]:
                heappush(self.max_heap, -1 * heappop(self.min_heap))
                heappush(self.min_heap, random_number)
            else:
                heappush(self.max_heap, -1 * random_number)
        else:
            if random_number < -1 * self.max_heap[0]:
                heappush(self.min_heap, -1 * heappop(self.max_heap))
                heappush(self.max_heap, -1 * random_number)
            else:
                heappush(self.min_heap, random_number)


m = Median()
m.add_number(4)
m.add_number(3)
m.add_number(6)
print(m.get_median())
