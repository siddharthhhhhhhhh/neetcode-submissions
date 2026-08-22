class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def backtrack(i):
            if i == len(nums):
                res.append(subset.copy())
                return
            backtrack(i+1)

            subset.append(nums[i])
            backtrack(i+1)
            subset.pop()
        backtrack(0)
        return res

            


        