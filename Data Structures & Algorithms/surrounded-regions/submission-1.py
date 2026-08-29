class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        def bfs(i,j):
            list1 = []
            status = True
            q = deque()         
            q.append((i,j))
            visited.add((i,j))
            list1.append([i,j])
            directions = [(0,1), (1,0), (-1,0), (0,-1)]
            while q:           
                row, col = q.popleft()
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if (r not in range(len(board))) or (c not in range(len(board[0]))):
                        status = False
                    elif (r in range(len(board))) and (c in range(len(board[0]))) and ((r,c) not in visited) and board[r][c] == "O":
                        visited.add((r,c))
                        list1.append([r,c])
                        q.append((r,c))
            if status == True:
                for i,j in list1:
                    board[i][j] = "X"
       
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and (i,j) not in visited:
                    bfs(i,j)
        
        