/*
Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.
*/

#include <iostream>
#include <unordered_map>
using namespace std;


class Solution {
public:
    int lengthOfLongestSubstringKDistinct(string s, int k) {
    	int n = s.length();
    	if (n * k==0) return 0;

    	int left = 0, right = 0;
    	int max_len = 0;
    	unordered_map<char, int> charMap;
    	while (right<n){
    		charMap[s[right]] = right;
    		right++;

    		if (charMap.size() == k+1){
    		//delete the left most char
    		left = charMap.begin() -> second;
    		charMap.erase( charMap.begin() );
    		}
    		max_len = max(max_len, right - left);
    	}
    	cout << "len of charMap:" << charMap.size() << endl;
    
        return max_len;
    }
};

int main(){
	Solution sol;
	int res = sol.lengthOfLongestSubstringKDistinct("eceba", 2);
	cout << "Answer:" << res << endl;
	return 0;
}