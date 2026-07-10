import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        distances = []
        
        for point in points:
            p_distance = self.distance(point, [0, 0])
            distances.append((p_distance, point))
        
        heapq.heapify(distances)
        for i in range(k):
            result.append(heapq.heappop(distances)[1])
        
        return result


    def distance(self, point1, point2) -> int:
        return math.sqrt(math.pow(point1[0] - point2[0], 2) + math.pow(point1[1] - point2[1], 2))