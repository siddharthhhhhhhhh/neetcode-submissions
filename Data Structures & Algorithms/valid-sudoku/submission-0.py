class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        listr = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != "." and board[i][j] in listr:
                    return False
                else: 
                    listr.append(board[i][j])
            listr = []
        listc = []   
        for i in range(9):
            for j in range(9):
                if board[j][i] != "." and board[j][i] in listc:
                    return False
                else:
                    listc.append(board[j][i])
            listc = []
        listm = []
        for i in range(9):
            for j in range(3):
                for k in range(3):
                    row = 3*(i%3) + k
                    column = 3*(i//3) + j
                    if board[row][column] != "." and board[row][column] in listm:
                        return False
                    else:
                        listm.append(board[row][column])
            listm = []
        return True
        