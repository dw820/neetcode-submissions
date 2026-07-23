class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)

        max_len = 0
        seen = set()

        for num in nums_set:

            if num in seen:
                continue
            
            seen.add(num)
            l = 1
            
            before = num - 1
            after = num + 1

            while before in nums_set and before not in seen:
                seen.add(before)
                l += 1
                before = before - 1
            
            while after in nums_set and after not in seen:
                seen.add(after)
                l += 1
                after = after + 1
            
            max_len = max(l, max_len)

        return max_len


            

