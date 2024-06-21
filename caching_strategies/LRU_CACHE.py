class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # Maps key to node
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        """Remove an existing node from the linked list."""
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def _add(self, node):
        """Add a new node right before the tail."""
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def get(self, key):
        """Return the value of the key if it exists, otherwise return -1."""
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def put(self, key, value):
        """Update the value of the key if it exists, otherwise add the key-value pair to the cache."""
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self._add(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            # Remove the least recently used (LRU) node
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]

# Example usage:
lru_cache = LRUCache(2)
lru_cache.put(1, 1)  # Cache: {1: 1}
lru_cache.put(2, 2)  # Cache: {1: 1, 2: 2}
print(lru_cache.get(1))  # Returns 1, Cache: {2: 2, 1: 1}
lru_cache.put(3, 3)  # Evicts key 2, Cache: {1: 1, 3: 3}
print(lru_cache.get(2))  # Returns -1 (not found)
lru_cache.put(4, 4)  # Evicts key 1, Cache: {3: 3, 4: 4}
print(lru_cache.get(1))  # Returns -1 (not found)
print(lru_cache.get(3))  # Returns 3, Cache: {4: 4, 3: 3}
print(lru_cache.get(4))  # Returns 4, Cache: {3: 3, 4: 4}