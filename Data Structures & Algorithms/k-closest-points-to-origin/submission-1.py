class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dict1 = {}
        list1 = []
        for i in points:
            distance = i[0]**2 + i[1]**2
            x = tuple(i)
            dict1[x] = distance
        sorted_dict = dict(sorted(dict1.items(), key = lambda x:x[1]))
        sorted_keys = list(sorted_dict.keys())
        for i in range(k):
            x = list(sorted_keys[i])
            list1.append(x)
        return list1
        
        