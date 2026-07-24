class LRUCache:

    class QueueNode:
        def __init__(self, key):
            self.key = key
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.volume = 0
        self.cache = {}
        self.qHead = None
        self.qTail = None
        

    def get(self, key: int) -> int:
        if key in self.cache:
            returnedValue, cur = self.cache[key]
            if cur.next is None:
                return returnedValue
            # If it's not the tail
            if cur.prev:
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
            else:
                cur.next.prev = None
                self.qHead = cur.next

            self.qTail.next = cur
            cur.prev = self.qTail
            cur.next = None
            self.qTail = cur
            self.cache[key] = [returnedValue, cur]
            return returnedValue
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            _ = self.get(key)
            self.cache[key][0] = value
            return

        if self.volume == self.capacity:
            del self.cache[self.qHead.key]
            if self.qHead.next is None:
                self.qHead = self.qTail = None
            else:
                self.qHead = self.qHead.next
                self.qHead.prev = None
            self.volume -= 1

        if self.qTail is None:
            self.qHead = self.qTail = self.QueueNode(key)
        else:
            newNode = self.QueueNode(key)
            self.qTail.next = newNode
            newNode.prev = self.qTail
            self.qTail = newNode
        self.cache[key] = [value, self.qTail]
        self.volume += 1
            