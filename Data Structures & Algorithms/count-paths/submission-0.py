class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dfs(i,j):
            if i==m-1 and j==n-1:
                return 1
            if i>m-1 or j>n-1:
                return 0
            if (i,j) in memo:
                return memo[i,j]
            r = (0,1)
            d = (1,0)
            right = dfs(i+r[0], j+r[1])
            down = dfs(i+d[0], j+d[1])
            memo[(i,j)] = right + down
            return memo[(i,j)]
            
        return dfs(0,0)