class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        myheap = []
        for i in nums:
            heapq.heappush(myheap, i)
            if len(myheap) > k:
                heapq.heappop(myheap)
        return myheap[0]
        