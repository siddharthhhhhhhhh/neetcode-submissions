class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize != 0:
            return False
        dict1 = Counter(hand)
        heapq.heapify(hand)
        while hand:
            a = heapq.heappop(hand)
            x = 1
            if dict1[a] != 0:
                dict1[a] -= 1
                while x < groupSize:
                    a += 1
                    if a in dict1:
                        dict1[a] -= 1
                        x += 1
                    else: return False
        return True