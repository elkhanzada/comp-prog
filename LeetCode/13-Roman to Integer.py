class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        for i, ch in enumerate(s):
            if ch == 'M':
                sum += 1000
            elif ch == 'D':
                sum += 500
            elif ch == 'C':
                if i + 1 < len(s) and s[i + 1] in ['D', 'M']:
                    sum -= 100
                else:
                    sum += 100
            elif ch == 'L':
                sum += 50
            elif ch == 'X':
                if i + 1 < len(s) and s[i + 1] in ['L', 'C']:
                    sum -= 10
                else:
                    sum += 10
            elif ch == 'V':
                sum += 5
            elif ch == 'I':
                if i + 1 < len(s) and s[i + 1] in ['V', 'X']:
                    sum -= 1
                else:
                    sum += 1
        return sum

if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt("MCMXCIV"))