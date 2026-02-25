class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        dic = {}

        for num in arr :
            dic[num] = bin(num)[2:].count('1')

        arr.sort(key=lambda num: (dic[num], num))

        return arr