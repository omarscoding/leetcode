class Solution(object):
    def groupAnagrams(self, strs):
        res = defaultdict(list)
        for s in strs :
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())
        
# Example usage:
solution = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(solution.groupAnagrams(strs))  # Output: [["eat","tea","ate"],["tan","nat"],["bat"]]

# Time Complexity: O(n * k log k), where n is the number of strings in strs and k is the maximum length of a string in strs.
# Space Complexity: O(n * k), as we are storing all the strings in the hash map.

# Notes
# The group anagrams problem can be efficiently solved using a hash map (dictionary in Python).
# The idea is to sort each string to create a unique key that represents its anagram group.
# We then use this sorted string as the key in the hash map, appending the original string to the list of its corresponding anagram group.
# Using defaultdict, to automatically handle the initialization of lists for new keys, simplifies the code and improves readability.
from collections import defaultdict