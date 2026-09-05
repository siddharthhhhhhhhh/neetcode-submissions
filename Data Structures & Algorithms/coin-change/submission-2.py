class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        memo = {}
        def backtrack(i, total):
            if total == amount:
                return 0
            if total > amount:
                return 10000
            if (i, total) in memo:
                return memo[(i,total)]
            minx = 10000
            for x in range(i, len(coins)):
                b =  1 + backtrack(x, total+coins[x]) 
                minx = min(minx, b)
            memo[(i, total)] = minx
            return minx

        x = backtrack(0, 0) 
        if x == 10000:
            return -1
        else: return x 
