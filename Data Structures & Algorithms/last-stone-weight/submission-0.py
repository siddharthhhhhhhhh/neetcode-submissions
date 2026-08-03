class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            count = 0
            stones.sort()
            if len(stones) > 1:

                for j in range(2):
                    if j == 0:
                        count = count + stones.pop()
                    elif j == 1:
                        count = count - stones.pop()
                stones.append(count)
        return stones[0]
                
        