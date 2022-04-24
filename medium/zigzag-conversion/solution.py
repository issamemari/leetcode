class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = ""

        if len(s) == 1 or numRows == 1:
            return s

        for i in range(numRows):

            period1 = 2 * numRows - 2
            period2 = period1 - i * 2

            if period2 == 0 or period2 == period1:
                index = i
                while index < len(s):
                    res += s[index]
                    index += period1

                continue

            index = i
            c = 0
            while index < len(s):
                res += s[index]

                if c % 2 == 0:
                    period = period2
                else:
                    period = period1 - period2
                index += period

                c += 1

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.convert("A", 1))
