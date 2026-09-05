class Solution:
    def numDecodings(self, s: str) -> int:
        count = 0
        list1 = []
        if int(s[0]) == 0:
            return 0
        ns = ''
        memo = {}
        for i in range(len(s)):
            if i in range(len(s)-1):
                if s[i+1] == '0':
                    ns = ns+s[i]+'0'
                    continue
            if s[i] == '0':
                continue
            ns += s[i]
        if len(ns) == 1:
            return 1
        if len(ns) ==2 and ns[1] == '0':
            return 1
        def backtrack(i):
            if i == len(ns):
                return 1
            if ns[i] == '0':
                return 0
            if i in memo:              # <-- ADD THIS: check cache first
                return memo[i]
            ways = backtrack(i+1)
            if i + 1 < len(ns) and int(ns[i:i+2]) <= 26:
                ways += backtrack(i + 2)  

            memo[i] = ways
            return ways
        
        return backtrack(0)
        
        