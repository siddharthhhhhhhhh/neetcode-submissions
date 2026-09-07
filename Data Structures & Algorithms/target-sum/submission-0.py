class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(i, val):
            if val == target and i == len(nums):
                return 1
            if i >= len(nums):
                return 0
            if i == -1:
                i += 1
            if (i,val) in memo:
                return memo[(i,val)]
            val1 = val + nums[i]
            val2 = val - nums[i]
            a = dfs(i+1, val1)
            b = dfs(i+1, val2)
            memo[(i, val)] = a + b
            return memo[(i,val)]
        return dfs(-1,0)
            