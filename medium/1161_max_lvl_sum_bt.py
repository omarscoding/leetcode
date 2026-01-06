class Solution(object):
    def maxLevelSum(self, root):
        queue = deque()                         # Initialize a queue for BFS
        queue.append(root)                      # Start with the root node
        max_sum = float('-inf')                 # Initialize max_sum to the smallest possible value
        max_level = 0                           
        current_level = 0                       

        while queue: 
            current_level += 1
            level_sum = 0

            nodes_in_level = len(queue)

            for i in range(nodes_in_level):     # Iterate through all nodes at the current level (Won't access nodes of next level due to range function)
                node = queue.popleft()          # Dequeue the front node
                level_sum += node.val

                if node.left:
                    queue.append(node.left)     # Saving the left child to the queue for next level
                if node.right:
                    queue.append(node.right)    # Saving the right child to the queue for next level
            
            # After finishing the current level, check if the level sum is greater than max_sum
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = current_level
            
        return max_level

from collections import deque    

# Example usage:
solution = Solution()
root = [1,7,0,7,-8,None,None]
# The tree structure is as follows:
#         1
#        / \
#       7   0
#      / \
#     7  -8
print(solution.maxLevelSum(root))  # Output: 2

# Time Complexity: O(n), where n is the number of nodes in the binary tree. We visit each node exactly once.
# Space Complexity: O(m), where m is the maximum number of nodes at any level in the binary tree. This is the maximum size of the queue at any point in time.

# Notes
# The max level sum of a binary tree can be found using a breadth-first search (BFS) approach.
# We use a queue to traverse the tree level by level, calculating the sum of node values at each level.
# We keep track of the maximum sum encountered and the corresponding level number.
# By the end of the traversal, we return the level number with the highest sum.
# Using a queue allows us to efficiently manage the nodes at each level and ensures that we process all nodes in the tree.
# Python's deque from the collections module is used for efficient popping from the front of the queue.

# Personal thoughts
# Initially, i found the question quite daunting as it involved tree traversal which i was not very comfortable with.
# However, breaking down the problem into smaller parts helped me understand it better.
# Once i grasped the concept, implementing the BFS approach using a queue became straightforward.