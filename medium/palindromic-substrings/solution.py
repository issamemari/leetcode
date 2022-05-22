class Solution:
    def countSubstrings(self, s: str) -> int:

        # abaabbaa -> a b a a b b a a aba abba aabbaa aa aa bb

        count = 0
        for i in range(len(s)):

            j = 0
            while i - j >= 0 and i + j < len(s) and s[i - j] == s[i + j]:
                count += 1
                j += 1

            j = 1
            while i - j + 1 >= 0 and i + j < len(s) and s[i - j + 1] == s[i + j]:
                count += 1
                j += 1

        return count
