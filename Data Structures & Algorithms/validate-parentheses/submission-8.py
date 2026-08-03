class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        dict1 = {"[": "]", "(": ")", "{": "}"}
        list1 = []
        for i in range(len(s)):
            if s[i] in dict1:
                list1.append(s[i])
            else:
                list1.append(s[i])
                x = list1.pop()
                if len(list1) != 0 and x == dict1[list1[-1]]:
                    list1.pop()
                else: 
                    return False
        if len(list1) == 0:
            return True
        else:
            return False


        