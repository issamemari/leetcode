from itertools import product
from typing import List


class Solution:
    def __init__(self):
        self.dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        l = [self.dic[d] for d in digits]
        return list(map(lambda t: "".join(t), product(*l)))
