class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        if matrix[-1][-1] < target:
            return False
        for i in matrix:

            if len(matrix) == 0:
                return False
            
            elif i[-1] < target:
                row += 1
            
        start = 0
        end = len(matrix[row])-1
        

        while start <= end:
            mid = (start + end)//2
            if matrix[row][mid] < target:
                start = mid + 1
            elif matrix[row][mid] > target:
                end = mid - 1
            elif matrix[row][mid] == target:
                return True
        return False


            


        