class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        res = 0
        for num in range(left, right + 1):
            bin_num = bin(num)
            one_count = bin_num.count("1")

            if self.is_prime(one_count):
                res += 1
        
        return res
       
    def is_prime(self, n):
            if n < 2:
                return False
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False
            return True
