class Solution(object):
    def getConcatenation(self, nums):
        ans=[]

        for n in nums:
            ans.append(n)

        for n in nums:
            ans.append(n)
        return ans

Answer=Solution()
print(Answer.getConcatenation([1,2,3]))