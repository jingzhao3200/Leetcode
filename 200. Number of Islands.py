class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        if not grid:
            return 0
        connect = 0
        m = len(grid)
        if m==0:
            return 0
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.dfs(grid,i,j)
                    res += 1
        return res
    
    def dfs(self, grid, i, j):
        m = len(grid)
        n = len(grid[0])
        if i<0 or j<0 or i>=m or j>=n or grid[i][j] == '0' or grid[i][j]=='#':
            return
        grid[i][j] = '#'
        self.dfs(grid, i-1, j)
        self.dfs(grid, i+1, j)
        self.dfs(grid, i,j-1)
        self.dfs(grid, i,j+1)
            
                
        
        
        
# not dfs sol       
#         res = 0
#         # grid[0][0]
#         connect_flag = 0
#         found_flag = 0
#         m = len(grid)
#         if m==0:
#             return 0
#         n = len(grid[0])
#         if m==1 and n==1 and grid[0][0] == '1':
#             return 1
#         # print(grid[0])
        
#         for i in range(m):
#             for j in range(n):
#                 if (grid[i][j]) == '1':
#                     if (i-1)>=0 and grid[i-1][j]== '1':
#                         found_flag = 1
#                     if (j-1)>=0 and grid[i][j-1]== '1':
#                         found_flag = 1
#                     if (j+1)<n and grid[i][j+1]== '1':
#                         found_flag = 1
#                     if (i+1)<m and grid[i+1][j]== '1':
#                         found_flag = 1
#                     if (i-1)>=0 and grid[i-1][j]== '0' and (j-1)>=0 and grid[i][j-1]== '0' and (j+1)<n and grid[i][j+1]== '0' and (i+1)<m and grid[i+1][j]== '0':
#                         found_flag = 1
#                         connect_flag = 0
                        
                        
#                 if found_flag == 1 and connect_flag ==0 and grid[i-1][j]== '0':
#                     res += 1
#                     connect_flag = 1
#                 if found_flag == 1 and connect_flag == 1:
#                     pass
#                 if found_flag == 0:
#                     connect_flag = 0
#                 print('round',i,j)
#                 print(found_flag,connect_flag,res)
#                 found_flag = 0
                
#         return res
                
