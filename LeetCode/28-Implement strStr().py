class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '' or needle == haystack:
            return 0
        for i in range(len(haystack)):
            if i + len(needle) > len(haystack):
                return -1
            news = haystack[i:i + len(needle)]
            if news == needle:
                return i

        return -1


if __name__ == '__main__':
    hay = input()
    need = input()
    s = Solution()
    print(s.strStr(hay, need))
