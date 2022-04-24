class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums)
        s = {}

        count = 0
        for n in nums:
            if (n - k) in s:
                count += s[n - k]

            if n in s:
                s[n] += 1
            else:
                s[n] = 1

        return count


if __name__ == '__main__':
    s = Solution()
    print(s.countKDifference([1, 2, 3, 4, 5], 2))
