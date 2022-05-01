class Solution:

    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        fib0 = nums[0]
        fib1 = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            t1 = nums[i] + fib0
            t2 = fib1

            fib0 = fib1
            fib1 = max(t1, t2)

        return fib1
