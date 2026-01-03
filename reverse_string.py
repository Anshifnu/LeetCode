class Solution(object):
    def reverseString(self, s):
        left=0
        right=len(s)-1
        while left < right:
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1

P=["H","a","n","n","a","h"]
Reverse=Solution()
Reverse.reverseString(P)
print(P)





