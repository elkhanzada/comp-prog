from typing import List
import ast


class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        rows = {}
        columns = {}
        for i in range(len(matrix)):
            rows[i] = {}
            columns[i] = {}
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                try:
                    if rows[i][matrix[i][j]] == 1 or columns[j][matrix[i][j]] == 1:
                        return False
                except:
                    rows[i][matrix[i][j]] = 1
                    columns[j][matrix[i][j]] = 1
        for i in range(len(matrix)):
            if (len(rows[i]) != len(matrix)) or len(columns[i]) != len(matrix):
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    l = ast.literal_eval(input())
    print(s.checkValid(l))
