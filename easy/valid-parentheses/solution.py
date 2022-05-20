class Solution:
    def isValid(self, s: str) -> bool:

        opposites = {"}": "{", ")": "(", "]": "["}

        stack = []
        for c in s:

            if c in ["(", "{", "["]:
                stack.append(c)
            else:
                if len(stack) == 0 or stack[-1] != opposites[c]:
                    return False
                stack.pop()

        return len(stack) == 0
