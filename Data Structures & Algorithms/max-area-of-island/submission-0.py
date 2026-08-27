class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        areag = 0
        def bfs(i, j):
            areal = 1
            q = deque()
            q.append((i, j))
            visited.add((i, j))
            while q:
                row, col = q.popleft()
                directions = [(0,1), (1,0), (-1,0), (0,-1)]
                for dr, dc in directions:
                    r = row+dr
                    c = col+dc
                    if (r in range(len(grid))) and (c in range(len(grid[0]))) and ((r,c) not in visited) and (grid[r][c] == 1):
                        areal += 1
                        visited.add((r,c))
                        q.append((r,c))
            return areal
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    areag = max(areag, bfs(i, j))
        return areag
