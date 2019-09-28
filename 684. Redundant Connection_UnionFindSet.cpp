class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        UnionFindSet s(edges.size());
        for (const auto& edge : edges){
            int u = edge[0];
            int v = edge[1];
            if (s.Union(u,v) == false)
                return edge;
        }
        return {};
    }

    
    
class UnionFindSet{
private:
     vector<int> parents_;
     vector<int> ranks_;
    
public:
    UnionFindSet(int n){
        ranks_ = vector<int>(n+1, 0);
        parents_ = vector<int>(n+1, 0);
        
        for (int i=0; i<parents_.size(); ++i){
            parents_[i] = i;
        }     
    }
    
    // Merge sets that contains u and v.
    // Return true if merged, false if u and v are already in one set.
    bool Union(int u, int v){
        int pu = Find(u);
        int pv = Find(v);
        if (pu == pv) return false;
        // Meger low rank tree into high rank tree
        if (ranks_[pu] > ranks_[pv]){
            parents_[pv] = pu;
        } else if (ranks_[pu] < ranks_[pv]) {
            parents_[pu] = pv;
        } else {
            parents_[pu] = pv;
            ranks_[pu]++;
        }
        return true;
    }
    
    // Find the root of u
    int Find(int u){
        int pu;
        if (u != parents_[u]) parents_[u] = Find(parents_[u]);
        return parents_[u];
    }
};    
};

