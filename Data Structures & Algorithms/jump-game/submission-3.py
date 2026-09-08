class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}
        def jump(i):
            if i == len(nums)-1:
                return True
            if i > len(nums)-1:
                return False
            if nums[i] == 0:
                return False
            if i in memo:
                return memo[i]
            for x in range(nums[i]):
                if jump(i+1+x):
                    memo[i] = True
                    return memo[i]
            memo[i] = False
            return memo[i]
        return jump(0)
                
        