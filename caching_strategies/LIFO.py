class LIFOCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.stack = []

    def get(self, key):
        if key in self.cache:
            return self.cache[key]
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.cache[key] = value
        else:
            if len(self.cache) >= self.capacity:
                last_key = self.stack.pop()
                del self.cache[last_key]
            self.cache[key] = value
            self.stack.append(key)

# Example usage:
lifo_cache = LIFOCache(2)
lifo_cache.put(1, 1)  # Cache: {1: 1}
lifo_cache.put(2, 2)  # Cache: {1: 1, 2: 2}
print(lifo_cache.get(1))  # Returns 1
lifo_cache.put(3, 3)  # Evicts key 2, Cache: {1: 1, 3: 3}
print(lifo_cache.get(1))  # Returns 1
print(lifo_cache.get(2))  # Returns -1 (not found)
print(lifo_cache.get(3))  # Returns 3
lifo_cache.put(4, 4)  # Evicts key 3, Cache: {1: 1, 4: 4}
print(lifo_cache.get(3))  # Returns -1 (not found)
print(lifo_cache.get(4))  # Returns 4