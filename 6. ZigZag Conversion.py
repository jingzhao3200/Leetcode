class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows<=1:
            return s
        res = ''
        
        cycle = numRows*2 - 2
        
        for i in range(numRows):
            for j in range(i, len(s), cycle):
                res = res + s[j]
                secondJ = (j-i)+cycle-i
                if (i!=0 and i!=(numRows-1) and secondJ<len(s)):
                    res = res + s[secondJ]
        return res                    
