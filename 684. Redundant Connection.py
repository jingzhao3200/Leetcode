class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
        #create a parent list to store the visited
        parent = [0]*len(edges)
        
        def find(x):
            if parent[x]==0:
                return x
            return find(parent[x])
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            print('root',rootX,rootY)
            if rootX == rootY:
                return False
            # build the parent relationship
            parent[rootX] = rootY
            return True
        
        for x,y in edges:
            print(x,y)
            if not union(x-1, y-1):
                return [x, y]
        
        
