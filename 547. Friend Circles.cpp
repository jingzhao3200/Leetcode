class Solution {
public:
    int findCircleNum(vector<vector<int>>& M) {
        int ans = 0;
        int n = M.size();
        for (int i=0; i<n; i++){
            if (!M[i][i]) continue;
            dfs(M, i, n); //use dfs to find continuous region
            ans++; //increase the counter
        }
        return ans;
    }
private:
    void dfs(vector<vector<int>>& M, int curr, int n){
        for (int i=0; i<n; i++){
            if (!M[curr][i]) continue; 
            // don't forget to change the value of visited
            M[curr][i] = 0;
            M[i][curr] = 0;
            dfs(M, i, n);
        }
        
    }
};
