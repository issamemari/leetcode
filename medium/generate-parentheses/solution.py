from typing import List

class Solution:

    def __init__(self):
        self.cache = {}

    def addAtPositions(self, s: str, i: int, j: int):
        res = ""
        sPointer = 0
        resPointer = 0

        while resPointer < len(s) + 2:
            if resPointer == i:
                res += "("
            elif resPointer == j:
                res += ")"
            else:
                res += s[sPointer]
                sPointer += 1
            resPointer += 1

        return res

    def findAdditions(self, s: str):
        res = []

        i = 0
        while i < len(s) + 2:
            j = i + 1
            while j < len(s) + 2:
                res.append(self.addAtPositions(s, i, j))
                j += 2
            i += 1

        return res

    def generateParenthesis(self, n: int) -> List[str]:

        if n == 0:
            return []

        if n == 1:
            return ["()"]

        if n in self.cache:
            return self.cache[n]

        res = set()
        for i in range(1, n + 1):
            child = self.generateParenthesis(n - i)
            for x in child:
                if len(x) == (n - 1) * 2:
                    additions = self.findAdditions(x)
                    for addition in additions:
                        res.add(addition)

        res = list(res)
        self.cache[n] = res
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.generateParenthesis(4))
