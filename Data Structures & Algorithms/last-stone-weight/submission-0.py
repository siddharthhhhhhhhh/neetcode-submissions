class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        list1 = []
        for i in stones:
            list1.append(-i)
        while len(list1) > 1:
            res = 0
            for i in range(2):
                heapq.heapify(list1)
                if i == 0:
                    res += heapq.heappop(list1)
                else:
                    res -= heapq.heappop(list1)
            heapq.heappush(list1, res)
        return -list1[0]

        