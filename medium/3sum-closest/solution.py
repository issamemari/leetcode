from typing import List


class Solution:

    def binarySearch(self, nums: List[int], num, begin, end):

        if end < begin:
            return end

        if begin == end:
            if nums[begin] >= num:
                return begin
            if nums[begin] < num:
                return begin + 1

        mid = (begin + end) // 2
        if nums[mid] == num:
            return mid

        if nums[mid] > num:
            return self.binarySearch(nums, num, begin, mid - 1)

        return self.binarySearch(nums, num, mid + 1, end)

    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums = sorted(nums)

        closestSum = None
        closestDistance = float("inf")
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                s = nums[i] + nums[j]
                closestThirdIndex = self.binarySearch(nums, target - s, 0, len(nums) - 1)

                if closestThirdIndex == i:
                    closestThirdIndex += 1
                if closestThirdIndex == j:
                    closestThirdIndex += 1

                if closestThirdIndex >= len(nums):
                    newClosestSum = s + nums[closestThirdIndex - 1]
                else:
                    index1 = closestThirdIndex
                    index2 = min(max(closestThirdIndex - 1, j + 1), len(nums) - 1)

                    diff1 = abs(s + nums[index1] - target)
                    diff2 = abs(s + nums[index2] - target)

                    if diff1 < diff2:
                        newClosestSum = s + nums[index1]
                    else:
                        newClosestSum = s + nums[index2]

                dist = abs(newClosestSum - target)
                if dist < closestDistance:
                    closestDistance = dist
                    closestSum = newClosestSum

        return closestSum


if __name__ == "__main__":
    s = Solution()
    nums = [-1,0,1,1,55]
    target = 3
    print(f"s.threeSumClosest(nums, target) = {s.threeSumClosest(nums, target)}")
