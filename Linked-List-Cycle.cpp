1/**
2 * Definition for singly-linked list.
3 * struct ListNode {
4 *     int val;
5 *     ListNode *next;
6 *     ListNode(int x) : val(x), next(NULL) {}
7 * };
8 */
9class Solution {
10public:
11    bool hasCycle(ListNode *head) {
12        ListNode *fast = head;
13        ListNode *slow = head;
14        while (fast && fast->next) {
15            fast = fast->next->next;
16            slow = slow->next;
17            if (slow == fast) {
18                return true;
19            }
20        }
21        return false;
22    }
23};