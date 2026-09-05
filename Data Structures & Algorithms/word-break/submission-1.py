class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def backtrack(i):
            if i == len(s):
                return True
            if i in memo:
                return memo[i]
            for end in range(i+1, len(s)+1):
                if s[i:end] in wordDict and backtrack(end):
                    memo[i] = True
                    return True
            memo[i] = False
            return False
        return backtrack(0)
