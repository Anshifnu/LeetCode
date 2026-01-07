class Solution(object):
    def averageValue(self, nums):
        valid=[]
        average=0
        for num in nums:
            if num%2==0 and num % 3==0:
                valid.append(num)

        if len(valid)==0:
            return 0
        
        for num in valid:
            average+=num

        return average//len(valid)
    
Answer=Solution()
print(Answer.averageValue([1,2,3,4,5,6,7,8,12]))

        