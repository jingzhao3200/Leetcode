/*
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
*/

#include <iostream>
#include <unordered_map>
using namespace std;


class Solution {
public:
	
	bool isValid(string s) {


        return false;
    }
 
};

int main(){
	Solution sol;
	bool res = sol.isValid("");
	cout << "Answer:" << res << endl;
	return 0;
}