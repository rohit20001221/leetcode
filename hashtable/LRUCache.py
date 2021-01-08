from collections import deque

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.m = {}
        self.dque = deque()
    
    def get(self, key):
        if key in self.m:
            value = self.m[key]
            self.dque.remove(key)
            self.dque.append(key)
            return val
        else:
            return -1
    
    def put(self, key, value):
        if key not in self.m:
            if len(self.dque) == self.capacity:
                oldest = self.dque.popleft()
                del self.m[key]
        else:
            self.dque.remove(key)
        
        self.m[key] = value
        self.dque.append(key)