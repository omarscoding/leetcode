class Solution(object):
    def subtreeWithAllDeepest(self, root):
        
        def dfs(node):
            # Returns (deepest_node_in_subtree, depth_of_that_node)
            if not node:
                return (None, 0)
            
            # Get info from left and right subtrees
            left_node, left_depth = dfs(node.left)
            right_node, right_depth = dfs(node.right)

            # If left subtree is deeper
            if left_depth > right_depth:
                return (left_node, left_depth + 1)
            
            # If right subtree is deeper
            elif right_depth > left_depth:
                return (right_node, right_depth + 1)
            
            # If both subtrees have same depth, current node is the LCA
            else :
                return (node, left_depth + 1)

        # dfs(root)[0] extracts just the first element of the tuple returned by dfs:
        return dfs(root)[0]
        

# Example usage:
solution = Solution()
root = [3,5,1,6,2,0,8,null,null,7,4]
print(solution.subtreeWithAllDeepest(root))  # Output: [2,7,4]

# Time Complexity: O(n), where n is the number of nodes in the binary tree. We visit each node exactly once.
# Space Complexity: O(h), where h is the height of the binary tree. This space is used by the recursion stack.

# Notes
# The problem of finding the smallest subtree containing all the deepest nodes can be efficiently solved using a depth-first search (DFS) approach.
# The idea is to traverse the tree recursively, calculating the depth of each subtree.
# At each node, we compare the depths of the left and right subtrees:
# If the left subtree is deeper, we continue searching in the left subtree.
# If the right subtree is deeper, we continue searching in the right subtree.
# If both subtrees have the same depth, the current node is the lowest common ancestor of the deepest nodes, and we return it.
# We use a helper function dfs that returns a tuple containing the node and its depth.

from collections import defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Personal Thoughts
# I didn't enjoy this, however I do need the practice on questions with nodes 
# #weloveclaude