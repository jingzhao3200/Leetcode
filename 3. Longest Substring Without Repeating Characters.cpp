//
// 3. Longest Substring Without Repeating Characters
// Given a string, find the length of the longest substring without repeating characters.
//

#include <iostream>    // std::cout
#include <algorithm>  //std::max
#include <set>
#include <string>

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.length();
        int ans = 0;
        for (int i=0; i<n; i++){
            for (int j=i+1; j<=n; j++){
                if (allUnique(s, i, j)){
                    ans = std::max(ans, j-i);
                }
            }
        }
        return ans;
    }

    bool allUnique(string s, int start, int end){
        std::set<char> unique_set;
        for (int i=start; i<end; i++){
            auto search = unique_set.find(s[i]);
            if (search != unique_set.end()){
                return false;
            }
            else{
                unique_set.insert(s[i]);
            }
        }
        return true;
    }
};

int main(){
    std::string s = "abcdd";
    int res = Solution.lengthOfLongestSubstring(s);
    string out = to_string(ret);
    std::cout << out << endl;

    return  0;
}