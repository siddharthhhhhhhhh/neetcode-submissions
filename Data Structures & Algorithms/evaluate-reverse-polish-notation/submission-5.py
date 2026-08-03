class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        list1 = ["+", "-", "*", "/"]
        list2 = []
        for i in tokens:
            if i not in list1:
                list2.append(int(i))
            else:
                
                if i == "+":
                    pop1 = list2.pop()
                    pop2 = list2.pop()
                    res = pop2 + pop1
                    list2.append(res)
                elif i == "-":
                    pop1 = list2.pop()
                    pop2 = list2.pop()
                    res = pop2 - pop1
                    list2.append(res)
                elif i == "*":
                    pop1 = list2.pop()
                    pop2 = list2.pop()
                    res = pop2 * pop1
                    list2.append(res)
                elif i == "/":
                    pop1 = list2.pop()
                    pop2 = list2.pop()
                    if (pop2/pop1) < 0 and (pop2/pop1) != (pop2//pop1):
                        res = pop2//pop1 + 1
                    else:
                        res = pop2//pop1
                   
                    
                    list2.append(res)
        return int(list2[0])
