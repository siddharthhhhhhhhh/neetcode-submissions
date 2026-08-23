class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, curr = [], []
        def backtrack():
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            for i in nums:
                if i not in curr:
                    curr.append(i)
                    backtrack()
                    curr.pop()
        backtrack()
        return res     

