class Node:
    def __init__(self, key, id, value, order) -> None:
        self.key = key
        self.id = id
        self.value = value
        self.order = order


class NodeFactory:
    def __init__(self) -> None:
        self.count = 0

    def create(self, key, id, value) -> Node:
        node = Node(key, id, value, self.count)
        self.count += 1
        return node


class MinBinaryHeap:
    def __init__(self):
        self.heap = []
        self.map = {}
        self.node_factory = NodeFactory()

    def size(self):
        return len(self.heap)

    def peek(self):
        return self.heap[0]

    def insert(self, key, id, value):
        node = self.node_factory.create(key, id, value)
        self.heap.append(node)
        last_index = len(self.heap) - 1
        self.map[node.id] = last_index
        self._swim(last_index)

    def _swim(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[parent].key > self.heap[index].key:
                self._swap(index, parent)
                index = parent
            else:
                break

    def _swap(self, a, b):
        self.map[self.heap[a].id] = b
        self.map[self.heap[b].id] = a
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]

    def pop(self):
        self._swap(0, len(self.heap) - 1)
        node = self.heap.pop()
        self.map.pop(node.id)
        self._sink(0)
        return node

    def _sink(self, index):
        length = len(self.heap)
        while True:
            left = index * 2 + 1
            right = index * 2 + 2
            smallest = index
            if left < length and self.heap[left].key < self.heap[smallest].key:
                smallest = left
            if right < length and self.heap[right].key < self.heap[smallest].key:
                smallest = right
            if smallest == index:
                break
            self._swap(index, smallest)
            index = smallest

    def decrease_key(self, id, key):
        index = self.map[id]
        self.heap[index].key = key
        self._swim(index)
