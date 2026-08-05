class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        dict1 = {}
        for i in range(len(position)):
            dict1[position[i]] = speed[i]
        position.sort()
        rem_dis = []
        for i in range(len(position)):
            x = target - position[i]
            rem_dis.append(x)
        rate = []
        for i in range(len(rem_dis)):
            y = rem_dis[i]/dict1[position[i]]
            rate.append(y)
        z = rate.pop()
        maxval = z
        count = 1
        while rate:
            p = rate.pop()
            if p <= maxval:
                continue
            else:
                maxval = p
                count += 1
        return count
          


        
        