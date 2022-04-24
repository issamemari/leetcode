class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        s = {}

        for i, n in enumerate(nums):
            if n in s:
                return [i, s[n]]
            else:
                s[target - n] = i
