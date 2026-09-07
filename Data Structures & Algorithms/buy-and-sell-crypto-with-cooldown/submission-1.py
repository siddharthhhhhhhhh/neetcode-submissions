class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(i):
            if i>=len(prices)-1:
                return 0
            if i in memo:
                return memo[i]
            best = dfs(i+1)
            for j in range(i+1, len(prices)):
                best = max(best, dp[i][j]+dfs(j+2))
            memo[i] = best
            return best
            
                
        dp = [[-1]*(len(prices)) for _ in range(len(prices))]
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                dp[i][j] = prices[j]-prices[i]
        return dfs(0)