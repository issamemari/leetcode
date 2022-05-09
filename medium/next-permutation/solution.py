from typing import List


class Solution:
    def binarySearch(self, nums, target, begin, end):
        """
        This binary search function finds the last element
        in the list that is larger than the give target.

        Assumes the list is sorted in descending order.
        """
        while begin <= end:
            mid = (begin + end) // 2
            if nums[mid] > target:
                if mid + 1 <= end and nums[mid + 1] > target:
                    begin = mid + 1
                    continue

                return mid

            end = mid - 1

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1

        if i == 0:
            nums.reverse()
            return

        index = self.binarySearch(nums, nums[i - 1], i, len(nums) - 1)
        nums[i - 1], nums[index] = nums[index], nums[i - 1]

        for j in range((len(nums) - i) // 2):
            nums[i + j], nums[len(nums) - j - 1] = nums[len(nums) - j - 1], nums[i + j]
