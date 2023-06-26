from typing import List

class Solution:

    def completeParanthesis(self, s: str, n: int, count_open: int, count_closed: int) -> List[str]:
        if count_open == n:
            return [s + ")" * (n - count_closed)]

        c1 = []
        if count_closed < count_open:
            c1 = self.completeParanthesis(s + ")", n, count_open, count_closed + 1)

        c2 = self.completeParanthesis(s + "(", n, count_open + 1, count_closed)

        return c1 + c2

    def generateParenthesis(self, n: int) -> List[str]:
        return self.completeParanthesis("", n, 0, 0)
