class Node:
    
    def __init__(self, key, value, prev=None, next_=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next_

class LRUCache:

    def __init__(self, capacity: int):
        self.cache: dict[int, Node] = {}
        self.capacity = capacity

        self.left = Node(float('-inf'), 0)
        self.right = Node(float('inf'), 0)

        self.left.next, self.right.prev = self.right, self.left


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        value = node.value

        self.remove(node)
        self.insert(key, value)

        return value


    def insert(self, key, value):
        left = self.right.prev
        right = self.right

        new_node = Node(key, value, left, self.right)

        left.next, right.prev = new_node, new_node

        self.cache[key] = new_node


    def remove(self, node):
        del self.cache[node.key]
        
        left, right = node.prev, node.next
        left.next, right.prev = left.next.next, right.prev.prev


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]

            self.remove(node)
        
        self.insert(key, value)

        if len(self.cache) > self.capacity:
            self.remove(self.left.next)
        

        
