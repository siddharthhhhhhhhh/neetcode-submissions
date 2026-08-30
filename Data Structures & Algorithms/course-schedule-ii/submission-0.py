class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dict1 = {i:[] for i in range(numCourses)}
        list1 = deque()
        for i,j in prerequisites:
            dict1[i].append(j)
        visited = set()
        def dfs(i):
            if i in visited:
                return False
            if dict1[i] == []:
                if i not in list1:
                    list1.append(i)
                return True
            visited.add(i)
            for x in dict1[i]:
                if not dfs(x):
                    return False
            if i not in list1:
                list1.append(i)
            visited.remove(i)
            dict1[i] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return list(list1)
        