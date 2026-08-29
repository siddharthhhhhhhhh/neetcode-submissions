class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dict1 = {i:[] for i in range(numCourses)}
        visited = set()
        for i,j in prerequisites:
            dict1.setdefault(i, []).append(j)
        def dfs(i):
            if i in visited:
                return False
            if dict1[i] == []:
                return True
            visited.add(i)
            for x in dict1[i]:
                if not dfs(x):
                    return False
            visited.remove(i)
            dict1[i] = [] 
            return True        
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True   


        