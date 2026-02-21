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
13    bool isPalindrome(ListNode* head) {
14        ListNode *slow = head;
15        ListNode *fast = head;
16        while (fast && fast->next) {
17            fast = fast->next->next;
18            slow = slow->next;
19        }
20        ListNode *prev = nullptr;
21        ListNode *temp = nullptr;
22        ListNode *curr = slow;
23
24        while (curr) {
25            prev = curr;
26            curr = curr->next;
27            prev->next = temp;
28            temp = prev;
29        }
30        ListNode* left = head;
31        ListNode *right = prev;
32        while (right) {
33            if (left->val != right->val) {
34                return false;
35            }
36            left = left->next;
37            right = right->next;
38        }
39        return true;
40    }
41};