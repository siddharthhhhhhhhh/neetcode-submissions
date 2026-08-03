class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list2 = []
        list3 = []
        if len(strs) == 1 or len(strs) == 0:
            list2.append(strs)
            return list2
        
        for i in range(len(strs)):
            list1 = []
            if strs[i] not in list3:
                
                list1.append(strs[i])
                list3.append(strs[i])
                if i == len(strs):
                    list2.append(list1)
                    break
                
                dict1 = {}
                for w in range(len(strs[i])):
                    if strs[i][w] not in dict1:
                        dict1[strs[i][w]] = 1
                    else:
                        dict1[strs[i][w]] += 1
                
                for j in range(i+1, len(strs)):
                    dict2 = {}
                    for w in range(len(strs[j])):
                        if strs[j][w] not in dict2:
                            dict2[strs[j][w]] = 1
                        else:
                            dict2[strs[j][w]] += 1
                    count = 0
                    for k in dict1:
                        if k in dict2 and dict1[k] == dict2[k]:
                            count += 1
                    if count == len(dict1) and count == len(dict2):
                        list1.append(strs[j])
                        list3.append(strs[j])
                list2.append(list1)
        return list2            

        