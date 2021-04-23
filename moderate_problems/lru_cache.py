class Cache:
    def __init__(self):
        self.cache_max_size = 5
        self.cache_dict = dict()
        self.dll = DLL()

    def insert(self, key, value):
        if key not in self.cache_dict:
            if not self.cache_is_full():
                self.cache_dict[key] = self.dll.insert(key, value)
            else:
                least_recently_used_key = self.find_lru()
                self.remove_key(least_recently_used_key)
                self.cache_dict[key] = self.dll.insert(key, value)
        else:
            print("Key already present")

    def retrieve(self, key):
        if key in self.cache_dict:
            self.update_most_recently_used(key)
            return self.cache_dict[key].value
        else:
            print(f"No data for {key} found in cache")
            return None

    def print_cache(self, key):
        if key in self.cache_dict:
            print(self.cache_dict[key].value)
        else:
            print(f"Key {key} not found")

    def cache_is_full(self):
        if len(self.cache_dict) >= self.cache_max_size:
            return True
        else:
            return False

    def find_lru(self):
        lru_node = self.dll.tail
        self.dll.remove_last()
        return lru_node.key

    def update_most_recently_used(self, key):
        node = self.cache_dict[key]
        self.dll.move_to_front(node)

    def remove_key(self, key):
        self.dll.remove_node(self.cache_dict[key])
        del self.cache_dict[key]


class Node:
    def __init__(self, key, val):
        self.key = key
        self.value = val
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, key, value):
        node = Node(key, value)
        if not self.head:
            self.head = node
            self.tail = self.head
        else:
            temp = self.head
            temp.prev = node
            node.next = temp
            self.head = node
        return node

    def remove_last(self):
        temp = self.tail
        self.tail = temp.prev
        temp.prev.next = None

    def remove_node(self, node):
        # if only one node present
        if self.head == self.tail == node:
            self.head = None
            self.tail = None
        else:
            prev_node = node.prev
            next_node = node.next
            if prev_node:
                prev_node.next = next_node
            else:
                self.head = next_node

    def move_to_front(self, node):
        # while node.prev:
        #     prev_node = node.prev
        #     next_node = node.next
        #     node.prev = prev_node.prev
        #     node.next = prev_node
        #     prev_node.next = next_node
        # self.head = node
        self.remove_node(node)
        self.insert(node.key, node.value)


c = Cache()
c.insert(12, "Nirjhari")
c.insert(13, "Pankhuri")
c.insert(14, "Puneet")
c.insert(15, "Nisheeth")
c.insert(11, "Kashvi")
print(c.retrieve(15))
print(c.retrieve(11))
print(c.retrieve(13))
print(c.retrieve(14))
c.insert(16, 'Ravi')
c.print_cache(12)
