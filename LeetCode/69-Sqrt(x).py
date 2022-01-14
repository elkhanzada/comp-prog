import math


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        delta = math.inf
        num = -1
        for i in range(1, x):
            if i * i > x:
                break
            temp = x - i * i
            if delta > temp:
                delta = temp
                num = i
        return num


if __name__ == '__main__':
    s = Solution()
    print(s.mySqrt(int(input())))
