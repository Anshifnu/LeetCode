# Given two strings s and t, return true if t is an anagram of s, and false otherwise.


# 1.Logic method
class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        
        count={}

        for char in s:
            count[char]=count.get(char,0)+1

        for char in t:
            if char not in count:
                return False
            count[char]-=1
            if count[char]<0:
                return False

        return True

anagram=Solution()

        
# 2.short way (using methods)

def anagram(s,t):
    return sorted(s)==sorted(t)

print(anagram("acc", "cac"))
