import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            largest_stone = heapq.heappop_max(stones)
            second_largest_stone = heapq.heappop_max(stones)

            if largest_stone == second_largest_stone:
                continue
            
            new_stone = largest_stone - second_largest_stone
            heapq.heappush_max(stones, new_stone)
        
        if not stones:
            return 0
        return heapq.heappop_max(stones)