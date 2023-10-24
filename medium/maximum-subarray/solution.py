from typing import List
    

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        arr = [maxSum]
        for i in range(1, len(nums)):
            arr.append(max(arr[i-1] + nums[i], nums[i]))

            if arr[i] > maxSum:
                maxSum = arr[i]

        return maxSum
