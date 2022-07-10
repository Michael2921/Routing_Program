
class HashMap:
    def __init__(self, initial_capacity=10):
        # initialize the hash table with empty bucket list entries
        self.initial_capacity = initial_capacity
        self.size = 0
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

        # create hash key

    def make_hash_key(self, key):
        hash_key = hash(key) % self.initial_capacity
        return hash_key

        # insert into hashmap

    def insert(self, key, value):
        bucket = self.make_hash_key(key)
        self.table[bucket].append([key, value])
        self.size += 1

        # get values from hashmap
    def get(self, key):
        for item in self.table[self.make_hash_key(key)]:
            if item[0] == key:
                return item[1]
        return None

    # remove values from hashmap
    def remove(self, key):
        key_hash = self.make_hash_key(key)
        if self.table[key_hash] == None:
            return False
        for i in range(0, len(self.table[key_hash])):
            if self.table[key_hash][i][0] == key:
                self.table[key_hash].pop(i)
                return True
        return False

