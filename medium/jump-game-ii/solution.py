from typing import List


class Solution:

    def __init__(self):
        self.cache = {}

    def jumpRecursive(self, nums: List[int], index: int):

        if len(nums) <= 1:
            return 0

        if index in self.cache:
            return self.cache[index]

        minJumps = float("inf")
        num = nums[index]

        if num + index >= len(nums) - 1:
            return 1

        for i in range(1, num + 1):
            jumps = 1 + self.jumpRecursive(nums, index + i)
            if jumps < minJumps:
                minJumps = jumps

        self.cache[index] = minJumps
        return minJumps

    def jump(self, nums: List[int]) -> int:
        return self.jumpRecursive(nums, 0)
