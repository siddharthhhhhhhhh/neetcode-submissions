class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def backtrack(i, curr):
            if i == len(nums):
                res.append(curr[:])
                return
            curr.append(nums[i])
            backtrack(i+1, curr)
            curr.pop()
            j = i + 1
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            backtrack(j, curr)
        backtrack(0, [])
        return res

        