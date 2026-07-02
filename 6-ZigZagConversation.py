class Solution:
    def convert(self, s: str, numRows: int) -> str:
        r = ""
        if numRows == 1:
            return s
        cycle = numRows * 2 - 2
        for i in range(0, numRows):
            for j in range(0, len(s) - i, cycle):
                r += s[j + i]
                if i != 0 and i != numRows - 1 and j + cycle - i < len(s):
                    r += s[j + cycle - i]

        return(r)
