from typing import List


class Solution:

    def binarySearchInsert(self, l: List[int], count, begin, end, key) -> int:
        if begin == end:
            return begin

        if begin + 1 == end:
            if count > key(l[begin]):
                return end
            return begin

        mid = (begin + end) // 2
        if count == key(l[mid]):
            return mid

        if count > key(l[mid]):
            return self.binarySearchInsert(l, count, mid, end, key)

        return self.binarySearchInsert(l, count, begin, mid, key)

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1

        nums_ordered = []
        for num, count in counts.items():
            index = self.binarySearchInsert(nums_ordered, count, 0, len(nums_ordered), lambda x: x[1])
            nums_ordered.insert(index, (num, count))

        return [num for num, _ in nums_ordered[-k:]]


if __name__ == "__main__":
    sol = Solution()
    print(sol.topKFrequent([5,2,5,3,5,3,1,1,3], 2))
