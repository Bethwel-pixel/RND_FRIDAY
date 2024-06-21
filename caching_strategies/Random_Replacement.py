import random

class RandomCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.keys = []

    def get(self, key):
        if key in self.cache:
            return self.cache[key]
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.cache[key] = value
        else:
            if len(self.cache) >= self.capacity:
                # Randomly select and remove an existing key
                rand_index = random.randint(0, len(self.keys) - 1)
                key_to_remove = self.keys[rand_index]
                del self.cache[key_to_remove]
                self.keys.remove(key_to_remove)
            self.cache[key] = value
            self.keys.append(key)

# Example usage:
random_cache = RandomCache(3)
random_cache.put(1, 1)  # Cache: {1: 1}
random_cache.put(2, 2)  # Cache: {1: 1, 2: 2}
print(random_cache.get(1))  # Returns 1
random_cache.put(3, 3)  # Cache: {1: 1, 2: 2, 3: 3}
print(random_cache.get(2))  # Returns 2
random_cache.put(4, 4)  # Evicts randomly, Cache: {2: 2, 3: 3, 4: 4} or {1: 1, 3: 3, 4: 4} etc.
print(random_cache.get(1))  # Returns 1 or -1 (depends on eviction)
print(random_cache.get(2))  # Returns 2 or -1 (depends on eviction)
print(random_cache.get(3))  # Returns 3
print(random_cache.get(4))  # Returns 4