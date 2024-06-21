from collections import deque

class FIFOCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.queue = deque()

    def get(self, key):
        if key in self.cache:
            return self.cache[key]
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.cache[key] = value
        else:
            if len(self.cache) >= self.capacity:
                oldest_key = self.queue.popleft()
                del self.cache[oldest_key]
            self.cache[key] = value
            self.queue.append(key)

# Example usage:
fifo_cache = FIFOCache(2)
fifo_cache.put(1, 1)  # Cache: {1: 1}
fifo_cache.put(2, 2)  # Cache: {1: 1, 2: 2}
print(fifo_cache.get(1))  # Returns 1
fifo_cache.put(3, 3)  # Evicts key 1, Cache: {2: 2, 3: 3}
print(fifo_cache.get(1))  # Returns -1 (not found)
print(fifo_cache.get(2))  # Returns 2
print(fifo_cache.get(3))  # Returns 3
fifo_cache.put(4, 4)  # Evicts key 2, Cache: {3: 3, 4: 4}
print(fifo_cache.get(2))  # Returns -1 (not found)
print(fifo_cache.get(3))  # Returns 3
print(fifo_cache.get(4))  # Returns 4
