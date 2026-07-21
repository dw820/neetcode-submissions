class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        import heapq

        counter = defaultdict(int)

        for num in nums:
            counter[num] += 1
        
        h = []

        for key, value in counter.items():
            heapq.heappush(h, (-value, key))

        ans = []

        for _ in range(k):
            _, key = heapq.heappop(h)

            ans.append(key)

        return ans
