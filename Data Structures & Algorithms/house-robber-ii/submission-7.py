class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_linear(houses: List[int]) -> int:
            prev, curr = 0, 0
            for x in houses:
                prev, curr = curr, max(curr, prev + x)
            return curr

        if len(nums) == 1:
            return nums[0]
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
