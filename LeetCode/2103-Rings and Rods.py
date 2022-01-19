class Solution:
    def countPoints(self, rings: str) -> int:
        rods = {}
        for i in range(10):
            rods[i] = []
        for i in range(0, len(rings), 2):
            if rings[i] not in rods[int(rings[i + 1])]:
                rods[int(rings[i + 1])].append(rings[i])
        count = 0
        for i in range(10):
            if len(rods[i]) == 3:
                count += 1
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.countPoints(input()))
