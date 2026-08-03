class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = i+1
        curr = 0
        if len(prices) == 1:
            return 0
        while i < j:
            if prices[i] < prices[j]:
                profit = prices[j] - prices[i]
                curr = max(curr, profit)
                if j == len(prices) - 1:
                    break
                else:
                    j += 1
            else:
                if j == len(prices)-1:
                    break
                else:
                    i = j
                    j += 1
        return curr
        