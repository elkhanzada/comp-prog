class Solution:
    def checkString(self, s: str) -> bool:
        if 'ba' in s:
            return False
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.checkString(input()))