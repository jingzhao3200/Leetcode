class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        
        m = len(board)
        n = len(board[0])
        
        for i in range(m):
            for j in range(n):
                if self.dfs(board, word, i, j):
                    return True
        return False
    
    def dfs(self, board, word, i, j):
        
        if len(word)==0:
            return True
        if len(board)==1 and len(board[0])==1:
            if board[0][0]==word:
                return True
        # print(i,j)
        if board[i][j] == word[0]:
            temp = board[i][j]
            board[i][j] = '#' #indicate has been checked
            
            m = len(board)
            n = len(board[0])
            
            #check four direction if next word char exist
            if (i-1)>=0 and self.dfs(board, word[1:], i-1, j):
                return True
            if (i+1)<m and self.dfs(board, word[1:], i+1, j):
                return True
            if (j-1)>=0 and self.dfs(board, word[1:], i, j-1):
                return True
            if (j+1)<n and self.dfs(board, word[1:], i, j+1):
                return True
            board[i][j] = temp #restore after checked
            
            return False
        
            
        else:
            return False
            
            
