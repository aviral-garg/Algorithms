class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        if numRows == 0:
            return []

        tri = [[1]*(i+1) for i in range(numRows)]

        for r in range(1, numRows):
            for c in range(1, r):
                tri[r][c] = tri[r-1][c-1] + tri[r-1][c]

        return tri
