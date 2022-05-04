from typing import List


class Solution:

    def jump(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0

        lastJump = 1
        lastIndex = 0

        for i in range(3, len(nums) + 1):
            lastJumpNum = nums[lastIndex]
            if lastIndex + lastJumpNum < i - 1:
                maxDistInd = None
                maxDist = -1
                j = i - 2
                while j > lastIndex:
                    if nums[j] + j + 1 - i > maxDist:
                        maxDist = nums[j] + j + 1 - i
                        maxDistInd = j

                    j -= 1

                lastJump += 1
                lastIndex = maxDistInd

        return lastJump
