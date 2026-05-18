class Node:
    def __init__(self, key, val):
        self.val = val
        # need key for removing it from the list later
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:
    # Discards the LRU item first
    def __init__(self, capacity: int):
        # points to of the linked list
        self.capacity = capacity
        # hash map to map key to node
        self.cache = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    #  helper functions:
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    

    def insert(self, node):
        # tail.prev is the last node
        # insert between tail.prev and tail
        old = self.tail.prev
        old.next = node
        self.tail.prev = node
        node.prev = old
        node.next = self.tail


    def get(self, key: int) -> int:
        # if we called it, then the linked list 
        # should link it next
        if key in self.cache:
            node = self.cache[key]
            # remove node from old position
            self.remove(node)
            # add it to the end
            self.insert(node)
            return node.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        # discard the LRU
        if key in self.cache:
            # remove old one
            self.remove(self.cache[key])
        # insert new node
        new_node = Node(key, value)
        self.cache[key] = new_node
        self.insert(new_node)

        if len(self.cache) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]


    