class Solution:
    def findNumbers(self, nums: List[int]) -> int:  
        def count_dig(i):
            digits = 0
            while i > 0:
                i = i // 10
                digits += 1
            return digits
                
        res = 0
        for i in nums:
            
            if count_dig(i) % 2 == 0:
                res += 1
        return res
