# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.
#
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
#
# The cache is initialized with a positive capacity.
#
# Follow up:
# Could you do both operations in O(1) time complexity?
#
# Example:
#
# LRUCache cache = new LRUCache( 2 /* capacity */ );
#
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(4);       // returns 4
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dict = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.dict:
            node = self.dict[key]
            self.remove(node)  # remove and add back to make it most recently used
            self.add(node)
            return node.value
        return -1

    def put(self, key, value):
        if key in self.dict: self.remove(self.dict[key])
        node = Node(key, value)
        self.add(node)
        self.dict[key] = node                  #Double linked clist serves as the valur of the dictionary
        if len(self.dict) > self.capacity:
            node = self.head.next
            self.remove(node)
            del self.dict[node.key]

    # helper function
    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    # helper function
    def add(self, node):
        prev = self.tail.prev
        prev.next = node
        self.tail.prev = node
        node.prev = prev
        node.next = self.tail


obj = LRUCache(2)
obj.put(1, 1)
obj.put(2, 2)
obj.put(3, 3)    #  evicts key 2
obj.get(2)     # returns -1 (not found)
obj.put(4, 4)    #  evicts key 1
obj.get(1)     # returns -1 (not found)
obj.get(3)       #  returns 3
obj.get(4)       #  returns 4
param_1 = obj.get(4)
print param_1