import ast
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)


if __name__ == '__main__':
    s = Solution()
    inps = ast.literal_eval(input())
    myval = int(input())
    print(s.removeElement(inps, myval))
    print(inps)
