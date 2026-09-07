class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def backtrack(i, val):
            if val > amount or i == len(coins):
                return 0
            if val == amount:
                return 1
            if (i,val) in memo:
                return memo[(i,val)]
            if i == -1:
                i += 1
            a = backtrack(i, val+coins[i])            
            b = backtrack(i+1, val)
            memo[(i,val)] = a+b
            return memo[(i,val)]
        return backtrack(-1,0)