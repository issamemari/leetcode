class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]

        result = []
        for i in range(len(nums)):
            smaller_perms = self.permute(nums[:i] + nums[i + 1:])
            for perm in smaller_perms:
                result.append([nums[i]] + perm)

        return result
