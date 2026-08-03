class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        lowest = 0
        ind = 0
        if nums[start]<nums[end]:
            lowest = nums[start]
        if len(nums) == 1:
            lowest = nums[0]
        elif len(nums) > 1:

            while start<=end:
                mid = (start + end)//2
                if nums[start] <= nums[mid]:
                    if start + 1 == end:
                        lowest = nums[end]
                        ind = end
                        break
                    start = mid
                elif nums[start] >= nums[mid]:
                    if (start + 1) == end:
                        lowest = nums[end]
                        ind = end
                        break
                    end = mid 
        count = 0
        if target >= lowest:
            l = ind
            r = len(nums) - 1

            while l<=r:
                mid = (l+r)//2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] == target:
                    count += 1
                    return mid
                elif nums[mid] > target:
                    r = mid - 1
        if count ==0 :
            l = 0
            r = ind-1

            while l<=r:
                mid = (l+r)//2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid - 1
        return -1