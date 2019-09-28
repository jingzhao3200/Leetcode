class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
       
        unordered_map<int, vector<int>> graph; // graph: node, neighbors
        for (const auto& edge : edges){
            int u = edge[0];
            int v = edge[1];
            
            unordered_set<int> visited;
            if (hasPath(u, v, graph, visited)) // if find path in graph, return this edge
                return edge;
            
            graph[u].push_back(v); // if not, add this edge to graph
            graph[v].push_back(u); // no direction, so add from both direction
        }
        return {};
    }
    
private:
    // DFS to find path
    bool hasPath(int curr, int goal, 
                const unordered_map<int, vector<int>>& graph,
                unordered_set<int>& visited){
        if (curr == goal)
            return true;
        visited.insert(curr); // no need to clean
        if (!graph.count(curr) || !graph.count(goal)) //if either not in graph, no path 
            return false;
        for (int next : graph.at(curr)){ //visit all its neighbors to find if has path to goal, see whether can find v
            if (visited.count(next)) continue;
            if (hasPath(next, goal, graph, visited))
                return true;
        }
        return false;
    }
    
    
};
