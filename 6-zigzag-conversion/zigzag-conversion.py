class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        res = [''] * numRows
        cr, d = 0, -1
        for char in s:
            res[cr] += char
            if cr == 0 or cr == numRows - 1:
                d = d*(-1)
            cr += d
        return ''.join(res)
        