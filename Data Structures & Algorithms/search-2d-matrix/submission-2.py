class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        f_ind = []
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        else:
            for i in range(len(matrix)):
                if target >= matrix[i][0] and target <= matrix[i][-1]:
                    f_ind.append(i)
        if len(f_ind) == 0:
            return False
        left = 0
        right = len(matrix[f_ind[0]])-1
        for i in range(len(matrix[f_ind[0]])):
            mid = (left + right)//2
            if matrix[f_ind[0]][mid] > target:
                right = mid -1
            elif matrix[f_ind[0]][mid] < target:
                left = mid + 1
            elif matrix[f_ind[0]][mid] == target:
                return True
        return False
