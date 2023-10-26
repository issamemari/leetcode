class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        begin = 1
        end = x // 2 + 1
        while end - begin > 0:
            mid = begin + (end - begin) // 2
            if mid * mid == x:
                return mid

            if mid * mid < x:
                begin = mid + 1
            else:
                end = mid

        return end - 1
