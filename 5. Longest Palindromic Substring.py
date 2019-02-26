class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        res = ''
        if n == 0:
            return res
        if n == 1:
            return s
        for i in range(n):
            #odd case
            temp = self.helper(s,i,i)
            # print(i, 'odd',temp)
            if len(temp)>len(res):
                res = temp
                
            #even case
            temp =self.helper(s,i,i+1)
            # print(i, 'even',temp)
            if len(temp)>len(res):
                res = temp
                
        return res
    
    def helper(self,s,l,r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1
        return s[l+1:r]
            
            
        
        
