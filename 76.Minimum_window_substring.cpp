#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    string minWindow(string s, string t) {
	    
    	if (s.length() == 0 || t.length() == 0){
    		return "";
    	}
    	unordered_map<char, int> dict_t;
    	// get the numnber of chars in t string
    	for (int i=0; i<t.length(); i++){
    		if (dict_t.find(t[i]) == dict_t.end()){
    			dict_t[t[i]] = 1; 
    		} else {
    			dict_t[t[i]]++;
    		}
    		
    	}

    	int required = dict_t.size();
    	// cout << "required: " << required << endl;
    	int left = 0, right = 0;
    	int found = 0;
    	unordered_map <char, int> dict_s;
  		vector<int> result{-1, 0, 0};

    	while (right < s.length()){
    		// cout << "current window: " << s.substr(left, right-left+1) << endl;
    		char current_char = s[right];
    		// cout << "current_char:  " << current_char << endl;
    		// check if already in dict_s, if no, add and set value to 0
    		if (dict_s.find(current_char) == dict_s.end()){
    			dict_s[current_char] = 0;
    		}
    		dict_s[current_char]++;

    		// check if in dict_t, and if match the value in dict_t
    		if (dict_t.find(current_char) != dict_t.end() && 
    			dict_t[current_char] == dict_s[current_char]){
    			found++;
    		}
    		// cout << "found =" << found << endl;
    		while(left <= right && found == required){
    			char current_left_char = s[left];
    			if (result[0] == -1 || right-left+1 < result[0]){
    				result[0] = right - left + 1;
    				result[1] = left;
    				result[2] = right;
    			}

    			dict_s[current_left_char]--;
    			if (dict_t.find(current_left_char) != dict_t.end() && 
    				dict_s[current_left_char] < dict_t[current_left_char]){
    				found--;
    			}
    			left++;
    		}
    		right++;
    		// cout << "pointer: " << left << ", " << right << endl;
    		// cout << "vector: " << result[0] << ", "<< result[1] << ", "<< result[2] << endl;
    		// cout << "current result:" << s.substr(result[1], result[2]-result[1]+1) << endl;
    	}

    	// cout << dict_s.size() << endl;
    	// cout << "found =" << found << endl;
    	
    	if (result[0] == -1){
    		return "";
    	} else {
    		return s.substr(result[1], result[2]-result[1]+1);
    	}
    	
    }
};

int main(){
	Solution sol;
	cout << sol.minWindow("ABAACBAB", "ABC") <<endl;
	return 0;
}