class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        minutes = 0
        count = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count += 1
                if grid[i][j] == 2:
                    q.append((i,j))
        if len(q) == 0 and count != 0:
            return -1
        while q:
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if (r in range(len(grid))) and (c in range(len(grid[0]))) and ((r, c) not in visited) and grid[r][c] == 1:
                        grid[i][j] == 2
                        count -= 1
                        q.append((r, c))
                        visited.add((r, c))
                
            if len(q) == 0 and count != 0:
                minutes =  -1
            elif len(q) != 0:
                minutes += 1
                
                
                
        return minutes
