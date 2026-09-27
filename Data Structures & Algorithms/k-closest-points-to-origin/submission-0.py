import heapq 
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def getDistance(x1, x2, y1, y2): 
            return (math.sqrt((x1 - x2)**2 + (y1 - y2)**2))
        
        res = []

        for point in points: 
            total = getDistance(point[0], 0, point[1], 0)
            res.append([total, point])
        
         
        heapq.heapify(res)
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(res)[1])
        

        # print(res)

        return ans



            
        






        