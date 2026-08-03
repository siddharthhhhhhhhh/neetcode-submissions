class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        curr = 0
        while i < j:            
            if heights[i] > heights[j]:
                volume = heights[j] * (j-i)
                curr = max(curr, volume)
                j = j-1
            else:
                volume = heights[i] * (j-i)
                curr = max(curr, volume)
                i = i+1
        return curr 
        