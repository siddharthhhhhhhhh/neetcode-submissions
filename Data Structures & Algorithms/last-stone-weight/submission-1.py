class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in stones:
            heapq.heappush(heap, -i)
        while len(heap) > 1:
            count = 0
            for i in range(2):
                if i == 0:
                    count = count + heapq.heappop(heap)
                elif i == 1:
                    count = count - heapq.heappop(heap)
            heapq.heappush(heap, count)
        if len(heap) == 1:
            return -heap[0]

        
                
        