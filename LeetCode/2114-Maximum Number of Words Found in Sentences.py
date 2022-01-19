from typing import List
import ast


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(len(sen.split()) for sen in sentences)


if __name__ == '__main__':
    s = Solution()
    print(s.mostWordsFound(ast.literal_eval(input())))
