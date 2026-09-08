class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}
        def jump(i):
            minjumps = 1001
            if i >= len(nums)-1:
                return 0
            if nums[i] == 0:
                return 1001
            if i in memo:
                return memo[i]
            for x in range(nums[i]):
                minjumps = min(minjumps, 1+jump(i+x+1))
            memo[i] = minjumps
            return memo[i]
        return jump(0)