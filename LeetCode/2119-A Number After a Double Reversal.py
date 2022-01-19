class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return True if num % 10 != 0 or num == 0 else False

if __name__ == '__main__':
    s = Solution()
    print(s.isSameAfterReversals(int(input())))