class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 0
        new_set = len(set(nums))
        while j < len(nums)-1:
            if nums[i] == nums[j+1]:
                j += 1
            else:
                nums[i+1] = nums[j+1]
                i += 1
                j += 1
        nums = nums[:new_set]
        return len(nums)