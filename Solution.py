class Solution:
    def isAnagram(self, s, t):
        if sorted(s)==sorted(t):
            return True
        return False
s,t="mom","omm"
obj=Solution()
print(obj.isAnagram(s,t))