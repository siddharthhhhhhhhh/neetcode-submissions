class Solution:
    def isPalindrome(self, s: str) -> bool:
        count = 0
        list1 = []
        for i in range(len(s)):
            if s[i].isalpha():
               list1.append(s[i].lower())
            elif s[i].isnumeric():
                list1.append(s[i])
        if len(list1)%2 == 0:
            for i in range(int(len(list1)/2)):
                if list1[i] == list1[len(list1)-1-i]:
                    count += 1
           
            if count == len(list1)/2:
                return True
            else:
                return False

        elif len(list1)%2 == 1:
            
            for i in range(int(len(list1)//2)):
                if i == int(len(list1)//2) :
                    break
                elif list1[i] == list1[len(list1)-1-i]:
                    count += 1
            if count == len(list1)//2:
                return True
            else:
                return False

        