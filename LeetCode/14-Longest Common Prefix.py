from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_str = strs[0]
        index = len(first_str)
        if len(strs) == 1:
            return first_str
        while index > 0:
            common = first_str[:index]
            for s in strs[1:]:
                if common not in s[:index]:
                    break
            else:
                return common
            index -= 1
        return ''


if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["c", "acc", "ccc"]))
