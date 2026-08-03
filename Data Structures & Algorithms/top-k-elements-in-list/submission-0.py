
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        list1 = []
        counts = Counter(nums)
        mostfreq = counts.most_common(k)
        for i in mostfreq:
            list1.append(i[0])
        return list1  
       
        