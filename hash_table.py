class HashTable:
    def __init__(self, size):
        self.data = [[] for _ in range(size)]

    def _hash(self, key: str) -> int:
        h = 0
        for i, ch in enumerate(key):
            h = (h + ord(ch) * i) % len(self.data)
        return h

    def set(self, key: str, value):
        idx = self._hash(key)
        for slot in self.data[idx]:
            if slot[0] == key:
                slot[1] = value
                return
        self.data[idx].append([key, value])

    def get(self, key: str):
        idx = self._hash(key)
        for k, v in self.data[idx]:
            if k == key:
                return v
        return None

    def keys (self):
        keysArray = []
        for i in range(len(self.data)):
            if self.data[i]:
                keysArray.append(self.data[i][0][0])
        return keysArray


if __name__ == "__main__":
    ht = HashTable(50)
    ht.set("grapes", 10)
    ht.set("apples", 5)
    print(ht.keys())
