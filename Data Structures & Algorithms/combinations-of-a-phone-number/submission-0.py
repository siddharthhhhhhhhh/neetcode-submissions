class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict1 = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4":["g", "h", "i"], "5": ["j", "k", "l"],"6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        res, sol = [], ""
        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            return dict1[digits[0]]
        def backtrack(i, sol):
            if len(sol) == len(digits):
                res.append(sol)
                return
            for letter in dict1[digits[i]]:
                backtrack(i+1, sol + letter)
        backtrack(0, "")
        return res




        