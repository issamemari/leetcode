class Solution:
    def robWithIndex(self, nums, start, end):

        if len(nums[start:end]) == 0:
            return 0

        if len(nums[start:end]) == 1:
            return nums[start]

        if len(nums[start:end]) == 2:
            return max(nums[start:end])

        if (start, end) in self.cache:
            return self.cache[(start, end)]

        if start == 0:
            t1 = nums[start] + self.robWithIndex(nums, start + 2, end - 1)
        else:
            t1 = nums[start] + self.robWithIndex(nums, start + 2, end)

        t2 = self.robWithIndex(nums, start + 1, end)

        self.cache[(start, end)] = max(t1, t2)
        return max(t1, t2)

    def rob(self, nums: List[int]) -> int:
        self.cache = {}
        return self.robWithIndex(nums, 0, len(nums))
