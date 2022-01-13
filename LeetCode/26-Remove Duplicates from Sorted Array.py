from typing import List
import ast


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for n in nums:
            count = -1
            for m in nums:
                if n == m:
                    count += 1
            while count > 0:
                count -= 1
                nums.remove(n)
        return len(nums)


if __name__ == '__main__':
    s = Solution()
    inps = ast.literal_eval(input())
    print(s.removeDuplicates(inps))
    print(inps)
