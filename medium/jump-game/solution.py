from typing import List


class Solution:

    def canJump(self, nums: List[int]) -> bool:

        if len(nums) <= 1:
            return True

        if nums[0] == 0:
            return False

        firstZero = len(nums) - 1
        while firstZero >= 0 and nums[firstZero] != 0:
            firstZero -= 1

        if firstZero == -1:
            return True

        lastZero = firstZero
        while lastZero >= 0 and nums[lastZero] == 0:
            lastZero -= 1

        if lastZero == -1:
            return False

        lastZero += 1

        firstNonZeroAfterZeros = lastZero - 1
        while firstNonZeroAfterZeros >= 0:
            s = firstNonZeroAfterZeros + nums[firstNonZeroAfterZeros]
            if s > firstZero or s >= len(nums) - 1:
                return self.canJump(nums[:firstNonZeroAfterZeros + 1])
            firstNonZeroAfterZeros -= 1

        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.canJump([2, 3, 1, 1, 4]))
    print(sol.canJump([3, 2, 1, 0, 4]))
    print(sol.canJump([0]))
    print(sol.canJump([1]))
    print(sol.canJump([2, 0]))
    print(sol.canJump([2, 0, 0]))
    print(sol.canJump([2, 0, 0, 0]))
    print(sol.canJump([0, 1]))
    print(sol.canJump([1, 0]))
