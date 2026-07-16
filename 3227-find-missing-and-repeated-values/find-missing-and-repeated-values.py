class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        freq={}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] in freq:
                    freq[grid[i][j]]+=1
                else:
                    freq[grid[i][j]]=1
        n = len(grid)
        repeated = 0
        missing = 0
        for i in range(1, n * n + 1):
            if i not in freq:
                missing = i
            elif freq[i] > 1:
                repeated = i
        return [repeated, missing]
               
        