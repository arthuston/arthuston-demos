# /usr/bin/env python3

"""
Least recently used cache.
"""


class LinkedNode:
    """
    Linked list node.
    """

    def __init__(self, prev, nxt, key=None):
        self.prev = prev
        self.nxt = nxt
        self.key = key

    def __str__(self):
        return str(self.key)


class LinkedList:
    """
    LinkedList with ability to push, pop, and pro
    """

    def __init__(self):
        self.front = LinkedNode(None, None)
        self.back = LinkedNode(self.front, None)
        self.front.nxt = self.back

    def push(self, key):
        node = LinkedNode(self.back.prev, self.back, key)
        self.back.prev.nxt = node
        self.back.prev = node
        return node

    def move_to_end(self, node):
        self._remove(node)
        return self.push(node.key)

    def pop(self):
        node = self.front.nxt
        self._remove(self.front.nxt)
        return node

    def _remove(self, node):
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev

    def __str__(self):
        sep = ''
        s = 'lru: ['
        node = self.front.nxt
        while node != self.back:
            s += sep
            sep = ', '
            s += str(node.key)
            node = node.nxt
        s += ']'
        return s


class LRUCache:
    """
    Least recently used cache.
    """

    cache = {}
    used = LinkedList()

    def __init__(self, max_size):
        self.max_size = max_size

    def get(self, key):
        if key in self.cache:
            self.cache[key]['used'] = self.used.move_to_end(self.cache[key]['used'])
            return self.cache[key]['value']
        return None

    def put(self, key, value):
        if key in self.cache:
            # move used to now and set new value
            used = self.used.move_to_end(self.cache[key]['used'])
            self.cache[key] = {'value': value, 'used': used}
        else:
            if len(self.cache) == self.max_size:
                # remove lru
                used = self.used.pop()
                del self.cache[used.key]
            # add new key
            used = self.used.push(key)
            self.cache[key] = {'value': value, 'used': used}

    def __str__(self):
        s = 'cache: {'
        sep = ''
        for k, v in self.cache.items():
            s += sep
            sep = ', '
            s += '%d: ' % k
            s += ''
            s += str(v['value'])
        s += '}, '
        s += str(self.used)
        return s


if __name__ == '__main__':
    test_data = [6, 16, 5, 21, 24, 4, 3, 17, 20, 12]
    print('test_data: %s' % str(test_data))
    limit = 5
    cache = LRUCache(limit)

    print("adding values")
    for i in range(0, len(test_data)):
        cache.put(i, test_data[i])
        print('put %d %d %s' % (i, test_data[i], str(cache)))

    print("updating values")
    for i in range(5, len(test_data)):
        cache.put(i, test_data[i] + 1)
        print('put %d %d %s' % (i, test_data[i] + 1, str(cache)))

    print("getting values")
    for i in range(0, len(test_data)):
        result = str(cache.get(i))
        print('get %d = %s %s' % (i, result, str(cache)))

    print("done")
