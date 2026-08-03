class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        list1 = ["+", "-", "*", "/"]
        stack = []
        
        s = 0
        for i in tokens:
            list2 = []
            if i not in list1:
                stack.append(int(i))
            elif i in list1:
                if i == "+":
                    for i in range(2):
                        list2.append(stack.pop())
                    s = list2[1] + list2[0]
                    stack.append(s)
                elif i == "-":
                    for i in range(2):
                        list2.append(stack.pop())
                    s = list2[1] - list2[0]
                    stack.append(s)
                elif i == "*":
                    for i in range(2):
                        list2.append(stack.pop())
                    s = list2[1] * list2[0]
                    stack.append(s)
                elif i == "/":
                    for i in range(2):
                        list2.append(stack.pop())
                    if list2[1] < list2[1] or list2[0] < list2[0]:
                        s = list2[1] // list2[0]
                    elif list2[1] >= 0 and list2[0] > 0:
                        s = list2[1] // list2[0]
                    elif list2[1] < 0 or list2[0] < 0:
                        if list2[1] // list2[0] < list2[1] / list2[0]:                            
                            s = 1 + (list2[1]//list2[0]) 
                        else:
                            s = list2[1] // list2[0]

                    
                    stack.append(s)
        return stack[0]

        