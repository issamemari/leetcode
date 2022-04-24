from itertools import count
from typing import List, Tuple


class Solution:

    def binarySearch(self, num: int, nums: List[int], begin: int, end: int) -> int:

        if end < begin:
            return begin

        # begin and end are inclusive boundaries
        if begin == end:
            if nums[begin] == num:
                return begin
            if nums[begin] > num:
                return begin
            return begin + 1

        mid = begin + (end - begin) // 2
        if nums[mid] == num:
            while mid < end and nums[mid] == num:
               mid += 1
            return mid
        if nums[mid] > num:
            return self.binarySearch(num, nums, begin, mid - 1)
        if nums[mid] < num:
            return self.binarySearch(num, nums, mid + 1, end)

    def findMedian(self, nums1: List[int], nums2: List[int], begin: int, end: int) -> Tuple[int, float]:
        print("===============================")
        print(f"in findMedian, nums1: {nums1}, nums2: {nums2}, begin: {begin}, end: {end}")
        if end < begin:
            print("end < begin", end, begin)
            return 0, -1

        n = len(nums1)
        m = len(nums2)

        twoMedians = True
        idxs = [(n + m) // 2 - 1, (n + m) // 2]
        if (n + m) % 2 == 1:
            twoMedians = False
            idxs = [idxs[1]]

        print(f"twoMedians is {twoMedians}, idxs: {idxs}")

        if begin == end:
            print("begin == end", begin, end)
            if (begin + self.binarySearch(nums1[begin], nums2, 0, len(nums2) - 1)) in idxs:
                print("begin + self.binarySearch(nums1[begin], nums2, 0, len(nums2) - 1) in idxs")
                return 1, nums1[begin]
            else:
                print("begin + self.binarySearch(nums1[begin], nums2, 0, len(nums2) - 1) not in idxs, median not found")
                return 0, -1

        mid = begin + (end - begin) // 2
        s = self.binarySearch(nums1[mid], nums2, 0, len(nums2) - 1)
        countUnder = mid + s
        print(f"countUnder: {countUnder}, mid: {mid}, nums1[mid]: {nums1[mid]}, s: {s}")
        if countUnder in idxs:
            print("countUnder in idxs")
            if not twoMedians:
                print("not twoMedians, return 1, {nums1[mid]}")
                return 1, nums1[mid]

            print("twoMedians, finding second median")
            f1, med1 = self.findMedian(nums1, nums2, 0, mid - 1)
            f2, med2 = self.findMedian(nums1, nums2, mid + 1, end)

            if f1 == 1 and f2 == 0:
                print("f1 == 1 and f2 == 0")
                return 2, med1
            if f1 == 0 and f2 == 1:
                print("f1 == 0 and f2 == 1")
                return 2, med2
            if f1 == 1 and f2 == 1:
                print("f1 == 1 and f2 == 1")
                return 2, (med1 + med2) / 2

            print(f"f1 == {f1} and f2 == {f2}")
            return 1, nums1[mid]
        if countUnder < idxs[0]:
            print(f"countUnder < idxs[0], countUnder: {countUnder}, idxs[0]: {idxs[0]}")
            return self.findMedian(nums1, nums2, mid + 1, end)

        print(f"countUnder > idxs[1], countUnder: {countUnder}, idxs[0]: {idxs[1]}")
        return self.findMedian(nums1, nums2, begin, mid - 1)

    def findMedianNormal(self, nums):
        if len(nums) % 2 == 1:
            return nums[len(nums) // 2]
        return (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) == 0:
            return self.findMedianNormal(nums2)
        if len(nums2) == 0:
            return self.findMedianNormal(nums1)

        count, med = self.findMedian(nums1, nums2, 0, len(nums1) - 1)
        print("AFTER FIRST FIND MEDIAN", count, med)
        if count == 2:
            return med
        if count == 1:
            count2, med2 = self.findMedian(nums2, nums1, 0, len(nums2) - 1)
            print("A AFTER SECOND FIND MEDIAN", count2, med2)
            if count2 == 2:
                return med2
            if count2 == 1:
                return (med + med2) / 2
            if count2 == 0:
                return med
        if count == 0:
            print("PARAMETERS")
            print(nums2, nums1, 0, len(nums2) - 1)
            count2, med2 = self.findMedian(nums2, nums1, 0, len(nums2) - 1)
            print("B AFTER SECOND FIND MEDIAN", count2, med2)
            return med2

if __name__ == "__main__":
    s = Solution()

    nums1 = [2, 2, 4, 4]
    nums2 = [2, 2, 4, 4]
    print(s.findMedianSortedArrays(nums1, nums2))
