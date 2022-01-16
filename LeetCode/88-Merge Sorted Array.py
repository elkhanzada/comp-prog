from typing import List
import ast


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(n):
            nums1[m + i] = nums2[i]
        for i in range(m, m + n):
            key = nums1[i]
            j = i - 1
            while j >= 0 and key < nums1[j]:
                nums1[j + 1] = nums1[j]
                j -= 1
            nums1[j + 1] = key


if __name__ == '__main__':
    s = Solution()
    l1 = ast.literal_eval(input())
    l2 = ast.literal_eval(input())
    s.merge(l1, len(l1) - len(l2), l2, len(l2))
    print(l1)
