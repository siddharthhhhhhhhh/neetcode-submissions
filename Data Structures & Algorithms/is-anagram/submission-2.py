class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        setS = set(s)
        setT = set(t)
        if len(setS) != len(setT):
            return False
            
        dict1 = {}
        dict2 = {}

        for i in range(len(s)):
            if s[i] not in dict1:
                dict1[s[i]] = 1
            else:
                dict1[s[i]] += 1

        for j in range(len(t)):
            if t[j] not in dict2:
                dict2[t[j]] = 1
            else:
                dict2[t[j]] += 1
        count = 0
        for i in dict1:
            if i in dict2:
                if dict1[i] == dict2[i]:
                    count += 1
        if len(dict1) == count:
            return True
        else:
            return False
        
        
        