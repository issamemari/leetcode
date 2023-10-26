from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        begin = 0
        end = len(nums)
        while True:
            if end - begin == 0:
                return -1, -1

            mid = begin + (end - begin) // 2
            if nums[mid] == target:
                left, right = mid, mid
                while left >= 0 and nums[left] == target:
                    left -= 1

                while right < len(nums) and nums[right] == target:
                    right += 1

                return left + 1, right - 1

            if nums[mid] > target:
                end = mid
            else:
                begin = mid + 1
