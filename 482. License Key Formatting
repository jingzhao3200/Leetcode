class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.upper()
        S = S.replace('-', '')
        # print(S)
        res = ''
        while len(S)>K:
            n = len(S)
            subS = S[-K:]
            # print('subS', subS)
            S = S[:n-K]
            res = subS + '-' + res
            # print('res',res)
        res = S +'-'+ res
        res = res.strip('-')
        return res
