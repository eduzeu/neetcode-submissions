class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        

        events = []

        for pas, start, end in trips:
            events.append((start, pas))
            events.append((end, -pas))
        
        events.sort()

        currentCap = 0
        for location, cap in events: 
            currentCap += cap
            if currentCap > capacity:
                return False
        return True
        


        