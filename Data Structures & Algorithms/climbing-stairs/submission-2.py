class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(step):
            if step == n:
                return 1
            elif step > n:
                return 0
            if step in memo:
                return memo[step]
            memo[step] = dfs(step+1) + dfs(step+2)
            return memo[step]
        final = dfs(0)
        return final