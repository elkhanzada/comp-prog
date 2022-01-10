class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            try:
                stack = self.check(stack, s[i])
            except Exception as e:
                return False
        if len(stack) != 0:
            return False
        return True

    def check(self, arr, s1):
        if s1 == '(' or s1 == '[' or s1 == '{':
            arr.append(s1)
        else:
            if s1 == ')' and arr[len(arr) - 1] == '(':
                arr.pop()
            elif s1 == ']' and arr[len(arr) - 1] == '[':
                arr.pop()
            elif s1 == '}' and arr[len(arr) - 1] == '{':
                arr.pop()
            else:
                raise ValueError("Not Matching")
        return arr


if __name__ == '__main__':
    s = Solution()
    print(s.isValid(input()))
