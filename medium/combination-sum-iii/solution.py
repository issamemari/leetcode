class Solution:

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        stack = [([], 0)]

        while stack:

            current_combination, current_sum = stack.pop()

            if len(current_combination) == k and current_sum == n:
                res.append(current_combination)
                continue

            if len(current_combination) != k and current_sum < n:
                low = 0
                if len(current_combination) > 0:
                    low = current_combination[-1]

                for i in range(low + 1, min(10, n - current_sum + 1)):
                    stack.append((current_combination + [i], current_sum + i))

        return res
