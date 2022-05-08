class Solution:

    def removeDuplicateLetters(self, s: str) -> str:
        lastOccurrence = {}

        for i in range(len(s)):
            lastOccurrence[s[i]] = i

        stackSet = set()
        stack = []

        for i in range(len(s)):

            if s[i] not in stackSet:

                while stack and stack[-1] > s[i] and lastOccurrence[stack[-1]] > i:
                    stackSet.remove(stack.pop())

                stack.append(s[i])
                stackSet.add(s[i])

        return "".join(stack)


if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicateLetters("bcabc"))
