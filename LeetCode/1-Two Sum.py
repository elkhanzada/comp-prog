from typing import List
from ast import literal_eval


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


if __name__ == '__main__':
    s = Solution()
    nums = literal_eval((input()))
    target = int(input())
    print(s.twoSum(nums, target))
