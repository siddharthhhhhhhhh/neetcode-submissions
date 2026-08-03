class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        list1 = []
        if len(temperatures) == 1:
            list1.append(0)
            return list1
        for i in range(len(temperatures)-1):
            count = 0
            for j in range(i+1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    count = j - i
                    break
            list1.append(count)
        list1.append(0)
        return list1

        