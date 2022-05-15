from functools import lru_cache


class Solution:

    @lru_cache(None)
    def numDecodings(self, s: str) -> int:
        if s.startswith("0"):
            return 0

        if len(s) == 1:
            return 1

        if len(s) == 2:
            if s < "11":
                return 1

            res = 0
            if s > "26":
                res = 1
            else:
                res = 2

            if s[-1] == "0":
                return res - 1

            return res

        n1 = self.numDecodings(s[1:])
        n2 = self.numDecodings(s[2:]) if s[:2] <= "26" else 0

        return n1 + n2
