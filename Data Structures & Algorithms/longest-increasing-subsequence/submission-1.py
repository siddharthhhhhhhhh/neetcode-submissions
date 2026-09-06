class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []
        for i in nums:
            lo = 0
            hi = len(tails)
            while lo < hi:
                mid = (lo+hi)//2
                if tails[mid] < i:
                    lo = mid+1
                if tails[mid] >= i:
                    hi = mid
            if lo == len(tails):
                tails.append(i)
            else: tails[lo] = i
        return len(tails)

            

        