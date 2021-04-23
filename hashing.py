# global hash_table


class HashTable:
    def __init__(self, size):
        global hash_table
        hash_table = [[] for i in range(size)]

    def hash_func(self, key):
        return len(key) % 100

    def insert(self, key):
        index = self.hash_func(key)
        hash_table[index].append(key)

    def search(self, key):
        index = self.hash_func(key)
        for i in hash_table[index]:
            if i == key:
                return True
        return False

    def delete(self, key):
        index = self.hash_func(key)
        for ind, value in enumerate(hash_table[index]):
            if value == key:
                hash_table[index].remove(value)
                return True
        return False


if __name__ == "__main__":
    hash_table_obj = HashTable(100)
    hash_table_obj.insert("Testing")
    hash_table_obj.insert("testing")
    print(hash_table)
    search_status = hash_table_obj.search("Testing")
    print("Found: {}".format(search_status))
    delete_status = hash_table_obj.delete("testing")
    print("Deleted: {}".format(delete_status))
    print(hash_table)
