class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0:1} # target_remainder: index
        res = 0
        cur_sum = 0

        for i in range(len(nums)):
            cur_sum += nums[i]

            target_diff = cur_sum - k
        
            if target_diff in prefix:
                res += prefix[target_diff]
        
            if cur_sum in prefix:
                prefix[cur_sum] += 1
            else:
                prefix[cur_sum] = 1
        
        return res
