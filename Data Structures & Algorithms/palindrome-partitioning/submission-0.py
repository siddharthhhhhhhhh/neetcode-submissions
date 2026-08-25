class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        sol = []
        def isPalindrome(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i, j = i+1, j-1
            return True
        def backtrack(i):
            if i == len(s):
                res.append(sol[:])
            for j in range(i, len(s)):
                if isPalindrome(s, i, j):
                    sol.append(s[i:j+1])
                    backtrack(j+1)
                    sol.pop()
        backtrack(0)
        return res
        

            
