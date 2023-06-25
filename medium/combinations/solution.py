from typing import List


class Solution:

    def combine_nums(self, nums, k: int):
        if len(nums) == k:
            return [nums]

        if k == 1:
            return [[x] for x in nums]

        results = []
        for i in range(len(nums)):
            nums_without_me = nums[i + 1:]
            smaller_combinations = self.combine_nums(nums_without_me, k - 1)
            for combination in smaller_combinations:
                results.append([nums[i]] + combination)

        return results

    def combine(self, n: int, k: int) -> List[List[int]]:
        return self.combine_nums(list(range(1, n + 1)), k)


if __name__ == "__main__":
    s = Solution()
    print(s.combine(7, 4))
