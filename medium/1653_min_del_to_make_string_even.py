class Solution:
    def minimumDeletions(self, s: str) -> int:
        count = 0
        b = 0

        for c in s:
            if c == 'b' :
                b += 1
            elif b :
                count += 1
                b -= 1
        
        return count