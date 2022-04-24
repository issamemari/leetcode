class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            return -1 * self.reverse(-1 * x)

        result = 0
        while x:
            digit = x % 10
            x = x // 10

            if result > 214748364 or (
                result == 214748364 and digit > 7
            ):
                return 0

            result *= 10
            result += digit

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.reverse(1534236469))
