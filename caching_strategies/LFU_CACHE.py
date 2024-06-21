from collections import defaultdict

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_node(self, node):
        """Add node to the front (right after head)"""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove_node(self, node):
        """Remove an existing node from the linked list"""
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        self.size -= 1

    def pop_tail(self):
        """Pop the node before the tail (least recently used)"""
        if self.size > 0:
            node = self.tail.prev
            self.remove_node(node)
            return node
        return None

class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.min_freq = 0
        self.node_map = {}  # key -> Node
        self.freq_map = defaultdict(DoublyLinkedList)  # freq -> DoublyLinkedList of Nodes

    def _update_freq(self, node):
        """Update node's frequency and move it to the corresponding frequency list"""
        freq = node.freq
        self.freq_map[freq].remove_node(node)
        if not self.freq_map[freq].size:
            if freq == self.min_freq:
                self.min_freq += 1
        node.freq += 1
        self.freq_map[node.freq].add_node(node)

    def get(self, key):
        if key in self.node_map:
            node = self.node_map[key]
            self._update_freq(node)
            return node.value
        return -1

    def put(self, key, value):
        if self.capacity == 0:
            return

        if key in self.node_map:
            node = self.node_map[key]
            node.value = value
            self._update_freq(node)
        else:
            if len(self.node_map) >= self.capacity:
                node_to_remove = self.freq_map[self.min_freq].pop_tail()
                if node_to_remove:
                    del self.node_map[node_to_remove.key]

            new_node = Node(key, value)
            self.node_map[key] = new_node
            self.min_freq = 1
            self.freq_map[1].add_node(new_node)

# Example usage:
lfu_cache = LFUCache(2)
lfu_cache.put(1, 1)  # Cache: {1:1}
lfu_cache.put(2, 2)  # Cache: {1:1, 2:2}
print(lfu_cache.get(1))  # Returns 1, Cache: {2:2, 1:1}
lfu_cache.put(3, 3)  # Evicts key 2, Cache: {1:1, 3:3}
print(lfu_cache.get(2))  # Returns -1 (not found)
print(lfu_cache.get(3))  # Returns 3, Cache: {1:1, 3:3}
lfu_cache.put(4, 4)  # Evicts key 1, Cache: {3:3, 4:4}
print(lfu_cache.get(1))  # Returns -1 (not found)
print(lfu_cache.get(3))  # Returns 3, Cache: {3:3, 4:4}
print(lfu_cache.get(4))  # Returns 4, Cache: {3:3, 4:4}