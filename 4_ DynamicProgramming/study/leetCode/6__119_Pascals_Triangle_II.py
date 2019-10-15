class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        p_row = [1 for _ in range(rowIndex)]
        row = [1 for _ in range(rowIndex+1)]

        for r in range(2, rowIndex+1):
            for c in range(1, r):
                row[c] = p_row[c-1] + p_row[c]
            p_row = row[:]

        return row
