class Heap:

    def __init__(self):
        self.HeapArray = []
        self.heap_size = 0

    def MakeHeap(self, a, depth):
        tree_size = pow(2,depth + 1) - 1
        self.HeapArray = [None] * tree_size
        for value in a:
            self.Add(value)

    def heapify(self, index):
        left = index*2 + 1
        right = index*2 + 2

        largest = index

        if left < self.heap_size and self.HeapArray[left] > self.HeapArray[largest]:
            largest = left

        if right < self.heap_size and self.HeapArray[right] > self.HeapArray[largest]:
            largest = right

        if largest != index:
            self.HeapArray[largest], self.HeapArray[index] = self.HeapArray[index], self.HeapArray[largest]
            self.heapify(largest)

    def GetMax(self):
        if self.heap_size == 0:
            return -1

        max_value = self.HeapArray[0]
        last_value = self.HeapArray[self.heap_size - 1]

        self.HeapArray[0] = last_value
        self.heap_size -= 1
        self.HeapArray[self.heap_size] = None
        self.heapify(0)

        return max_value

    def Add(self, key):
        if len(self.HeapArray) == self.heap_size:
            return False

        i = self.heap_size
        self.HeapArray[i] = key
        self.heap_size += 1
        while i != 0:
            if self.HeapArray[self.parent(i)] > self.HeapArray[i]:
                return True
            self.HeapArray[self.parent(i)], self.HeapArray[i] = self.HeapArray[i], self.HeapArray[self.parent(i)]
            i = self.parent(i)

        return True

    def parent(self, index):
        return (index - 1)//2


