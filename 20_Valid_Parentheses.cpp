/*
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
*/

#include <iostream>
#include <unordered_map>
#include <stack>
using namespace std;


class Solution {
private:
	unordered_map<char, char> mappings;
public:
	Solution(){
		mappings[')'] = '(';
		mappings[']'] = '[';
		mappings['}'] = '{';
	}
	
	bool isValid(string s) {
		cout << mappings.size() << endl;
		stack<char> myStack;

		for (int i=0; i<s.length(); i++){
			char c = s[i];
			cout << "current:" << c << endl;
			cout << myStack.size() << endl;

			// if current char is a closing bracket
			if ( mappings.find(c) != mappings.end() ){
				//get current top element of stack, if stack is empty, use '#' to indicate
				char topElement =  myStack.empty() ? '#' : myStack.top();
				myStack.pop();
				cout << "top element: " << topElement << endl;
				cout << "mapping value: " << mappings[c] << endl;
				if (topElement != mappings[c]){
					cout << "Reason: not the mapping value" << endl;
					return false;
				} 
			}
			else{
				myStack.push(c);
			}
	}
	return myStack.empty();
}
};
 

int main(){
	Solution sol;
	bool res = sol.isValid("[]");
	cout << "Answer:" << res << endl;
	return 0;
}