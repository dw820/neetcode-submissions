class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        target_map = {}

        for i in range(len(nums)):
            num = nums[i]

            if num in target_map:
                return [target_map[num], i]

            target_map[target - num] = i