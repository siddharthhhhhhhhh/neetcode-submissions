class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if 0 in nums:
            count = 1
            list1 = []
            zerocheck = Counter(nums)
      
            if zerocheck[0] == len(nums):
                return nums
            elif zerocheck[0]>1:
                return [0]*len(nums)

            for i in nums:
                if i != 0:
                    count = count * i
            for i in nums:
                if i != 0:
                    list1.append(0)
                else:
                    list1.append(count)
            return list1 
        else:
            count = 1
            for i in nums:
                count = count * i
            list1 = []
            for i in nums:
                list1.append(int(count/i))
            return list1
                

        