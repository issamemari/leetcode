from typing import List


class Solution:
    def longestCommonPrefix(self, strings: List[str]) -> str:

        # find the shortest string in the list:
        shortestLength = 500
        shortestStringIndex = -1
        for i, s in enumerate(strings):
            if len(s) < shortestLength:
                shortestLength = len(s)
                shortestStringIndex = i

        if shortestStringIndex == -1:
            return ""

        shortestString = strings[shortestStringIndex]

        for i in range(len(shortestString), -1, -1):
            prefix = shortestString[:i]

            # check if prefix is also a prefix of all the other strings in the list
            isPrefixInAll = True
            for s in strings:
                if s[:i] != prefix:
                    isPrefixInAll = False
                    break

            if isPrefixInAll:
                return prefix

        return ""
