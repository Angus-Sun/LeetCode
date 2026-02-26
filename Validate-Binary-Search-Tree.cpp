1/**
2 * Definition for a binary tree node.
3 * struct TreeNode {
4 *     int val;
5 *     TreeNode *left;
6 *     TreeNode *right;
7 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
8 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
9 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
10 * };
11 */
12class Solution {
13public:
14    bool isValidBST(TreeNode* root) {
15        return (isValid(root, LONG_MIN, LONG_MAX));
16    }
17    bool isValid(TreeNode* node, long left, long right) {
18        if (!node) {
19            return true;
20        }
21        if (!(left < node->val && right > node->val)) {
22            return false;
23        }
24        return (isValid(node->left, left, node->val) && isValid(node->right, node->val, right));
25    }
26};