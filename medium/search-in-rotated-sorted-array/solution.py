from typing import List


class Solution:

    def binarySearch(self, nums, target, begin, end):
        if begin == end:
            return -1

        if begin + 1 == end:
            if nums[begin] == target:
                return begin
            return -1

        mid = (begin + end) // 2
        if nums[mid] == target:
            return mid

        if nums[mid] > target:
            return self.binarySearch(nums, target, begin, mid)

        return self.binarySearch(nums, target, mid + 1, end)

    def findRotationIndex(self, nums, begin, end):
        if begin + 1 == end:
            return begin

        if nums[begin] < nums[end - 1]:
            return begin

        mid = (begin + end) // 2
        if mid + 1 == end:
            return self.findRotationIndex(nums, begin, mid)

        if nums[mid] > nums[mid + 1]:
            return mid

        if nums[mid] > nums[begin]:
            return self.findRotationIndex(nums, mid + 1, end)

        return self.findRotationIndex(nums, begin, mid + 1)

    def search(self, nums: List[int], target: int) -> int:
        rotation_index = self.findRotationIndex(nums, 0, len(nums))
        if nums[rotation_index] == target:
            return rotation_index

        if target >= nums[0] and target <= nums[rotation_index]:
            return self.binarySearch(nums, target, 0, rotation_index + 1)

        return self.binarySearch(nums, target, rotation_index + 1, len(nums))
