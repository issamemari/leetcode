class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        start = 0

        max_count = -1
        prev_start = -1
        while prev_start != start:
            prev_start = start
            seen = {}
            count = 0
            i = start
            while i < len(s):
                if s[i] in seen:
                    break

                seen[s[i]] = i
                count += 1
                i += 1

            if count >= max_count:
                max_count = count

            if i == len(s):
                break

            start = seen[s[i]] + 1

        return max_count


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("pwwkew"))
