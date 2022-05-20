from typing import List


class Solution:

    def binarySearchInsert(self, nums: List[int], target: int, begin: int, end: int):
        if begin >= end:
            if target <= nums[begin]:
                return begin
            return begin + 1

        mid = (begin + end) // 2
        if nums[mid] == target:
            return mid

        if nums[mid] > target:
            return self.binarySearchInsert(nums, target, begin, mid)

        return self.binarySearchInsert(nums, target, mid + 1, end)

    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binarySearchInsert(nums, target, 0, len(nums) - 1)
