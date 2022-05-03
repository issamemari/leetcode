class Solution:

    def say(self, s: str):

        res = ""

        j = 0
        while j < len(s):
            i = j
            while i < len(s) and s[i] == s[j]:
                i += 1

            res += str(i - j) + s[j]
            j += i - j

        return res

    def countAndSay(self, n: int) -> str:

        if n == 1:
            return "1"

        s = "1"
        for _ in range(n - 1):
            s = self.say(s)

        return s
