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
14    TreeNode* deleteNode(TreeNode* root, int key) {
15        if (!root) {
16            return root;
17        }
18        if (root->val > key) {
19            root->left = deleteNode(root->left, key);
20        } else if (root->val < key) {
21            root->right = deleteNode(root->right, key);
22        } else {
23            if (!root->right) {
24                return root->left;
25            } else if (!root->left) {
26                return root->right;
27            }
28
29            TreeNode *curr = root->right;
30            while (curr->left) {
31                curr = curr->left;
32            }
33            root->val = curr->val;
34            root->right = deleteNode(root->right, root->val);
35        }
36        return root;
37    }
38};