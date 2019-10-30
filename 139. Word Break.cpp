/*
139. Word Break
Medium

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
*/


class Solution {
private:
    unordered_map<string, bool> mem_;
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        // change vector to the unordered set
        unordered_set<string> dict(wordDict.begin(), wordDict.end());
        return wordBreak(s, dict);
    }
    
    bool wordBreak(string s, unordered_set<string>dict){
        
        // if already in memory, return
        if (mem_.count(s)) return mem_[s];
        
        // if the s is a word, memories and return
        if (dict.count(s))  return mem_[s] = true;
        
        // otherwise, tranverse and try every split of s
        for (int i=0; i<s.length(); i++){
            // i is the split point, split s into left and right side
            string left = s.substr(0, i);
            string right = s.substr(i);
            
            // check splited left and right if in dict
            if (wordBreak(left, dict) && dict.count(right))
                return mem_[s] = true;
        }
        return mem_[s] = false;
    }
};
