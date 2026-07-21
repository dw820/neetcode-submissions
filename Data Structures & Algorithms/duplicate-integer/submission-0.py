class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import defaultdict
        count = defaultdict(int)

        for num in nums:
            if num in count:
                return True
            
            count[num] += 1
        
        return False