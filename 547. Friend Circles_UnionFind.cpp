// class Solution {
// public:
//     int findCircleNum(vector<vector<int>>& M) {
//         int ans = 0;
//         int n = M.size();
//         for (int i=0; i<n; i++){
//             if (!M[i][i]) continue;
//             dfs(M, i, n); //use dfs to find continuous region
//             ans++; //increase the counter
//         }
//         return ans;
//     }
// private:
//     void dfs(vector<vector<int>>& M, int curr, int n){
//         for (int i=0; i<n; i++){
//             if (!M[curr][i]) continue; 
//             // don't forget to change the value of visited
//             M[curr][i] = 0;
//             M[i][curr] = 0;
//             dfs(M, i, n);
//         }
        
//     }
// };
class UnionFindSet{
public:
    //constructor
    UnionFindSet(int n){
        parents_ = vector<int>(n+1, 0);
        ranks_ = vector<int>(n+1, 0);
        
        for (int i=0; i<n+1; i++){
            parents_[i] = i;
        }
    }
    bool Union(int u, int v){
        int pu = Find(u);
        int pv = Find(v);
        if (pu==pv) return false; // no need to union, already in
        
        if (ranks_[pu] > ranks_[pv]){
            parents_[pv] = pu;
        } else if (ranks_[pv] > ranks_[pu]){
            parents_[pu] = pv;
        } else {
            parents_[pu] = pv;
            ranks_[pv]++;
        }
        return true;
    }
    int Find(int u){
        if (u != parents_[u]){
            parents_[u] = Find(parents_[u]);
        }
        return parents_[u];
    }

private:
    vector<int> parents_;
    vector<int> ranks_;
};


class Solution{
public:
    int findCircleNum(vector< vector<int> >& M){
        int ans = 0;
        int n = M.size();
        UnionFindSet s(n);
        
        for (int i=0; i<n; i++){
            for (int j=i+1; j<n; j++){
                if (M[i][j] == 1) s.Union(i,j);
            }
        }
        
        unordered_set<int> circles;
        for (int i=0; i<n; i++){
            circles.insert(s.Find(i));
        }
        ans = circles.size();
        
        return ans;
    }
};

