class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def insert(self, node):
        # Insert before tail
        prev_node = self.tail.prev

        prev_node.next = node
        node.prev = prev_node

        node.next = self.tail
        self.tail.prev = node

    def get(self, key):
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Move node to MRU position
        self.remove(node)
        self.insert(node)

        return node.value

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]

            # Update value
            node.value = value

            # Move to MRU
            self.remove(node)
            self.insert(node)

        else:
            node = Node(key, value)

            self.cache[key] = node
            self.insert(node)

            # Remove LRU if capacity exceeded
            if len(self.cache) > self.capacity:
                lru = self.head.next

                self.remove(lru)
                del self.cache[lru.key]