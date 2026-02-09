# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrder(self, node, vals) :
        if not node:
            return
        self.inOrder(node.left, vals)
        vals.append(node.val)
        self.inOrder(node.right, vals)

    def build(self, vals, l, r) :
        if l > r :
            return None
        
        mid = (l + r) // 2
        node = TreeNode(vals[mid])
        node.left = self.build(vals, l, mid - 1)
        node.right = self.build(vals, mid + 1, r)
        return node
    
    def balanceBST(self, root) :
        vals = []
        self.inOrder(root, vals)
        return self.build(vals, 0, len(vals) - 1)