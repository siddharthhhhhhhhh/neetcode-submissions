class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        list1 = Counter(s)
        list2 = []
        i = 0
        while i < len(s):
            visited = set()
            x = 0
            j = i
            while j < len(s):
                visited.add(s[j])
                list1[s[j]] -= 1
                if list1[s[j]] == 0:
                    x += 1
                if x == len(visited):
                    list2.append(j-i+1)
                    i = j+1
                    break
                j += 1
        return list2       
                    
                