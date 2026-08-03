class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        i = 0
        j = i + 1
        list1 = []
        list1.append(s[0])
        curr = 1
        
        while i < j:
            if j <= len(s)-1:
                if s[j] not in list1:
                    list1.append(s[j])
                    j = j + 1
                    curr = max(curr, len(list1))
                
                else:
                    
                    if j <= len(s)-1:
                        list1.append(s[j])
                        if len(list1) > 1:
                            
                            x = list1.index(s[j])
                            list1 = list1[(x+1):]
                            i = x+1
                            j = j + 1
                        else:
                            continue
                    else:
                        break
            else:
                break
        return curr  


        