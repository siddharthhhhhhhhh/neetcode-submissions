class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = []
        rows, cols = len(board), len(board[0])
        visited = set()
        def backtrack(i, j, count):
            if count == len(word):
                return True
            if (i < 0 or i >= rows or j < 0 or j >= cols or (i, j) in visited or    board[i][j] != word[count]):
                return False
            visited.add((i, j))
            result = (backtrack(i+1, j, count+1) or
                    backtrack(i-1, j, count+1) or
                    backtrack(i, j+1, count+1) or
                    backtrack(i, j-1, count+1))
            visited.remove((i, j))
            return result

        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, 0):
                    return True
        return False
            