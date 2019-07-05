#include <iostream>
#include "3. Longest_Substring_Without_Repeating_Characters.cpp"

int main(){
    std::string s = "abcdd";
    Solution solution;
    int res = solution.lengthOfLongestSubstring(s);
    std::string out = std::to_string(res);
    std::cout << out << std::endl;

    return  0;
}
