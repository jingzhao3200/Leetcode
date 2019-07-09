//
// 3. Longest Substring Without Repeating Characters
// Given a string, find the length of the longest substring without repeating characters.
//

#include <iostream>    // std::cout
#include <algorithm>  //std::max
#include <set>
#include <string>
#include <unordered_set>
#include <unordered_map>

class Solution {
public:
    int lengthOfLongestSubstring(std::string s) {
        /* brutal force */
        // int n = s.length();
        // int ans = 0;
        // for (int i=0; i<n; i++){
        //     for (int j=i+1; j<=n; j++){
        //         if (allUnique(s, i, j)){
        //             ans = std::max(ans, j-i);
        //         }
        //     }
        // }

        // /* sliding window */
        // int n = s.length();
        // int ans = 0, i = 0, j = 0;
        // std::unordered_set <char> charSet;
        // while (i<n && j<n){
        //     //try to extend the range[i, j]
        //     if (charSet.find(s[j]) == charSet.end()){ // not in set
        //         charSet.insert(s[j]);
        //         j++;
        //         ans = std::max(ans, j-i);
        //     }
        //     else{
        //         charSet.erase(s[i]);
        //         i++;
        //     }
        // }

        /* sliding window optimized */
        int n = s.length();
        int ans = 0;
        std::unordered_map<char, int> map;
        for (int i=0, j=0; j<n; j++){
            if (map.find(s[j]) != map.end()){
                i = std::max(map[s[j]], i);
            }
            ans = std::max(ans, j-i+1);
            map[s[j]] = j+1;
        }
        return ans;
    }

    // bool allUnique(std::string s, int start, int end){
    //     std::set<char>unique_set;
    //     for (int i=start; i<end; i++){
    //         auto search = unique_set.find(s[i]);
    //         if (search != unique_set.end()){
    //             return false;
    //         }
    //         else{
    //             unique_set.insert(s[i]);
    //         }
    //     }
    //     return true;
    // }
};


int main(){
    std::string s = "abcddef";
    Solution solution;
    int res = solution.lengthOfLongestSubstring(s);
    std::string out = std::to_string(res);
    std::cout << out << std::endl;

    return  0;
}




