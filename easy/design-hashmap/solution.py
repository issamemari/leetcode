class MyHashMap:

    def __init__(self):
        self.num_buckets = 1000
        self.buckets = [[]] * self.num_buckets

    def put(self, key: int, value: int) -> None:
        bucket_idx = self.hash_code(key) % self.num_buckets
        idx = self.find(key, bucket_idx)
        if idx == -1:
            self.buckets[bucket_idx].append((key, value))
        else:
            self.buckets[bucket_idx][idx] = (self.buckets[bucket_idx][idx][0], value)

    def find(self, key, bucket_idx):
        for i, (k, v) in enumerate(self.buckets[bucket_idx]):
            if k == key:
                return i
        return -1

    def get(self, key: int) -> int:
        bucket_idx = self.hash_code(key) % self.num_buckets
        idx = self.find(key, bucket_idx)
        if idx == -1:
            return -1
        else:
            return self.buckets[bucket_idx][idx][1]

    def remove(self, key: int) -> None:
        bucket_idx = self.hash_code(key) % self.num_buckets
        idx = self.find(key, bucket_idx)
        if idx != -1:
            self.buckets[bucket_idx] = self.buckets[bucket_idx][:idx] + self.buckets[bucket_idx][idx + 1:]

    def hash_code(self, key: int):
        return key


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
