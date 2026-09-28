class Node:
    def __init__(self, key=-1, value=-1):
        self.key, self.value = key, value
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = self.right.prev
            node.next = self.right
            self.right.prev.next = node
            self.right.prev = node
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = self.right.prev
            node.next = self.right
            self.right.prev.next = node
            self.right.prev = node
        else:
            node = Node(key, value)
            node.prev = self.right.prev
            node.next = self.right
            self.right.prev.next = node
            self.right.prev = node
            self.cache[key] = node
            if len(self.cache) > self.cap:
                self.cache.pop(self.left.next.key)
                self.left.next.next.prev = self.left
                self.left.next = self.left.next.next
            