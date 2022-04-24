from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if len(nums) < 3:
            return []

        num_to_index = {}
        for index, num in enumerate(nums):
            num_to_index[num] = index

        res = set()
        for index1, num1 in enumerate(nums):

            taken = set()
            for index2, num2 in enumerate(nums[index1 + 1:]):
                index2 = index1 + index2 + 1
                s = -(num1 + num2)
                if s in num_to_index:
                    index3 = num_to_index[s]

                    if index3 != index2 and index3 != index1 and not index3 in taken and not index2 in taken:
                        print(index1, index2, index3)
                        res.add(tuple(sorted([num1, num2, s])))
                        taken.add(index3)
                        taken.add(index2)

        return list(res)


if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([1,2,-2,-1]))
