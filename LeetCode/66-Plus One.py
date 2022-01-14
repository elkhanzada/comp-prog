from typing import List
import ast


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[len(digits) - 1] != 9:
            digits[len(digits) - 1] += 1
            return digits
        count = -1
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                count = i
                digits[i] = 0
            else:
                break
        if count == 0:
            digits.insert(0, 1)
        else:
            digits[count - 1] += 1
        return digits


if __name__ == '__main__':
    s = Solution()
    print(s.plusOne(ast.literal_eval(input())))
