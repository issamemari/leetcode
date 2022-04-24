class Solution(object):

    def expand(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1: r]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        max_pal = ""
        max_len = -1
        for i in range(len(s)):
            pal1 = self.expand(s, i, i)
            pal2 = self.expand(s, i, i + 1)
            if len(pal1) > max_len:
                max_pal = pal1
                max_len = len(pal1)

            if len(pal2) > max_len:
                max_pal = pal2
                max_len = len(pal2)

        return max_pal
