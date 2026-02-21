1/**
2 * Definition for singly-linked list.
3 * struct ListNode {
4 *     int val;
5 *     ListNode *next;
6 *     ListNode() : val(0), next(nullptr) {}
7 *     ListNode(int x) : val(x), next(nullptr) {}
8 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
9 * };
10 */
11class Solution {
12public:
13    ListNode* removeElements(ListNode* head, int val) {
14        ListNode dummy;
15        ListNode *node = &dummy;
16        ListNode *curr = head;
17        while (curr) {
18            if (curr->val != val) {
19                node->next = curr;
20                node = node->next;
21            } 
22            curr = curr->next;
23        }
24        node->next = nullptr;
25        return dummy.next;
26    }
27
28};