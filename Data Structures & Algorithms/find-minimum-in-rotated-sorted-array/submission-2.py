class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        if nums[start]<nums[end]:
            return nums[start]
        if len(nums) == 1:
            return nums[0]
        while start<=end:
            mid = (start + end)//2
            if nums[start] <= nums[mid]:
                if start + 1 == end:
                    return nums[end]
                start = mid
            elif nums[start] >= nums[mid]:
                if (start + 1) == end:
                    return nums[end]
                end = mid 
            
        