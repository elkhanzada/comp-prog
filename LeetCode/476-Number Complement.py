class Solution:
    def findComplement(self, num: int) -> int:
        bistr = ""
        while num != 0:
            r = num % 2
            bistr += '1' if r == 0 else '0'
            num = num // 2
        output = 0
        for i, x in enumerate(bistr):
            output += int(pow(2, i)) * int(bistr[i])
        return output


if __name__ == '__main__':
    s = Solution()
    print(s.findComplement(int(input("num = "))))
