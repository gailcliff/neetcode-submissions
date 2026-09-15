class Node:
    
    def __init__(self, key, value, prev=None, next_=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next_


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: dict[int, Node] = {}

        self.left = Node(None, None)
        self.right = Node(None, None)

        self.left.next, self.right.prev = self.right, self.left
        

    def insert(self, node):
        left, right = self.right.prev, self.right
        node.prev, node.next = left, right
        left.next, right.prev = node, node


    def remove(self, node):
        left, right = node.prev, node.next

        left.next, right.prev = right, left


    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)

            return node.value
        
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)

            node.value = value
            self.insert(node)
        else:
            new_node = Node(key, value)
            self.insert(new_node)

            self.cache[key] = new_node

            if len(self.cache) > self.capacity:
                lru = self.left.next
                self.remove(lru)
                del self.cache[lru.key]
        
