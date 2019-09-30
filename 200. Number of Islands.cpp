class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int ans = 0;
        if (grid.empty()) return 0;
        int m = grid.size();
        int n = grid[0].size();
        
        for (int i=0; i<m; i++){
            for (int j=0; j<n; j++){
                if (grid[i][j] == '1'){
                    dfs(grid, i, j, m, n);
                    ans++;
                }
            }
        }
        return ans;
    }
private:
    void dfs(vector<vector<char>>& grid, int i, int j, int m, int n){
         // cout << i<<", " << j << endl;
        if ( i<0 || j<0 || i>=m || j>=n || grid[i][j]=='0' ) return;
        grid[i][j] = '0';
        dfs(grid, i-1, j, m, n);
        dfs(grid, i+1, j, m, n);
        dfs(grid, i, j-1, m, n);
        dfs(grid, i, j+1, m, n);
    }
};
