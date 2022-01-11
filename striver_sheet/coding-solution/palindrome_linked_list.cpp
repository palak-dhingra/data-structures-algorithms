/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        
        if(head==NULL || head->next==NULL){
            return true;
        }
        
        ListNode* dummy = head;
        ListNode* slow = head;
        ListNode* fast = head;
        //find middle of linkedlist;
        while(fast->next!=NULL and fast->next->next!=NULL){
            slow = slow->next;
            fast = fast->next->next;
        }
        
        //reverse the linkedlist after slow
        ListNode* prev = NULL;
        ListNode* cur = slow->next;
        ListNode* next = slow->next;
        while(cur!=NULL){
            next = cur->next;
            cur->next = prev;
            prev = cur;
            cur = next;
        }
        
        slow->next = prev;
        slow = slow->next;
        while(slow!=NULL){
            if(dummy->val != slow->val){
                return false;
            }
            
            dummy = dummy->next;
            slow = slow->next;
        }
        
        return true;        
    }
};