class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        myheap = []
        dict1 = {}
        list1 = []
        for i in points:
            res = ((i[0])**2) + ((i[1])**2)
            heapq.heappush(myheap, [-res, i])
            if len(myheap) > k:
                heapq.heappop(myheap)
        
       
        for i in myheap:
            list1.append(i[1])
        return list1
            
        