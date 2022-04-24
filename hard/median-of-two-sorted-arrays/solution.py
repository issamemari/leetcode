from typing import List


class Solution:

    def whereInCombined(self, index: int, nums1: List[int], num2: List[int], first: bool) -> int:
        if first:
            return index + self.binarySearch(nums1[index], num2, 0, len(num2) - 1, True)
        return index + self.binarySearch(nums1[index], num2, 0, len(num2) - 1, False)

    def binarySearch(self, num: int, nums: List[int], begin: int, end: int, return_first: bool) -> int:
        if end < begin:
            return begin

        if begin == end:
            if nums[begin] == num:
                if return_first:
                    while begin - 1 >= 0 and nums[begin - 1] == num:
                        begin -= 1
                    return begin
                while begin + 1< len(nums) and nums[begin + 1] == num:
                    begin += 1
                return begin
            if nums[begin] > num:
                return begin
            return begin + 1

        mid = begin + (end - begin) // 2
        if nums[mid] == num:
            if not return_first:
                while mid + 1 < len(nums) and nums[mid + 1] == num:
                    mid += 1
                return mid + 1
            while mid - 1 >= 0 and nums[mid - 1] == num:
                mid -= 1
            return mid
        if nums[mid] > num:
            return self.binarySearch(num, nums, begin, mid - 1, return_first)
        if nums[mid] < num:
            return self.binarySearch(num, nums, mid + 1, end, return_first)


    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) == 0:
            return self.findMedianNormal(nums2)
        if len(nums2) == 0:
            return self.findMedianNormal(nums1)

        n = len(nums1)
        m = len(nums2)

        twoMedians = False
        if (n + m) % 2 == 0:
            twoMedians = True

        meds = []
        if twoMedians:
            med1 = self.findMedian(nums1, nums2, 0, len(nums1) - 1, True, True)
            med2 = self.findMedian(nums1, nums2, 0, len(nums1) - 1, False, True)
            med3 = self.findMedian(nums2, nums1, 0, len(nums2) - 1, True, False)
            med4 = self.findMedian(nums2, nums1, 0, len(nums2) - 1, False, False)

            meds.extend([med1, med2, med3, med4])
        else:
            med1 = self.findMedian(nums1, nums2, 0, len(nums1) - 1, True, True)
            med2 = self.findMedian(nums2, nums1, 0, len(nums2) - 1, True, False)
            meds.extend([med1, med2])

        sum = 0
        count = 0
        for med in set(meds):
            if med is not None:
                sum += med
                count += 1
        return sum / count

    def findMedianNormal(self, nums: List[int]) -> float:
        if len(nums) % 2 == 1:
            return nums[len(nums) // 2]
        return (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2

    def findMedian(self, nums1: List[int], nums2: List[int], begin: int, end: int, return_first: bool, one_first: bool) -> float:
        if end < begin:
            return None

        n = len(nums1)
        m = len(nums2)

        if (n + m) % 2 == 0:
            if return_first:
                index = (n + m) // 2 - 1
            else:
                index = (n + m) // 2
        else:
            index = (n + m) // 2

        if begin == end:
            indexInCombined = self.whereInCombined(begin, nums1, nums2, one_first)
            if indexInCombined == index:
                return nums1[begin]
            return None

        mid = begin + (end - begin) // 2

        indexInCombined = self.whereInCombined(mid, nums1, nums2, one_first)
        if indexInCombined == index:
            return nums1[mid]
        if indexInCombined < index:
            return self.findMedian(nums1, nums2, mid + 1, end, return_first, one_first)
        return self.findMedian(nums1, nums2, begin, mid - 1, return_first, one_first)

if __name__ == "__main__":
    s = Solution()
    print(s.findMedianSortedArrays([1, 3], [2]))
