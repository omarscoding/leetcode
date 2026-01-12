class Solution(object):
    def isAnagram(self, s, t):
        if len(t) != len(s) :
            return False

        dic1, dic2 = {}, {}
        for i in range(len(s)) :
            if s[i] not in dic1 :
                dic1[s[i]] = 0
            else :
                dic1[s[i]] += 1

            if t[i] not in dic2 :
                dic2[t[i]] = 0
            else :
                dic2[t[i]] += 1
        
        for key in dic1 :
            if key in dic2 :
                if dic1[key] == dic2[key] :
                    continue
                else:
                    return False
            else : 
                return False

        return True 



# Example usage:
solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))  # Output: True
print(solution.isAnagram("rat", "car"))          # Output: False

# Notes:
# The function checks if two strings are anagrams by comparing the frequency of each character in both strings.

# Time Complexity: O(n), where n is the length of the strings.
# Space Complexity: O(1), since the character set is limited (e.g., lowercase English letters).