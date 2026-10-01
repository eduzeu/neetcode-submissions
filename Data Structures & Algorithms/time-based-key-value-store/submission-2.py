class TimeMap:

    def __init__(self):
        self.names = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.names[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:

        list_to_search = self.names[key]

        l, r= 0, len(list_to_search) -1
        ans = ''

        while l <= r: 

            mid = (l + r) // 2

            if list_to_search[mid][1] == timestamp:
                return list_to_search[mid][0]

            elif list_to_search[mid][1] < timestamp: 
                ans = list_to_search[mid][0]
                l = mid + 1
            else:
                r = mid - 1 

        return ans  
        
