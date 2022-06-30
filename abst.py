class aBST:

    def __init__(self, depth):
        # правильно рассчитайте размер массива для дерева глубины depth:
        tree_size = pow(2,depth + 1)
        self.Tree = [None] * tree_size # массив ключей

    def FindKeyIndex(self, key):
        i = 0
        while i < len(self.Tree):
            if self.Tree[i] == key:
                return i
            if self.Tree[i] == None:
                return -i

            if self.Tree[i] > key:
                i = i*2 + 1
                continue
            if self.Tree[i] < key:
                i = i*2 + 2
                continue
        return None # не найден

    def AddKey(self, key):
        indexToAdd = self.FindKeyIndex(key)
        if indexToAdd == None:
            return -1

        if indexToAdd == 0:
            self.Tree[indexToAdd] = key
            return 0

        if indexToAdd < 0:
            indexToAdd = -indexToAdd
            self.Tree[indexToAdd] = key
            return indexToAdd

        if indexToAdd > 0:
            return indexToAdd

        return -1
