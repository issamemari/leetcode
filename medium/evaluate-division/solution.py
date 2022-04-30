from typing import List
from collections import defaultdict


class Solution:
    def computeFromEquation(self, equation, value, query):
        if equation[0] == query[0]:
            return value
        return 1 / value

    def solveOneQuery(
        self, equations: List[List[str]], values: List[float], query: List[str],
    ):
        equationIndices1 = self.variableToEquationIndices[query[0]]
        equationIndices2 = self.variableToEquationIndices[query[1]]

        if len(equationIndices1) == 0 or len(equationIndices2) == 0:
            return -1

        if query[0] == query[1]:
            return 1

        intersection = equationIndices1.intersection(equationIndices2)
        if len(intersection) > 0:
            for equationIndex in intersection:
                return self.computeFromEquation(
                    equations[equationIndex], values[equationIndex], query
                )

        for k, indices in enumerate([equationIndices1, equationIndices2]):
            for equationIndex in indices:
                invert = False
                if k == 0 and equations[equationIndex][0] == query[0]:
                    candidate = [equations[equationIndex][1], query[1]]
                elif k == 0:
                    candidate = [query[1], equations[equationIndex][0]]
                    invert = True
                elif k == 1 and equations[equationIndex][0] == query[1]:
                    candidate = [equations[equationIndex][1], query[0]]
                    invert = True
                else:
                    candidate = [query[0], equations[equationIndex][0]]

                if tuple(candidate) in self.visitedCandidates:
                    continue

                self.visitedCandidates.add(tuple(candidate))

                comp = self.solveOneQuery(equations, values, candidate)
                if comp != -1:
                    if invert:
                        return 1 / (comp * values[equationIndex])
                    return comp * values[equationIndex]

        return -1

    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:

        self.variableToEquationIndices = defaultdict(set)
        for i, equation in enumerate(equations):
            self.variableToEquationIndices[equation[0]].add(i)
            self.variableToEquationIndices[equation[1]].add(i)

        result = []
        for query in queries:
            self.visitedCandidates = set()
            result.append(self.solveOneQuery(equations, values, query))

        return result


if __name__ == "__main__":
    equations = [["a","b"],["b","c"],["c","d"],["d","e"]]
    values = [2.0,3.0,4.0,5.0]
    queries = [
        ["c","e"],
    ]
    solution = Solution()
    print(solution.calcEquation(equations, values, queries))
