/*
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
*/

class Solution {
public:
    string longestPalindrome(string s) {
        const int size_s = s.size();
        int max_s = 0, max_l = 0;
        
        for (int i = 0; i < size_s ;  ){
            int start = i, end = i;
            while ( end+1 < size_s && s[end] == s[end + 1]){
                end++;
            }
            i = end + 1;
            while ( start-1 >=0 && end + 1< size_s && s[start-1] == s[end+1]){
                start--;
                end++;
            }
            if (end - start + 1 > max_l){
                max_s = start;
                max_l = end - start + 1;
                
            }
        }
        
        return s.substr(max_s, max_l);
    }
};
