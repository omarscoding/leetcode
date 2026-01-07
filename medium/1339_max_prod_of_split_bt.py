class Solution(object):
    def maxProduct(self, root):
        value = 0
        sub_tree_sum = []

        def get_sums(node):
            if not node:
                return 0
            value = node.val + get_sums(node.left) + get_sums(node.right)
            sub_tree_sum.append(value)
            return value

        greatest_prod = 0
        total = get_sums(root)

        for i in sub_tree_sum:
            greatest_prod = max(greatest_prod, i * (total - i))
        return greatest_prod % (10**9 + 7)
    

# Time Complexity: O(n), where n is the number of nodes in the binary tree.
# Space Complexity: O(h), where h is the height of the binary tree due to the recursion stack.

# Notes
# The function calculates the maximum product of the sums of two subtrees formed by splitting a binary tree at any edge.
# It first computes the total sum of the tree and stores the sums of all subtrees in a list.
# Then, it iterates through the list of subtree sums to find the maximum product of the sum of a subtree and the sum of the remaining tree.
# The result is returned modulo 10^9 + 7 to handle large numbers.

# Example usage:
solution = Solution()
root = [1,2,3,4,5,6]
print(solution.maxProduct(root))  # Output: 110

# Personal Thoughts
# I did not enjoy todays leetcode
# I could not get it initially
# Now that I got the solution, when i look back it all makes sense
