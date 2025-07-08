from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dictionary = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.dictionary:
            return -1
        self.dictionary.move_to_end(key)
        return self.dictionary[key]

    def put(self, key: int, value: int) -> None:
        if key in self.dictionary:
            del self.dictionary[key]
        self.dictionary[key] = value
        if len(self.dictionary) > self.capacity:
            self.dictionary.popitem(last = False)

# Code Explanation:
# The cache stores key-value pairs in an OrderedDict.
# When we get a key, if it exists, it moves to the end (most recently used).
#When we put a key:
    #If it exists, it's first deleted.
    #Then inserted at the end (most recently used).
# If the cache is full, the least recently used item (front of the dict) is removed. 
