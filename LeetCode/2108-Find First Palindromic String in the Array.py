import ast
from typing import List
import ast


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for w in words:
            for i in range(len(w) // 2):
                if w[i] != w[len(w) - i - 1]:
                    break
            else:
                return w
        return ''


if __name__ == '__main__':
    s = Solution()
    print(s.firstPalindrome(ast.literal_eval(input())))
