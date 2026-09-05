class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        left = 1
        right = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                left = 0
            else:
                left = left*nums[i]
            if nums[len(nums)-i-1] == 0:
                right = 0
            else:
                right = right*nums[len(nums)-i-1]
            ans = max(ans, left, right)
            if nums[i] == 0:
                left = 1
            if nums[len(nums)-i-1] == 0:
                right = 1
        return ans
            
