class TimeMap:

    def __init__(self):
        self.stamps = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.stamps: 
            self.stamps[key] = [(timestamp, value)]
        else: 
            self.stamps[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.stamps: 
            l = 0
            r = len(self.stamps[key]) - 1 

            while l <= r: 
                
                mid = l + (r - l ) //2

                if self.stamps[key][mid][0] < timestamp: 
                    l = mid + 1
                elif self.stamps[key][mid][0] > timestamp:
                    r = mid - 1
                else: 
                    return self.stamps[key][mid][1] 
                
            if r >= 0:
                return self.stamps[key][r][1]  

        return ""
