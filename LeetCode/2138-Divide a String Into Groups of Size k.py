from typing import List


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        group_list = []
        for i in range(0, len(s), k):
            if i + k <= len(s):
                group_list.append(s[i:i + k])
            else:
                group_list.append(s[i:len(s)])
        for i in range(k - len(group_list[-1])):
            group_list[-1] += fill
        return group_list


if __name__ == '__main__':
    s = Solution()
    print(s.divideString(input(), int(input()), input()))
