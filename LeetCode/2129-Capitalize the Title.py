class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split()
        newstr = ''
        for w in words:
            if len(w) < 3:
                newstr += w.lower()
            else:
                temp = w.lower()
                newstr += temp[0].upper() + temp[1:]
            newstr += ' '
        newstr = newstr[:-1] if newstr[-1] == ' ' else newstr
        return newstr


if __name__ == '__main__':
    s = Solution()
    print(s.capitalizeTitle(input()))
