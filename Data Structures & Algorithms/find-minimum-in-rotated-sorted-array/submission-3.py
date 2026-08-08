class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            if nums[0] > nums[1]:
                return nums[1]
            else:
                return nums[0]
        if nums[0] < nums[-1]:
            return nums[0]

        left = 0
        right = len(nums) - 1
        min = 10001
        while left <= right:
            mid = (left + right)//2
            if nums[left] <= nums[mid]:
                left = mid + 1
                if nums[left]<nums[mid]:
                    return nums[left]
            elif nums[left] >= nums[mid]:
                min = nums[mid]
                right = mid -1
        return min

        
        