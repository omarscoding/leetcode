class Solution:
    def binaryGap(self, n: int) -> int:
        bin_n = bin(n)[2:]
        count = 0
        res = 0
        track = False
        for i in bin_n:
            if i == '1' :
                if track:
                    res = max(count + 1, res)
                track = True
                count = 0
            elif track:
                count += 1
            
        return res