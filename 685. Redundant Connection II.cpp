class Solution {
public:
    vector<int> findRedundantDirectedConnection(vector<vector<int>>& edges) {
        
        //initialize the parents vector
        int n = edges.size();
        vector<int> parents(n+1, 0);
        vector<int> ans1;
        vector<int> ans2;
        bool dup_p = false;
        
        for (auto& edge : edges){
            int u = edge[0];
            int v = edge[1];
            
            if (parents[v] > 0){
                //v has two parents
                ans1 = {parents[v], v};
                ans2 = edge;
                edge[0] = edge[1] = -1;
                dup_p = true;
            } else {
                parents[v] = u;
            }
        }
        
        // reinitialize the parents vector
        parents = vector<int>(n+1, 0);
        for (auto& edge : edges){
            int u = edge[0];
            int v = edge[1];
            
            if (u<0 || v<0) continue;
            parents[v] = u;
            if (has_cycle(v, parents)){
                return dup_p ? ans1 : edge;
            }
        }
        return ans2;
    }
private:
    bool has_cycle(int v, vector<int>& parents){
        int pv = parents[v];
        while(pv != 0){
            if (pv == v) return true; // has cycle
            pv = parents[pv];
        }
    return false;
    }
};
