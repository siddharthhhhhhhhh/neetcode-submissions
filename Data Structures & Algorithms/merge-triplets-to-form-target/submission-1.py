class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        maxi = [0, 0, 0]
        for i in range(len(triplets)):
            if triplets[i][0] > target[0] or triplets[i][1] > target[1] or triplets[i][2] > target[2]:
                continue
            for j in range(3):
                maxi[j] = max(maxi[j], triplets[i][j])
        if target == maxi:
            return True
        else: return False
                    