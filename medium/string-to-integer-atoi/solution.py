class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        while i < len(s) and s[i] == " ":
            i += 1

        s = s[i:]

        if len(s) == 0:
            return 0

        isPositive = True
        if s[0] == "-":
            isPositive = False
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]

        result = 0
        i = 0
        while i < len(s) and ord(s[i]) <= 57 and ord(s[i]) >= 48:
            result *= 10
            result += ord(s[i]) - 48
            i += 1

        if not isPositive:
            result *= -1

        return min(max(result, -2147483648), 2147483647)
