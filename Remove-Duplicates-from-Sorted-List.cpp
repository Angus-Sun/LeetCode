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
13    ListNode* deleteDuplicates(ListNode* head) {
14        ListNode *curr = head;
15        ListNode *prev = nullptr;
16        ListNode *temp = nullptr;
17        while (curr) {
18            prev = curr;
19            curr = curr->next;
20            if (curr && prev->val == curr->val) {
21                while (curr && prev->val == curr->val) {
22                    temp = curr;
23                    curr = curr->next;
24                    delete temp;
25                }
26                prev->next = curr;
27            }
28        }
29        return head;
30    }
31};