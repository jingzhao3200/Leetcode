
/*

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
//     // iterative solution
//     ListNode* reverseList(ListNode* head) {
//         ListNode* prev = NULL;
//         ListNode* curr = head;
//         while (curr != NULL){
//             ListNode* temp = curr->next;
//             curr->next = prev;
//             prev = curr;
//             curr = temp;
//         }
//         return prev;
//     }
    
    // recursive solution
    ListNode* reverseList(ListNode* head){
        ListNode* prev = nullptr;
        if (head == nullptr || head->next == nullptr){
            return head;
        }
            
        prev = reverseList(head->next);
        head->next->next = head;
        head->next = nullptr;
        
        return prev;
    }
};